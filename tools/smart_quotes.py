#!/usr/bin/env python3
"""Apply American quotation-mark typography to study pages, in place.
Usage: python3 -I tools/smart_quotes.py study/*.html

Converts straight quotation marks and apostrophes in text (never in tags,
attributes, <head>, <code>, <pre>, <script> or <style>) to curly ones. Inside
an inline quotation (<q>, whose outer marks the stylesheet supplies), the
source's double marks become single and its single marks become double, as
American usage requires for a quotation within a quotation; nested <q>
alternates again. Block quotations keep the source's levels. Curly marks
already present in a source are treated the same way. A converted page is
stamped with <meta name="typography" content="american"> and skipped on later
runs, since converting twice would swap the marks inside <q> back again.
check_study_quotes.py ignores quotation-mark characters, so the conversion
does not affect verification. Run it after build_apparatus.py (which writes
unstamped pages) and after editing a page with straight marks: remove the
stamp from an edited page first, or type curly marks by hand.
"""
import re, sys

SKIP = {'head', 'code', 'pre', 'script', 'style'}
BLOCK = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'div',
         'td', 'th', 'section', 'br', 'dd', 'dt', 'ul', 'ol', 'nav', 'body'}
OPENERS = set(' \t\n([{—–-/ “‘')
TOKEN = re.compile(r'(<!--.*?-->|<[^>]+>)', re.S)


def convert(html):
    """Marks alternate double/single by nesting level, whatever the source
    used: level 0 is double, level 1 single, and so on. An open <q> counts as
    a level, since the stylesheet supplies its marks."""
    out, skip = [], 0
    prev = ' '
    stack = []  # open levels in the current block: 'q' for <q>, else 'd'/'s'
    parts = TOKEN.split(html)
    for i, part in enumerate(parts):
        if i % 2:  # tag or comment
            m = re.match(r'<\s*(/?)\s*([A-Za-z0-9]+)', part)
            if m:
                closing, name = m.group(1) == '/', m.group(2).lower()
                if name in SKIP:
                    skip = max(skip + (-1 if closing else 1), 0)
                elif name == 'q':
                    if closing:
                        while stack and stack[-1] != 'q':
                            stack.pop()
                        if stack:
                            stack.pop()
                        prev = '”'
                    else:
                        stack.append('q')
                        prev = '“'
                elif name in BLOCK:
                    prev = ' '
                    stack = [x for x in stack if x == 'q']
            out.append(part)
            continue
        if skip:
            out.append(part)
            continue
        res = []
        for j, c in enumerate(part):
            nxt = part[j + 1] if j + 1 < len(part) else (parts[i + 2][:1] if i + 2 < len(parts) else ' ')
            kind = None
            if c in '"“”':
                kind = 'd'
                opening = c == '“' or (c == '"' and prev in OPENERS)
            elif c in "'‘’":
                if prev.isalnum() and nxt.isalnum():
                    c = '’'                                   # contraction
                elif c == '‘' or (c == "'" and prev in OPENERS and not nxt.isdigit()):
                    kind, opening = 's', True
                elif stack and stack[-1] == 's':
                    kind, opening = 's', False
                else:
                    c = '’'                                   # apostrophe, elision
            if kind:
                if opening:
                    c = '“' if len(stack) % 2 == 0 else '‘'
                    stack.append(kind)
                else:
                    if stack and stack[-1] != 'q':
                        stack.pop()
                    c = '”' if len(stack) % 2 == 0 else '’'
            res.append(c)
            prev = c
        out.append(''.join(res))
    return ''.join(out)


if __name__ == '__main__':
    STAMP = '<meta name="typography" content="american">'
    for path in sys.argv[1:]:
        s = open(path, encoding='utf-8').read()
        if STAMP in s:
            continue
        t = convert(s).replace('</head>', STAMP + '\n</head>', 1)
        if t != s:
            open(path, 'w', encoding='utf-8').write(t)
            print('converted', path)
