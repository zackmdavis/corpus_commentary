#!/usr/bin/env python3
"""Verify every quotation in the pilot chapter against its source file.

Usage: python3 -I pilot/fable/tools/check_quotes.py pilot/fable/parts/*.html
Quotations are <q data-src="PATH">...</q> (inline) or <blockquote data-src="PATH">...</blockquote>.
PATH is relative to the project root. Both sides are normalized (markdown emphasis and link
syntax stripped, HTML tags stripped, entities unescaped, quotes straightened, whitespace
collapsed). A quotation may contain [...] / […] ellipses; each segment must occur in the source.
"""
import sys, re, html, os

def norm(s):
    s = html.unescape(s)
    s = re.sub(r'<[^>]+>', '', s)                     # html tags
    s = re.sub(r'\[ref\].*?\[/ref\]', '', s, flags=re.S)  # pelican footnotes in sources
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)         # images
    s = re.sub(r'\[([^\]]*)\]\((?:[^()]|\([^()]*\))*\)', r'\1', s)     # md links -> text (one nested paren level)
    s = s.translate(str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789'))  # subscript digits
    s = re.sub(r'\$([^$\n]{1,60})\$', lambda m: re.sub(r'[_{}\\]', '', m.group(1)), s)  # inline latex: $x_{41}$ -> x41
    s = re.sub(r'[${}]', '', s)                         # stray latex delimiters/braces
    s = re.sub(r'\[\^[^\]]*\]', '', s)                 # footnote markers [^x]
    s = s.replace('**', '').replace('`', '')
    s = re.sub(r'(?<![\w])_(?=\S)|(?<=\S)_(?![\w])', '', s)  # md italics underscores at word edges
    s = re.sub(r'(?<![\w])\*(?=\S)|(?<=\S)\*(?![\w])', '', s)
    for a, b in [('‘', "'"), ('’', "'"), ('“', '"'), ('”', '"'), (' ', ' '),
                 ('–', '-'), ('—', '-'), (' ', ' ')]:
        s = s.replace(a, b)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

cache = {}
def source(path):
    if path not in cache:
        cache[path] = norm(open(path, encoding='utf-8').read())
    return cache[path]

bad = 0; total = 0
for f in sys.argv[1:]:
    text = open(f, encoding='utf-8').read()
    for m in re.finditer(r'<(q|blockquote)\s+data-src="([^"]+)"[^>]*>(.*?)</\1>', text, flags=re.S):
        tag, path, body = m.groups()
        total += 1
        if not os.path.exists(path):
            print(f'{f}: MISSING SOURCE {path}'); bad += 1; continue
        src = source(path)
        q = norm(body)
        segs = [s.strip() for s in re.split(r'\[\.\.\.\]|\[…\]|…', q) if s.strip()]
        for seg in segs:
            if seg not in src:
                bad += 1
                print(f'{f}: NOT FOUND in {path}:\n    {seg[:200]}')
print(f'{total} quotations checked, {bad} problems')
sys.exit(1 if bad else 0)
