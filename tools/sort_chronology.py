#!/usr/bin/env python3
"""Merge and sort notes/chronology-working.md (incremental, many appended sections)
into a year-ordered draft on stdout. Lines are '- <date phrase> — <event> — <source>'.
The leading date phrase is parsed into a sort key; unparseable lines go last.
Usage: python3 -I tools/sort_chronology.py > /tmp/x.md  (then review by hand)"""
import re, sys
MON = {m: i for i, m in enumerate('jan feb mar apr may jun jul aug sep oct nov dec'.split(), 1)}
SEASON = {'spring': 4, 'summer': 7, 'fall': 9, 'autumn': 9, 'winter': 12, 'late': 10, 'early': 2, 'mid': 6}
def key(phrase):
    p = phrase.lower()
    m = re.search(r'(\d{4})-(\d\d)(?:-(\d\d))?', p)
    if m: return (int(m.group(1)), int(m.group(2)), int(m.group(3) or 0))
    y = re.search(r'(19|20)\d\d', p)
    if not y: return None
    year = int(y.group(0)); before = p[:y.start()]
    mon = 0
    for name, i in MON.items():
        if re.search(r'\b' + name, before): mon = i; break
    if not mon:
        for name, i in SEASON.items():
            if name in before: mon = i; break
    if 'before' in before: return (year, 0, -1)
    return (year, mon, 0)
items, undated = [], []
section, last_src = '', ''
for line in open('notes/chronology-working.md', encoding='utf-8'):
    if line.startswith('#'): section = line.strip('# \n'); continue
    if not line.startswith('- '): continue
    line = line.rstrip('\n'); parts = line[2:].split(' — ')
    if len(parts) < 3:   # no explicit source: default from the section heading
        line += ' — ' + ('AAL' if section == 'An Algorithmic Lucidity' else 'UUT' if section.startswith('20') else '(source: see notes)')
        parts = line[2:].split(' — ')
    src = parts[-1]
    if src.startswith('ibid'):   # resolve "ibid." to the previous line's source in the working file
        line = line[: line.rfind(' — ')] + ' — ' + last_src + src[len('ibid.'):].rstrip()
    else:
        last_src = src
    phrase = parts[0]
    k = key(phrase)
    (items if k else undated).append((k, line))
items.sort(key=lambda x: x[0])
year = None
for k, line in items:
    if k[0] != year:
        year = k[0]; print(f'\n## {year}')
    print(line)
print('\n## Undatable lines'); [print(l) for _, l in undated]
