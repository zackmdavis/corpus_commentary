#!/usr/bin/env python3
"""Fetch the public Isso comment threads for every published UUT post and
render each non-empty thread to text for the reception survey.
Usage: python3 -I tools/fetch_isso.py UUT_content OUTDIR
Reads each post's Date/Status headers to build its live path
/YYYY/Mon/<stem>/, queries http://unremediatedgender.space/isso/?uri=<path>
(the same public endpoint the blog's comment widget uses), and writes
OUTDIR/raw/<YYYY>_<stem>.json plus OUTDIR/<YYYY>_<stem>.md for threads with
comments. Only author display names, dates, likes, and text are rendered;
email hashes and websites are dropped."""
import sys, os, re, json, time, html, datetime, urllib.request, urllib.parse

src, out = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(out, 'raw'), exist_ok=True)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def text(h):
    h = re.sub(r'<br\s*/?>', '\n', h)
    h = re.sub(r'</p>\s*<p>', '\n\n', h)
    h = re.sub(r'<blockquote>\s*', '\n> ', h)
    h = re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', h)
    h = re.sub(r'<[^>]+>', '', h)
    return html.unescape(h).strip()

def walk(c, depth, lines, base):
    when = datetime.datetime.fromtimestamp(c['created'], datetime.timezone.utc).date()
    lines.append(f"{'#' * 4} [{'>' * depth or '-'}] {c.get('author') or 'Anonymous'} · "
                 f"{c.get('likes', 0)} likes · {when} · {base}#isso-{c['id']}")
    lines.append(text(c.get('text', '')))
    lines.append('')
    for r in c.get('replies', []):
        walk(r, depth + 1, lines, base)

n_threads = n_comments = 0
for year in sorted(os.listdir(src)):
    if not year.isdigit(): continue
    for fn in sorted(os.listdir(os.path.join(src, year))):
        if not fn.endswith('.md'): continue
        hdr = open(os.path.join(src, year, fn), encoding='utf-8').read().split('\n\n', 1)[0]
        if re.search(r'^Status:\s*(draft|hidden)', hdr, re.M | re.I): continue
        m = re.search(r'^Date:\s*(\d{4})-(\d{2})', hdr, re.M)
        if not m: continue
        stem = fn[:-3]
        path = f'/{m.group(1)}/{MON[int(m.group(2)) - 1]}/{stem}/'
        url = 'http://unremediatedgender.space/isso/?uri=' + urllib.parse.quote(path, safe='')
        try:
            data = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'corpus-study'}), timeout=30))
        except Exception as e:
            continue  # 404 = no thread
        finally:
            time.sleep(0.3)
        if not data.get('replies'): continue
        base = 'http://unremediatedgender.space' + path
        json.dump(data, open(os.path.join(out, 'raw', f'{year}_{stem}.json'), 'w'))
        lines = [f'Post: {base}', f'Fetched: {datetime.date.today()} (public Isso API)',
                 f"Comments: {data.get('total_replies')} top-level", '']
        for c in data['replies']:
            walk(c, 0, lines, base)
        cnt = sum(1 for l in lines if l.startswith('#### '))
        open(os.path.join(out, f'{year}_{stem}.md'), 'w', encoding='utf-8').write('\n'.join(lines))
        n_threads += 1; n_comments += cnt
        print(cnt, path)
print(f'{n_threads} threads, {n_comments} comments')
