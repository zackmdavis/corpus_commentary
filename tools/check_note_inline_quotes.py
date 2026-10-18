#!/usr/bin/env python3
"""Check double-quoted fragments inside non-blockquote note lines (summaries etc.)
against the entry's source file. Complements check_note_quotes.py, which covers
only `> ` blockquote lines. Fragments shorter than MIN chars are skipped; "…"
inside a fragment splits it into pieces that must appear in order. Straight and
curly quotes, apostrophes, and markdown emphasis are normalized away.
Reports candidates for human review (some hits are legitimate: quoted titles,
quotations of third parties found in a different file, scare quotes).
Usage: python3 -I tools/check_note_inline_quotes.py notes/UUT-drafts.md ..."""
import sys, re
MIN = 25
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'[_*`"\']', '', s)                      # emphasis and all quote marks (nested-quote style varies)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)   # markdown links -> text
    s = re.sub(r'</?[A-Za-z][^<>\n]{0,200}>', '', s)        # real HTML tags only (a stray '<' must not eat text)
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = total = 0
for nf in sys.argv[1:]:
    src = None; srctext = ''
    for i, line in enumerate(open(nf, encoding='utf-8'), 1):
        m = re.search(r'Path:\s*`([^`]+)`', line)
        if m:
            src = m.group(1)
            try: srctext = norm(open(src, encoding='utf-8').read())
            except OSError: srctext = ''
        if not src or line.startswith('> ') or 'Path:' in line or line.lstrip().startswith('- Xrefs'):
            continue
        frags = re.findall(r'"([^"]*)"', line.replace('“', '"').replace('”', '"'))
        for frag in [f for f in frags if len(f) >= MIN]:
            frag = re.sub(r'[.,;:!?]+$', '', frag.strip())         # punctuation moved inside the closing quote
            pieces = [norm(p) for p in re.split(r'\s*(?:…|\.\.\.|\s/\s)\s*', frag) if norm(p)]  # "/" = verse line break
            pieces = [re.sub(r'^\[|\]$', '', p) for p in pieces]
            total += 1
            pos, ok = 0, True
            for p in pieces:
                j = srctext.find(p, pos)
                if j < 0: ok = False; break
                pos = j + len(p)
            if not ok:
                bad += 1; print(f'{nf}:{i}: not found in {src}: "{frag[:110]}"')
print(f'{total} inline fragments checked, {bad} to review')
