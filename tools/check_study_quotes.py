#!/usr/bin/env python3
"""Check every quotation in the study's HTML files against its tagged source.

Usage (from the project root):
    python3 -I tools/check_study_quotes.py study/*.html

Each <q data-src=PATH> and <blockquote data-src=PATH> is extracted (for a
blockquote, every element except a <p class="attr"> attribution line). PATH is
relative to the project root: a corpus file, a reception_data/ thread file, or a
research/<slug>/text.txt file. Quote and source are normalized the same way:
HTML entities decoded, tags removed, Markdown link targets, images, emphasis
markers, footnote markers and backslash escapes removed, simple inline LaTeX
flattened, subscript digits flattened, quotation marks and square brackets
removed, dashes and spaces unified, whitespace collapsed. A quotation may contain
"[…]" or "[...]" elisions; each fragment between elisions must occur in the
source. A trailing sentence punctuation mark missing from the source is
tolerated. Any <q> or <blockquote> without data-src is reported unless it has
class="nocheck" (for epigraph-style display text that is not a quotation of a
source, which should be rare).

Exits nonzero on any failure.
"""
import html
import os
import re
import sys
from html.parser import HTMLParser


class Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []      # [tag, src, buffer, in_attr_p, line]
        self.quotes = []     # (src, text, line)
        self.untagged = []   # (tag, line)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('q', 'blockquote'):
            if 'data-src' in a:
                self.stack.append([tag, a['data-src'], [], False, self.getpos()[0]])
            elif 'nocheck' not in (a.get('class') or '').split():
                self.untagged.append((tag, self.getpos()[0]))
        elif tag in ('p', 'li', 'br') and self.stack and self.stack[-1][0] == 'blockquote':
            if tag == 'p' and 'attr' in (a.get('class') or '').split():
                self.stack[-1][3] = True
            else:
                self.stack[-1][2].append('\n')

    def handle_endtag(self, tag):
        if self.stack and tag == self.stack[-1][0]:
            t, src, buf, _, line = self.stack.pop()
            self.quotes.append((src, ''.join(buf), line))
            if self.stack:
                self.stack[-1][2].append(''.join(buf))
        elif tag == 'p' and self.stack and self.stack[-1][0] == 'blockquote':
            self.stack[-1][3] = False

    def handle_data(self, data):
        if self.stack and not self.stack[-1][3]:
            self.stack[-1][2].append(data)


QUOTE_CHARS = '"\'“”‘’`«»'


def norm(s):
    s = html.unescape(s)
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)            # html comments
    s = re.sub(r'</?[A-Za-z][A-Za-z0-9]*(?:\s[^<>]*)?/?>', ' ', s)  # html tags (not a bare '<' as in 'X<p')
    s = re.sub(r'\[ref\].*?\[/ref\]', ' ', s, flags=re.S)   # pelican footnotes
    s = re.sub(r'!\[[^\]]*\]\((?:[^()]|\([^()]*\))*\)', ' ', s)  # md images
    s = re.sub(r'\]\((?:[^()]|\([^()]*\))*\)', ']', s)       # md link targets
    s = re.sub(r'\]\[[^\]]*\]', ']', s)                      # md reference links
    s = re.sub(r'\[\^[^\]]*\]', '', s)                       # footnote markers
    s = re.sub(r'\{static\}|\{filename\}', '', s)
    s = s.translate(str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789'))
    s = re.sub(r'\$([^$\n]{1,80})\$', lambda m: re.sub(r'[_{}\\^]', '', m.group(1)), s)
    s = s.replace('\\', '')
    s = s.replace('**', '')
    s = re.sub(r'(?<![A-Za-z0-9])[_*]+|[_*]+(?![A-Za-z0-9])', '', s)  # emphasis markers
    s = re.sub(r'-\n(?=[a-z])', '', s)                       # pdf hyphenation
    for c in QUOTE_CHARS + '[]':
        s = s.replace(c, '')
    for a, b in [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '),
                 (' ', ' '), ('–', '-'), ('—', '-'), ('−', '-'), ('…', '...')]:
        s = s.replace(a, b)
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'([(\[]) ', r'\1', s)                        # space left by a stripped tag
    s = re.sub(r' ([)\],.;:!?])', r'\1', s)
    return s


def fragments(q):
    parts = re.split(r'\[\s*(?:…|\.\.\.)\s*\]', q)
    return [p for p in (norm(x) for x in parts) if p]


def main(paths):
    cache = {}
    total = fails = 0
    for path in paths:
        ex = Extract()
        ex.feed(open(path, encoding='utf-8').read())
        nfile = 0
        for tag, line in ex.untagged:
            print(f'{path}:{line}: UNTAGGED <{tag}> (add data-src or class="nocheck")')
            fails += 1
        for src, q, line in ex.quotes:
            total += 1
            nfile += 1
            if src not in cache:
                if not os.path.exists(src):
                    cache[src] = None
                else:
                    cache[src] = norm(open(src, encoding='utf-8', errors='replace').read())
            text = cache[src]
            if text is None:
                print(f'{path}:{line}: MISSING SOURCE {src}')
                fails += 1
                continue
            for frag in fragments(q):
                if frag in text or frag.rstrip('.,;:!?') in text:
                    continue
                fails += 1
                print(f'{path}:{line}: NOT FOUND in {src}\n    {frag[:300]}\n')
        print(f'{path}: {nfile} quotations')
    print(f'TOTAL: {total} quotations checked; {fails} problems')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
