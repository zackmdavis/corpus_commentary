#!/usr/bin/env python3
"""Check every quotation in pilot/opus/chapter.html against its tagged source.

Usage (from the project root): python3 -I pilot/opus/verify_quotes.py [chapter.html]

Each <q data-src=PATH> and <blockquote data-src=PATH> is extracted (for
blockquotes, the <p> elements other than the attribution line). Quote and source
are normalized the same way: HTML entities decoded, tags removed, Markdown link
targets/emphasis markers/backslash escapes removed, quotation marks and square
brackets removed, whitespace collapsed. A quote may contain "[…]"/"[...]" elisions;
each fragment between elisions must occur in the source. Exits nonzero on failure.
"""
import html, re, sys
from html.parser import HTMLParser

CHAPTER = sys.argv[1] if len(sys.argv) > 1 else 'pilot/opus/chapter.html'

class Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []      # (tag, src, buffer, is_attr_p)
        self.quotes = []     # (src, text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('q', 'blockquote') and 'data-src' in a:
            self.stack.append([tag, a['data-src'], [], False])
        elif tag == 'p' and self.stack and self.stack[-1][0] == 'blockquote':
            self.stack[-1][3] = (a.get('class') == 'attr')
            if not self.stack[-1][3]:
                self.stack[-1][2].append('\n')
    def handle_endtag(self, tag):
        if self.stack and tag == self.stack[-1][0]:
            t, src, buf, _ = self.stack.pop()
            self.quotes.append((src, ''.join(buf)))
            if self.stack:  # nested q inside blockquote: keep text in parent too
                self.stack[-1][2].append(''.join(buf))
        elif tag == 'p' and self.stack and self.stack[-1][0] == 'blockquote':
            self.stack[-1][3] = False
    def handle_data(self, data):
        if self.stack and not self.stack[-1][3]:
            self.stack[-1][2].append(data)

QUOTE_CHARS = '"\'“”‘’`'

def norm(s):
    s = html.unescape(s)
    s = re.sub(r'<[^>]+>', ' ', s)                      # html tags
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', s)          # md images
    s = re.sub(r'\]\((?:[^()]|\([^()]*\))*\)', ']', s)   # md link targets
    s = re.sub(r'\{static\}', '', s)
    s = s.replace('\\', '')
    s = re.sub(r'(?<![A-Za-z0-9])[_*]+|[_*]+(?![A-Za-z0-9])', '', s)  # emphasis markers
    s = s.replace('**', '')
    s = re.sub(r'-\n(?=[a-z])', '', s)                   # pdf hyphenation at line end
    for c in QUOTE_CHARS + '[]':
        s = s.replace(c, '')
    s = s.replace(' ', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def fragments(q):
    parts = re.split(r'\[\s*(?:…|\.\.\.)\s*\]', q)
    return [p for p in (norm(x) for x in parts) if p]

def main():
    ex = Extract()
    ex.feed(open(CHAPTER, encoding='utf-8').read())
    cache, fails = {}, 0
    for src, q in ex.quotes:
        if src not in cache:
            try:
                cache[src] = norm(open(src, encoding='utf-8', errors='replace').read())
            except FileNotFoundError:
                print(f'MISSING SOURCE {src}'); fails += 1; cache[src] = None; continue
        text = cache[src]
        if text is None:
            continue
        for frag in fragments(q):
            # also strip a trailing period from the quote fragment if the source lacks it
            ok = frag in text or frag.rstrip('.,;:!?') in text
            if not ok:
                fails += 1
                print(f'FAIL [{src}]\n   {frag[:300]}\n')
    print(f'{len(ex.quotes)} quotations checked; {fails} failures')
    sys.exit(1 if fails else 0)

main()
