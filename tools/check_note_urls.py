#!/usr/bin/env python3
"""Check that each `Path:` in notes is paired with the URL tools/show.py would compute.
Usage: python3 -I tools/check_note_urls.py notes/*.md"""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
MON = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
def url(path):
    t = open(path, encoding='utf-8').read()
    m = re.search(r'^Date:\s*(\d{4})-(\d\d)', t, re.M)
    stem = os.path.splitext(os.path.basename(path))[0]
    if path.startswith('UUT_content/pages/'):  # pages are live (Hidden ones unlisted): /about/, /ancillary/<rel>/
        rel = os.path.splitext(path[len('UUT_content/pages/'):])[0]
        return f'http://unremediatedgender.space/{rel}/'
    if '/drafts/' in path or '/pages/' in path or not m: return None
    y, mo = m.group(1), MON[int(m.group(2))-1]
    if path.startswith('AAL_content'): return f'https://zackmdavis.net/blog/{y}/{mo}/{stem}/'
    if path.startswith('UUT_content'): return f'http://unremediatedgender.space/{y}/{mo}/{stem}/'
    m = re.search(r'^LessWrong-URL:\s*(\S+)', t, re.M)
    return m.group(1) if m else None
bad = 0
for nf in sys.argv[1:]:
    for i, line in enumerate(open(nf, encoding='utf-8'), 1):
        for m in re.finditer(r'`((?:AAL|UUT|LW)_content/[^`]+\.(?:md|html))`', line):
            p = m.group(1)
            if not os.path.exists(p): print(f'{nf}:{i}: missing file {p}'); bad += 1; continue
            u = url(p)
            if u and 'http' in line and u not in line and line.lstrip().startswith('- Path'):
                print(f'{nf}:{i}: URL mismatch for {p}: expected {u}'); bad += 1
print(f'{bad} problems'); sys.exit(1 if bad else 0)
