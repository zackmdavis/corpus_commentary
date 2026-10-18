#!/usr/bin/env python3
"""Render a saved GreaterWrong post page (HTML) into the same quote-checkable Markdown
thread format as tools/render_lw_threads.py. Used where the LessWrong GraphQL dump
missed comments (e.g. answers on question posts).

Includes both the answers section (if any) and the comments section, in document
(tree) order. Comment heading format:
    #### [>>] author · N karma · YYYY-MM-DD · https://www.lesswrong.com/posts/<id>/<slug>?commentId=<cid>
Bodies are converted from GreaterWrong's HTML to GitHub-flavored Markdown with pandoc.
Usage: python3 -I tools/render_gw_thread.py PAGE.html OUT.md "Title" LW_URL FETCH_DATE"""
import sys, re, html, subprocess, datetime
from html.parser import HTMLParser

page, out_path, title, lw_url, fetched = sys.argv[1:6]
s = open(page, encoding='utf-8').read()

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []      # tag stack of (tag, is_comment_li)
        self.comments = []   # dicts
        self.cur = None      # comment being filled
        self.cap = None      # 'author' | 'date' | 'karma' | ('body', depth)
        self.body_depth = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '') or ''
        is_c = tag == 'li' and 'comment-item' in cls and (a.get('id') or '').startswith('comment-')
        if is_c:
            depth = sum(1 for t, c in self.stack if c)
            self.cur = {'id': a['id'][8:], 'depth': depth, 'author': '', 'date': '', 'karma': '', 'body': ''}
            self.comments.append(self.cur)
        if self.cap == 'body':
            self.body_depth += 1 if tag not in ('br', 'img', 'hr', 'input') else 0
            self.cur['body'] += self.get_starttag_text()
        elif self.cur is not None and not self.cur['body']:
            if tag == 'a' and 'author' in cls.split() and not self.cur['author']:
                self.cap = 'author'
            elif tag == 'a' and cls == 'date' and not self.cur['date']:
                self.cap = 'date'
            elif tag == 'span' and cls == 'karma-value' and not self.cur['karma']:
                self.cap = 'karma'
            elif tag == 'div' and 'comment-body' in cls.split():
                self.cap = 'body'; self.body_depth = 1
        if tag not in ('br', 'img', 'hr', 'input', 'meta', 'link'):
            self.stack.append((tag, is_c))
    def handle_endtag(self, tag):
        if self.cap == 'body':
            self.body_depth -= 1
            if self.body_depth == 0:
                self.cap = None
            else:
                self.cur['body'] += f'</{tag}>'
        elif self.cap in ('author', 'date', 'karma') and tag in ('a', 'span'):
            self.cap = None
        # pop to matching tag
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
    def handle_data(self, d):
        if self.cap == 'body': self.cur['body'] += html.escape(html.unescape(d), quote=False)
        elif self.cap in ('author', 'date', 'karma'): self.cur[self.cap] += html.unescape(d)
    def handle_entityref(self, name): self.handle_data(f'&{name};')
    def handle_charref(self, name): self.handle_data(f'&#{name};')

p = P(); p.feed(s)
out = [f'Title: {title}', f'LessWrong-URL: {lw_url}',
       f'Fetched: {fetched} (GreaterWrong HTML; rendered by tools/render_gw_thread.py)',
       f'Comments: {len(p.comments)} (answers and comments, as rendered by GreaterWrong)', '']
for c in p.comments:
    m = re.search(r'\d{1,2} \w{3} \d{4} \d{1,2}:\d{2} UTC', c['date'])
    d = datetime.datetime.strptime(m.group(0), '%d %b %Y %H:%M UTC').strftime('%Y-%m-%d') if m else c['date'].strip()
    k = re.match(r'\s*(-?\d+)', c['karma']); k = k.group(1) if k else '?'
    md = subprocess.run(['pandoc', '-f', 'html', '-t', 'gfm', '--wrap=none'], input=c['body'],
                        capture_output=True, text=True).stdout.strip()
    tag = ' [AUTHOR]' if c['author'].strip().lower() == 'zack_m_davis' else ''
    out.append(f"#### [{'>' * c['depth'] or '-'}] {c['author'].strip()}{tag} · {k} karma · {d} · {lw_url}?commentId={c['id']}")
    out.append(md or '[empty or deleted comment]'); out.append('')
open(out_path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'{len(p.comments)} comments -> {out_path}')
