#!/usr/bin/env python3
"""Convert a saved HTML page to plain text for quote checking.
Usage: python3 -I tools/html_to_text.py IN.html OUT.txt
Drops script/style/nav content, keeps text with paragraph breaks. Output is
what Part B reception entries cite as `Path:` (so check_note_quotes.py works)."""
import sys, html
from html.parser import HTMLParser

SKIP = {'script', 'style', 'noscript', 'svg', 'head'}
BLOCK = {'p', 'div', 'br', 'li', 'blockquote', 'h1', 'h2', 'h3', 'h4', 'h5',
         'h6', 'tr', 'section', 'article', 'pre', 'hr', 'dd', 'dt'}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in SKIP: self.skip += 1
        elif tag in BLOCK: self.out.append('\n')
    def handle_endtag(self, tag):
        if tag in SKIP: self.skip = max(0, self.skip - 1)
        elif tag in BLOCK: self.out.append('\n')
    def handle_data(self, data):
        if not self.skip: self.out.append(data)

p = P()
p.feed(open(sys.argv[1], encoding='utf-8', errors='replace').read())
text = ''.join(p.out)
lines = [' '.join(l.split()) for l in text.split('\n')]
res, blank = [], False
for l in lines:
    if l: res.append(l); blank = False
    elif not blank: res.append(''); blank = True
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(res).strip() + '\n')
