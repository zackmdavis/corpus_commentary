#!/usr/bin/env python3
"""Report quotations in the study whose italics differ from the source's.

Usage (from the project root):
    python3 -I tools/check_study_emphasis.py [--bold] study/*.html

check_study_quotes.py strips emphasis markers before comparing, so a quotation
that drops (or adds) italics passes it. This script compares italics. For each
<q data-src> / <blockquote data-src> whose source is a Markdown file, the
quotation's words are located in the source, and each whitespace-delimited
chunk's italics in the study (any part inside <i> or <em>) are compared with
its italics in the source (any part inside _..._, *...*, <i> or <em>).

Boldface is not compared: the corpus uses it for the highlighted sentences of
a post's summary list, for labels such as "Followup to", and for highlighting
in quoted correspondence, and the study does not reproduce it. Pass --bold to
list the quotations whose source words are in boldface.

Sources that are plain-text extractions (research/*/text.txt,
reception_data/web/*/text.txt) carry no emphasis and are skipped. A quotation
whose words cannot be located is reported as UNLOCATED; run
check_study_quotes.py for those.

Exits nonzero if any difference is found.
"""
import html
import os
import re
import sys
from html.parser import HTMLParser

MARK = '\x01'   # appended to each chunk inside italics
BOLD = '\x02'   # appended to each chunk inside boldface
ITALIC_TAGS = {'i', 'em'}
ELISION = re.compile(r'\[\s*(?:…|\.\.\.)\s*\]')


class Extract(HTMLParser):
    """Collect (src, marked_text, line) for each tagged quotation.

    marked_text is the quotation's text with MARK appended to every
    whitespace-delimited run that lies inside <i> or <em>.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []      # [tag, src, pieces, in_attr_p, line, italic_depth]
        self.quotes = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('q', 'blockquote') and 'data-src' in a:
            self.stack.append([tag, a['data-src'], [], False, self.getpos()[0], 0])
        elif self.stack:
            top = self.stack[-1]
            if tag in ITALIC_TAGS:
                top[5] += 1
            elif tag == 'p' and 'attr' in (a.get('class') or '').split():
                top[3] = True
            elif tag in ('p', 'li', 'br'):
                top[2].append(' ')

    def handle_endtag(self, tag):
        if not self.stack:
            return
        top = self.stack[-1]
        if tag == top[0]:
            self.stack.pop()
            self.quotes.append((top[1], ''.join(top[2]), top[4]))
        elif tag in ITALIC_TAGS:
            top[5] = max(0, top[5] - 1)
        elif tag == 'p':
            top[3] = False

    def handle_data(self, data):
        if self.stack and not self.stack[-1][3]:
            if self.stack[-1][5] > 0:
                data = re.sub(r'(\S+)', lambda w: w.group(1) + MARK, data)
            self.stack[-1][2].append(data)


def words(text):
    """Lowercased alphanumeric words of a string (apostrophes dropped)."""
    text = text.translate(str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789'))
    text = re.sub(r"['’‘`]", '', text)
    return re.findall(r'[0-9A-Za-zÀ-ÿ]+', text.lower())


def mark_span(m, mark=MARK):
    return re.sub(r'(\S+)', lambda w: w.group(1) + mark, m.group(2))


def tokens(marked):
    """[(word, italic, bold)] for a marked string, flags taken per chunk."""
    toks = []
    for chunk in marked.split():
        italic = MARK in chunk
        bold = BOLD in chunk
        for w in words(chunk.replace(MARK, '').replace(BOLD, '')):
            toks.append((w, italic, bold))
    return toks


def source_tokens(raw):
    s = html.unescape(raw)
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'\[ref\].*?\[/ref\]', ' ', s, flags=re.S)
    s = re.sub(r'!\[[^\]]*\]\((?:[^()]|\([^()]*\))*\)', ' ', s)
    s = re.sub(r'\]\((?:[^()]|\([^()]*\))*\)', ']', s)
    s = re.sub(r'\]\[[^\]]*\]', ']', s)
    s = re.sub(r'\[\^[^\]]*\]', '', s)
    s = s.replace('\\', '')
    s = re.sub(r'<(em|i)>(.*?)</\1>', mark_span, s, flags=re.S | re.I)
    s = re.sub(r'<(b|strong)>(.*?)</\1>', lambda m: mark_span(m, BOLD), s,
               flags=re.S | re.I)
    s = re.sub(r'</?[A-Za-z][A-Za-z0-9]*(?:\s[^<>]*)?/?>', ' ', s)
    out = []
    for para in re.split(r'\n\s*\n', s):
        para = re.sub(r'(\*\*|__)(?=\S)(.+?)(?<=\S)\1', lambda m: mark_span(m, BOLD),
                      para, flags=re.S)
        para = re.sub(r'(?<![A-Za-z0-9])([_*])(?=\S)(.+?)(?<=\S)\1(?![A-Za-z0-9])',
                      mark_span, para, flags=re.S)
        out.append(para)
    return tokens('\n\n'.join(out))


def quote_fragments(marked):
    """Token lists for the parts of a quotation between [...] elisions."""
    return [f for f in (tokens(part) for part in ELISION.split(marked)) if f]


def find(needle, hay_words):
    n = len(needle)
    first = needle[0]
    for i in range(len(hay_words) - n + 1):
        if hay_words[i] == first and hay_words[i:i + n] == needle:
            yield i


def best_match(frag, toks, hay):
    """Index of the occurrence of frag in the source that differs least in
    italics, or None if the words do not occur."""
    needle = [t[0] for t in frag]
    best = None
    for i in find(needle, hay):
        d = sum(1 for k in range(len(frag)) if toks[i + k][1] != frag[k][1])
        if best is None or d < best[1]:
            best = (i, d)
    return None if best is None else best[0]


def load_source(src, cache):
    if src not in cache:
        toks = source_tokens(open(src, encoding='utf-8', errors='replace').read())
        cache[src] = (toks, [t[0] for t in toks])
    return cache[src]


def main(args):
    show_bold = '--bold' in args
    paths = [p for p in args if p != '--bold']
    cache = {}
    diffs = unlocated = checked = 0
    for path in paths:
        ex = Extract()
        ex.feed(open(path, encoding='utf-8').read())
        for src, marked, line in ex.quotes:
            if not src.endswith('.md') or not os.path.exists(src):
                continue
            toks, hay = load_source(src, cache)
            for frag in quote_fragments(marked):
                checked += 1
                needle = [t[0] for t in frag]
                i = best_match(frag, toks, hay)
                if i is None:
                    unlocated += 1
                    print(f'{path}:{line}: UNLOCATED in {src}: {" ".join(needle[:12])}')
                    continue
                if show_bold:
                    bold = [toks[i + k][0] for k in range(len(frag)) if toks[i + k][2]]
                    if bold:
                        print(f'{path}:{line}: {src}\n    source boldface: '
                              f'{" ".join(bold[:20])}')
                dropped = [frag[k][0] for k in range(len(frag))
                           if toks[i + k][1] and not frag[k][1]]
                added = [frag[k][0] for k in range(len(frag))
                         if frag[k][1] and not toks[i + k][1]]
                if dropped or added:
                    diffs += 1
                    msg = []
                    if dropped:
                        msg.append('source italicizes, study does not: ' + ' '.join(dropped))
                    if added:
                        msg.append('study italicizes, source does not: ' + ' '.join(added))
                    print(f'{path}:{line}: {src}\n    quote: {" ".join(needle[:14])}'
                          f'{" …" if len(needle) > 14 else ""}\n    ' + '\n    '.join(msg))
    print(f'TOTAL: {checked} fragments checked; {diffs} with differences in italics; '
          f'{unlocated} unlocated')
    return 1 if diffs or unlocated else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
