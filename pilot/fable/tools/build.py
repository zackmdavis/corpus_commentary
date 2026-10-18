#!/usr/bin/env python3
"""Assemble pilot/fable/index.html from parts/*.html: numbers <fn>...</fn> notes into endnotes,
and strips data-src attributes (kept in parts for quote checking)."""
import re, glob, html, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parts = sorted(glob.glob(os.path.join(root, 'parts', '*.html')))
body = ''.join(open(p, encoding='utf-8').read() for p in parts)
notes = []
def repl(m):
    notes.append(m.group(1).strip())
    n = len(notes)
    return f'<sup class="fnref" id="fnref{n}"><a href="#fn{n}">{n}</a></sup>'
body = re.sub(r'<fn>(.*?)</fn>', repl, body, flags=re.S)
body = re.sub(r'\s+data-src="[^"]*"', '', body)
notes = [re.sub(r'\s+data-src="[^"]*"', '', t) for t in notes]
endnotes = '\n'.join(f'<li id="fn{i}">{t} <a href="#fnref{i}" class="back">&#8617;</a></li>' for i, t in enumerate(notes, 1))
head = open(os.path.join(root, 'templates', 'head.html'), encoding='utf-8').read()
foot = open(os.path.join(root, 'templates', 'foot.html'), encoding='utf-8').read()
out = head + body + '\n<section id="notes"><h2>Notes</h2><ol class="endnotes">\n' + endnotes + '\n</ol></section>\n' + foot
open(os.path.join(root, 'index.html'), 'w', encoding='utf-8').write(out)
words = len(re.sub(r'<[^>]+>', ' ', body).split())
print(f'built index.html: {len(notes)} notes, ~{words} words in body')
