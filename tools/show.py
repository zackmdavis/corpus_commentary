#!/usr/bin/env python3
"""Print corpus files for reading, each preceded by path, live URL, and word count.
Usage: python3 -I tools/show.py FILE...   (run from the project root)"""
import sys, re, os
MON = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
def url(path, text):
    m = re.search(r'^Date:\s*(\d{4})-(\d\d)', text, re.M)
    stem = os.path.splitext(os.path.basename(path))[0]
    if path.startswith('UUT_content/pages/'):  # pages are live (Hidden ones unlisted): /about/, /ancillary/<rel>/
        rel = os.path.splitext(path[len('UUT_content/pages/'):])[0]
        return f'http://unremediatedgender.space/{rel}/'
    if '/drafts/' in path or '/pages/' in path or not m: return '(no live URL: cite file path)'
    y, mo = m.group(1), MON[int(m.group(2))-1]
    if path.startswith('AAL_content'): return f'https://zackmdavis.net/blog/{y}/{mo}/{stem}/'
    if path.startswith('UUT_content'): return f'http://unremediatedgender.space/{y}/{mo}/{stem}/'
    m = re.search(r'^LessWrong-URL:\s*(\S+)', text, re.M)
    return m.group(1) if m else '?'
for p in sys.argv[1:]:
    t = open(p, encoding='utf-8').read()
    print(f'\n######## {p} | {url(p, t)} | {len(t.split())} w\n')
    print(t)
