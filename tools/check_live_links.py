#!/usr/bin/env python3
"""Fetch every external link in study/*.html and record its HTTP status.
Usage: python3 -I tools/check_live_links.py OUT.tsv

Uses curl (GET, redirects followed, 40 s timeout), at most two requests at a
time per host and eight overall. Writes url, final status, final URL and curl
error to OUT.tsv, and prints the links whose final status is not 2xx.
check_study_urls.py checks link patterns against the local files; this checks
that the links resolve on the live web.
"""
import collections, concurrent.futures as cf, glob, html, re, subprocess, sys, threading, time

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'
urls = set()
for f in glob.glob('study/*.html'):
    for h in re.findall(r'href="(https?://[^"]+)"', open(f, encoding='utf-8').read()):
        urls.add(html.unescape(h))

host_locks = collections.defaultdict(lambda: threading.Semaphore(2))


def host(u):
    return re.sub(r'^https?://(www\.)?', '', u).split('/')[0]


def fetch(u):
    with host_locks[host(u)]:
        time.sleep(0.5)
        r = subprocess.run(['curl', '-sS', '-L', '-o', '/dev/null', '--max-time', '40', '-A', UA,
                            '-w', '%{http_code}\t%{url_effective}', u],
                           capture_output=True, text=True)
        code, _, final = r.stdout.partition('\t')
        return u, code or '000', final, r.stderr.strip().replace('\t', ' ')


rows = []
with cf.ThreadPoolExecutor(8) as ex:
    for row in ex.map(fetch, sorted(urls)):
        rows.append(row)
with open(sys.argv[1], 'w', encoding='utf-8') as out:
    out.write('url\tstatus\tfinal_url\terror\n')
    for r in rows:
        out.write('\t'.join(r) + '\n')
bad = [r for r in rows if not r[1].startswith('2')]
print(f'{len(rows)} links; {len(bad)} not 2xx')
for u, code, final, err in bad:
    print(code, u, ('-> ' + final) if final != u else '', err)
