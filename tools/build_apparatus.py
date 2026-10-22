#!/usr/bin/env python3
"""Build the study's thematic index and bibliography from its own citations.

Usage (from the project root):
    python3 -I tools/build_apparatus.py

Reads study/00-*.html ... study/12-*.html. A chapter section "cites" a work of
Davis's if the section links to it (blog post, hidden page, LessWrong post,
or pinned Gitweb draft link) or quotes it (a data-src path into AAL_content/,
UUT_content/ or LW_content/). LessWrong cross-posts are folded into the blog
post they duplicate, using the Match column of notes/lw-dedupe.md. Comment
links (#isso-, ?commentId=) are not counted as citing the post.

Writes study/b-thematic-index.html (works of Davis's by chapter section) and
study/c-bibliography.html (Davis's works by kind, then the other works and
reception listed in the chapters' works-cited sections, deduplicated).
"""
import glob
import html
import os
import sys
import re
from html.parser import HTMLParser

MON = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
CHAPTERS = sorted(glob.glob('study/0*.html') + glob.glob('study/1*.html'))


def header(path, key):
    t = open(path, encoding='utf-8').read(4000)
    m = re.search(rf'^{key}:\s*(.+)$', t, re.M)
    return m.group(1).strip() if m else None


def md_title(s):
    s = s.replace('"', "'")
    s = html.escape(s, quote=False)
    s = re.sub(r'&lt;(/?)em&gt;', r'<\1i>', s)
    s = re.sub(r'(?<![\w*])[_*]([^_*]+)[_*](?![\w*])', r'<i>\1</i>', s)
    return s


# --- LessWrong ids -> local file ------------------------------------------
lw_file = {}
for f in glob.glob('LW_content/*/*.md'):
    u = header(f, 'LessWrong-URL')
    if u:
        m = re.search(r'/posts/([A-Za-z0-9]+)', u)
        if m:
            lw_file[m.group(1)] = f
for line in open('notes/lw-dedupe.md', encoding='utf-8'):
    cells = [c.strip() for c in line.split('|')]
    if len(cells) < 7 or not cells[5].startswith('http'):
        continue
    m = re.search(r'/posts/([A-Za-z0-9]+)', cells[5])
    match = cells[6]
    if not m or not match:
        continue
    target = None
    if re.match(r'(AAL|UUT)_content/', match):
        target = match
    else:
        mm = re.match(r'https?://zackmdavis\.net/blog/(\d{4})/\d\d/([^/]+)/', match)
        if mm and os.path.exists(f'AAL_content/{mm.group(1)}/{mm.group(2)}.md'):
            target = f'AAL_content/{mm.group(1)}/{mm.group(2)}.md'
        mm = re.match(r'https?://unremediatedgender\.space/(\d{4})/[A-Z][a-z]{2}/([^/]+)/', match)
        if mm and os.path.exists(f'UUT_content/{mm.group(1)}/{mm.group(2)}.md'):
            target = f'UUT_content/{mm.group(1)}/{mm.group(2)}.md'
    if target and os.path.exists(target) and m.group(1) not in lw_file:
        lw_file[m.group(1)] = target

# Draft links as the study pins them (file -> URL).
draft_url = {}
for ch in CHAPTERS:
    for u in re.findall(r'href="([^"]+)"', open(ch, encoding='utf-8').read()):
        u = html.unescape(u)
        if 'source?p=' in u and 'f=content/drafts/' in u and 'hb=' in u:
            root = 'AAL_content' if 'An_Algorithmic_Lucidity' in u else 'UUT_content'
            f = re.search(r'f=content/drafts/([^;&]+)', u).group(1)
            draft_url.setdefault(f'{root}/drafts/{f}', u)


def file_for_link(u):
    u = html.unescape(u)
    if '#isso' in u or 'commentId=' in u:
        return None
    m = re.match(r'https?://(zackmdavis\.net/blog|unremediatedgender\.space)/(\d{4})/([A-Z][a-z]{2})/([^/#]+)/', u)
    if m:
        root = 'AAL_content' if m.group(1).startswith('zack') else 'UUT_content'
        p = f'{root}/{m.group(2)}/{m.group(4)}.md'
        return p if os.path.exists(p) else None
    m = re.match(r'https?://unremediatedgender\.space/ancillary/(.+?)/?(?:#.*)?$', u)
    if m:
        p = f'UUT_content/pages/ancillary/{m.group(1)}.md'
        return p if os.path.exists(p) else None
    m = re.match(r'https?://www\.lesswrong\.com/posts/([A-Za-z0-9]+)', u)
    if m:
        return lw_file.get(m.group(1))
    if 'source?p=' in u and 'f=content/drafts/' in u:
        root = 'AAL_content' if 'An_Algorithmic_Lucidity' in u else 'UUT_content'
        p = f"{root}/drafts/{re.search(r'f=content/drafts/([^;&]+)', u).group(1)}"
        return p if os.path.exists(p) else None
    return None


def file_for_src(s):
    if not re.match(r'(AAL|UUT|LW)_content/', s) or not os.path.exists(s):
        return None
    if s.startswith('LW_content/'):
        u = header(s, 'LessWrong-URL')
        m = re.search(r'/posts/([A-Za-z0-9]+)', u or '')
        return lw_file.get(m.group(1), s) if m else s
    return s


def kind(p):
    if '/drafts/' in p:
        return 'draft'
    if '/pages/' in p:
        return 'page'
    return {'AAL_content': 'AAL', 'UUT_content': 'UUT', 'LW_content': 'LW'}[p.split('/')[0]]


def info(p):
    """(sort date, display date, title html, url) for a corpus file."""
    title = md_title(header(p, 'Title') or os.path.basename(p)[:-3])
    d = header(p, 'Date') or ''
    m = re.match(r'(\d{4})-(\d\d)-(\d\d)', d)
    disp = f'{int(m.group(3))} {MON[int(m.group(2)) - 1]} {m.group(1)}' if m else ''
    k = kind(p)
    if k in ('AAL', 'UUT'):
        y, mo = m.group(1), MON[int(m.group(2)) - 1]
        stem = os.path.basename(p)[:-3]
        url = (f'https://zackmdavis.net/blog/{y}/{mo}/{stem}/' if k == 'AAL'
               else f'http://unremediatedgender.space/{y}/{mo}/{stem}/')
    elif k == 'LW':
        url = header(p, 'LessWrong-URL')
    elif k == 'page':
        rel = p[len('UUT_content/pages/ancillary/'):-3] if '/ancillary/' in p else None
        url = f'http://unremediatedgender.space/ancillary/{rel}/' if rel else None
    else:
        url = draft_url.get(p)
    return (d[:10] or '9999', disp, title, url)


# --- Parse chapters into sections -------------------------------------------
class Sec(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.secs, self.cur, self.in_h1, self.h1, self.in_h2, self.stop = [], None, False, '', False, False
        self.h1_chapno = ''
        self.in_chapno = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'section' and a.get('class') in ('notes', 'works-cited', 'works'):
            self.stop = True
        if self.stop:
            return
        if tag == 'h1':
            self.in_h1 = True
        if tag == 'span' and a.get('class') == 'chapno' and self.in_h1:
            self.in_chapno = True
        if tag == 'h2' and a.get('id'):
            self.cur = {'id': a['id'], 'title': '', 'works': set()}
            self.secs.append(self.cur)
            self.in_h2 = True
        if self.cur is not None:
            for key in ('href', 'data-src'):
                if a.get(key):
                    f = file_for_link(a[key]) if key == 'href' else file_for_src(a[key])
                    if f:
                        self.cur['works'].add(f)

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_h1 = False
        if tag == 'span':
            self.in_chapno = False
        if tag == 'h2':
            self.in_h2 = False

    def handle_data(self, data):
        if self.in_chapno:
            self.h1_chapno += data
        elif self.in_h1:
            self.h1 += data
        if self.in_h2 and self.cur is not None:
            self.cur['title'] += data


chapters = []
for ch in CHAPTERS:
    p = Sec()
    p.feed(open(ch, encoding='utf-8').read())
    chapters.append({'file': os.path.basename(ch), 'label': p.h1_chapno.strip(),
                     'title': p.h1.strip(), 'secs': p.secs})


def short(label):
    return label.replace('Chapter ', 'Ch. ')


cited_in = {}
for c in chapters:
    for s in c['secs']:
        for w in s['works']:
            cited_in.setdefault(w, set()).add(c['file'])
order = {c['file']: i for i, c in enumerate(chapters)}
label_of = {c['file']: short(c['label']) for c in chapters}
BLOG = {'AAL': 'AAL', 'UUT': 'UUT', 'LW': 'LW', 'page': 'UUT, hidden page', 'draft': 'unpublished draft'}


def entry(w, with_chapters=True):
    d, disp, title, url = info(w)
    k = kind(w)
    if title.endswith("'"):  # comma inside the closing quotation mark
        title = title[:-1] + ",'"
        comma = ''
    else:
        comma = ','
    t = f'<a href="{html.escape(url)}">{title}</a>' if url else title
    where = BLOG[k]
    if k == 'draft':
        repo = 'AAL' if w.startswith('AAL') else 'UUT'
        where = f'unpublished {repo} draft, <span class="path">content/drafts/{html.escape(os.path.basename(w))}</span>'
    s = f'"{t}{comma}" {where}' + (f', {disp}' if disp and k != 'draft' else '')
    if with_chapters:
        chs = sorted(cited_in.get(w, ()), key=order.get)
        s += '. <span class="muted">' + ', '.join(f'<a href="{c}">{label_of[c]}</a>' for c in chs) + '</span>'
    return s


HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="bookbar"><a href="index.html">Contents</a>{nav}</nav>

<h1><span class="chapno">{label}</span>{title}</h1>
'''
TAIL = '''
<nav class="bookbar"><a href="index.html">Contents</a>{nav}</nav>
</body>
</html>
'''

# --- Thematic index ---------------------------------------------------------
out = [HEAD.format(title='Thematic Index of Posts', label='Apparatus B',
                   nav='<a href="a-chronology.html">← Chronology</a><a href="c-bibliography.html">Bibliography →</a>')]
out.append('<p class="lede">Davis\'s posts, hidden pages and drafts, arranged by the section of the study in which each is quoted or discussed. A work discussed in several places is listed under each. The bibliography lists the same works by kind and date. Drafts are listed by their path in the blog\'s public repository; the chapters link each to a fixed version.</p>\n')
for c in chapters:
    secs = [s for s in c['secs'] if s['works']]
    if not secs:
        continue
    out.append(f'<h2><a href="{c["file"]}">{c["label"]}: {c["title"]}</a></h2>')
    for s in secs:
        out.append(f'<h3><a href="{c["file"]}#{s["id"]}">{html.escape(s["title"])}</a></h3>\n<ul class="index">')
        for w in sorted(s['works'], key=lambda w: (info(w)[0], w)):
            out.append(f'<li>{entry(w, with_chapters=False)}</li>')
        out.append('</ul>')
out.append(TAIL.format(nav='<a href="a-chronology.html">← Chronology</a><a href="c-bibliography.html">Bibliography →</a>'))
open('study/b-thematic-index.html', 'w', encoding='utf-8').write('\n'.join(out))

# --- Bibliography -----------------------------------------------------------
out = [HEAD.format(title='Bibliography', label='Apparatus C',
                   nav='<a href="b-thematic-index.html">← Thematic Index</a><a href="d-questions.html">Questions →</a>')]
out.append('<p class="lede">Part I lists every work of Davis\'s quoted or discussed in the study, with the chapters that cite it. Parts II and III gather the other sources and the reception from the chapters\' lists of works cited. Posts that appeared both on a blog and on LessWrong are listed under the blog.</p>\n')
out.append('<h2 id="davis">I. Works by Davis</h2>')
groups = [('AAL', '<i>An Algorithmic Lucidity</i> (zackmdavis.net/blog)'),
          ('UUT', '<i>The Scintillating But Ultimately Untrue Thought</i> (unremediatedgender.space)'),
          ('LW', 'LessWrong only'),
          ('page', 'Hidden pages (<i>The Scintillating But Ultimately Untrue Thought</i>)'),
          ('draft', 'Unpublished drafts in the blogs\' public repositories')]
for k, name in groups:
    ws = sorted((w for w in cited_in if kind(w) == k),
                key=(lambda w: re.sub(r'\W', '', info(w)[2]).lower()) if k == 'draft'
                else (lambda w: (info(w)[0], info(w)[2], w)))
    if not ws:
        continue
    out.append(f'<h3>{name}</h3>\n<ul class="bib">')
    for w in ws:
        out.append(f'<li>{entry(w)}</li>')
    out.append('</ul>')


class WC(HTMLParser):
    """Collect (h3 heading, li inner html) from a works-cited section."""
    def __init__(self, raw):
        super().__init__(convert_charrefs=False)
        self.raw, self.items, self.h3, self.in_wc, self.in_h3 = raw, [], '', False, False

    def handle_starttag(self, tag, attrs):
        if tag == 'section' and dict(attrs).get('class') == 'works-cited':
            self.in_wc = True
        if self.in_wc and tag == 'h3':
            self.in_h3, self.h3 = True, ''

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False

    def handle_data(self, d):
        if self.in_h3:
            self.h3 += d


def works_cited_items(path):
    raw = open(path, encoding='utf-8').read()
    m = re.search(r'<section class="works(?:-cited)?"[^>]*>(.*?)</section>', raw, re.S)
    if not m:
        return []
    res, h3 = [], ''
    for tok in re.finditer(r'<h3>(.*?)</h3>|<li>(.*?)</li>', m.group(1), re.S):
        if tok.group(1) is not None:
            h3 = re.sub('<[^>]+>', '', tok.group(1))
        else:
            res.append((h3, tok.group(2).strip()))
    return res


def plain(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', s))).strip()


other, reception, secondhand = {}, {}, {}
for c in chapters:
    for h3, li in works_cited_items('study/' + c['file']):
        if re.match(r'(Davis|Corpus)', h3):
            continue
        hrefs = [u for u in re.findall(r'href="([^"]+)"', li) if 'web.archive.org' not in u]
        if hrefs and file_for_link(hrefs[0]):
            continue  # a work of Davis's, listed in Part I
        if plain(li).startswith('All other works are cited'):
            continue  # a note addressed to the chapter's own reader
        threads = 'on the posts above' in li
        li = li.replace('on the posts above', "on Davis's posts cited in the chapter")
        bucket = reception if threads or re.search(r'reception|comment', h3, re.I) else other
        if re.match(r'(From memory|Cited as|Yudkowsky[\'’]s Facebook posts)', plain(li)):
            bucket = secondhand
        key = (c['file'] if threads else '') + (hrefs[0] if hrefs else plain(li).lower()[:80])
        e = bucket.setdefault(key, {'li': li, 'chs': set()})
        e['chs'].add(c['file'])
        if len(li) > len(e['li']):
            e['li'] = li


def sortkey(e):
    s = re.sub(r'^[^A-Za-z0-9]+', '', re.sub(r'["\'‘’“”]', '', plain(e['li'])))
    head = s.split(',')[0].replace(' et al.', '').strip()
    head = re.split(r' and | & ', head)[0].replace(' Jr.', '')
    words = head.split()
    if 1 < len(words) <= 4 and not s.startswith(('"', "'")) and all(w[:1].isupper() for w in words):
        head = ' '.join(words[-2:]) if words[-2] in ('Del', 'van', 'von', 'de') else words[-1]
    return (head + ' ' + s).lower(), e['li']


for name, bucket, hid in (('II. Other works', other, 'other'),
                          ('Cited from memory or at second hand', secondhand, 'secondhand'),
                          ('III. Reception and comment threads', reception, 'reception')):
    tag = 'h3' if hid == 'secondhand' else 'h2'
    out.append(f'<{tag} id="{hid}">{name}</{tag}>\n<ul class="bib">')
    for e in sorted(bucket.values(), key=sortkey):
        chs = sorted(e['chs'], key=order.get)
        out.append(f'<li>{e["li"]} <span class="muted">' +
                   ', '.join(f'<a href="{c}">{label_of[c]}</a>' for c in chs) + '</span></li>')
    out.append('</ul>')
out.append(TAIL.format(nav='<a href="b-thematic-index.html">← Thematic Index</a><a href="d-questions.html">Questions →</a>'))
open('study/c-bibliography.html', 'w', encoding='utf-8').write('\n'.join(out))

# American quotation-mark typography on the pages just written (see tools/smart_quotes.py)
import subprocess
subprocess.run([sys.executable, '-I', 'tools/smart_quotes.py', 'study/b-thematic-index.html', 'study/c-bibliography.html'], check=True)

n_davis = len(cited_in)
print(f'thematic index and bibliography written: {n_davis} works by Davis; '
      f'{len(other)} other works; {len(reception)} reception entries')
