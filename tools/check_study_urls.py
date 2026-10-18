#!/usr/bin/env python3
"""Check the corpus links in the study's HTML against the local corpus files.

Usage (from the project root):
    python3 -I tools/check_study_urls.py study/*.html

For every link to a blog post (zackmdavis.net/blog/YYYY/Mon/stem/ or
unremediatedgender.space/YYYY/Mon/stem/), checks that AAL_content/YYYY/stem.md
(resp. UUT_content/YYYY/stem.md) exists and that its Date header falls in that
month. Hidden pages (unremediatedgender.space/ancillary/<rel>/) must exist under
UUT_content/pages/ancillary/. LessWrong post links (lesswrong.com/posts/<id>)
must match the LessWrong-URL header of some LW_content file or the post id of
a thread in reception_data/lw_threads/. Gitweb draft links must be pinned to a
commit hash (hb=<40 hex>) and name a file that exists in the local drafts
directory. Also reports any data-src path that does not exist.
"""
import glob
import os
import re
import sys

MON = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()


def date_month(path):
    t = open(path, encoding='utf-8').read()
    m = re.search(r'^Date:\s*(\d{4})-(\d\d)', t, re.M)
    return (m.group(1), MON[int(m.group(2)) - 1]) if m else None


lw_ids = set()
for f in glob.glob('LW_content/*/*.md'):
    m = re.search(r'^LessWrong-URL:\s*\S*/posts/([A-Za-z0-9]+)', open(f, encoding='utf-8').read(), re.M)
    if m:
        lw_ids.add(m.group(1))
for f in glob.glob('reception_data/lw_threads/*.md'):
    for m in re.finditer(r'lesswrong\.com/posts/([A-Za-z0-9]+)', open(f, encoding='utf-8').read()[:3000]):
        lw_ids.add(m.group(1))

for f in ['notes/reception.md', 'notes/sources.md']:  # LW posts fetched as reception sources
    for m in re.finditer(r'lesswrong\.com/posts/([A-Za-z0-9]+)', open(f, encoding='utf-8').read()):
        lw_ids.add(m.group(1))

bad = 0
for hf in sys.argv[1:]:
    text = open(hf, encoding='utf-8').read()
    for i, line in enumerate(text.split('\n'), 1):
        for m in re.finditer(r'href="([^"]+)"', line):
            u = m.group(1)
            mm = re.match(r'https?://(zackmdavis\.net/blog|unremediatedgender\.space)/(\d{4})/([A-Z][a-z]{2})/([^/]+)/', u)
            if mm:
                site, y, mo, stem = mm.groups()
                root = 'AAL_content' if site.startswith('zack') else 'UUT_content'
                p = f'{root}/{y}/{stem}.md'
                if not os.path.exists(p):
                    print(f'{hf}:{i}: no local file {p} for {u}'); bad += 1
                elif date_month(p) != (y, mo):
                    print(f'{hf}:{i}: date mismatch {u} vs {p} {date_month(p)}'); bad += 1
                continue
            mm = re.match(r"https?://unremediatedgender\.space/ancillary/(.+)/(?:#.*)?$", u)
            if mm:
                p = f'UUT_content/pages/ancillary/{mm.group(1)}.md'
                if not os.path.exists(p):
                    print(f'{hf}:{i}: no hidden page {p}'); bad += 1
                continue
            mm = re.match(r'https?://www\.lesswrong\.com/posts/([A-Za-z0-9]+)', u)
            if mm and mm.group(1) not in lw_ids:
                print(f'{hf}:{i}: LW post id {mm.group(1)} not found locally'); bad += 1
                continue
            if 'a=blob' in u and 'source?p=' in u:
                h = re.search(r'hb=([0-9a-f]+)', u)
                f = re.search(r'f=content/drafts/([^;&]+)', u)
                if not h or len(h.group(1)) != 40:
                    print(f'{hf}:{i}: draft link not pinned to a full hash: {u}'); bad += 1
                root = 'AAL_content' if 'An_Algorithmic_Lucidity' in u else 'UUT_content'
                if f and not os.path.exists(f'{root}/drafts/{f.group(1)}'):
                    print(f'{hf}:{i}: no local draft {root}/drafts/{f.group(1)}'); bad += 1
        for m in re.finditer(r'data-src="([^"]+)"', line):
            if not os.path.exists(m.group(1)):
                print(f'{hf}:{i}: data-src missing {m.group(1)}'); bad += 1
print(f'{bad} problems')
sys.exit(1 if bad else 0)
