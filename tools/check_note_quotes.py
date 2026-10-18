#!/usr/bin/env python3
"""Check quotations in survey notes against source files.
Convention in notes: each post entry has a line containing `Path: `<file>`` and
quotes are blockquote lines beginning `> ` that follow it (until the next Path).
A quote passes if, after collapsing whitespace, it is a substring of the source
file (also collapsed). Usage: python3 -I tools/check_note_quotes.py notes/AAL-2012.md ..."""
import sys, re
def norm(s): return re.sub(r'\s+', ' ', s).strip()
bad = total = 0
for nf in sys.argv[1:]:
    src = None; srctext = ''
    for i, line in enumerate(open(nf, encoding='utf-8'), 1):
        m = re.search(r'Path:\s*`([^`]+)`', line)
        if m:
            src = m.group(1)
            try: srctext = norm(open(src, encoding='utf-8').read())
            except OSError: print(f'{nf}:{i}: MISSING SOURCE {src}'); srctext = ''; bad += 1
            continue
        if line.startswith('> ') and src:
            q = norm(line[2:])
            # allow an ellipsis "…" marking an elision between verbatim fragments
            parts = [norm(x) for x in q.split(' […] ')]
            total += 1
            pos, ok = 0, True
            for part in parts:
                j = srctext.find(part, pos)
                if j < 0: ok = False; break
                pos = j + len(part)
            if not ok:
                bad += 1; print(f'{nf}:{i}: NOT FOUND in {src}: {q[:100]}')
print(f'{total} quotes checked, {bad} problems')
sys.exit(1 if bad else 0)
