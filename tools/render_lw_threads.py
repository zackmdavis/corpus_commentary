#!/usr/bin/env python3
"""Render reception_data/lw_comments/*.json (raw LessWrong GraphQL comment dumps) into
readable, quote-checkable Markdown threads in reception_data/lw_threads/*.md.

Each output file starts with a header block (Title, LessWrong-URL, Fetched, Comments)
and lists comments in thread order (parents before children, siblings by date).
Each comment heading gives depth marker, author, karma, date, and permalink:
    #### [>>] gjm · 2 karma · 2019-03-12 · https://www.lesswrong.com/posts/<post>/<slug>?commentId=<id>
The author is shown by the display name the website shows (the API's username is an immutable
key that can differ, e.g. username Yvain, display name Scott Alexander). Cite the display name.
followed by the comment body (LessWrong's markdown export, unedited). Davis's own
comments are marked [AUTHOR]. Deleted/empty comments are shown as such.
Usage: python3 -I tools/render_lw_threads.py"""
import json, glob, os, collections
SRC, DST = 'reception_data/lw_comments', 'reception_data/lw_threads'
os.makedirs(DST, exist_ok=True)
DAVIS = {'zack_m_davis', 'zack_m_davis'.lower(), 'Zack_M_Davis'}
n_files = n_comments = 0
for f in sorted(glob.glob(f'{SRC}/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    post, cs = d['post'], d['comments']
    kids = collections.defaultdict(list)
    ids = {c['_id'] for c in cs}
    for c in cs:
        parent = c.get('parentCommentId')
        kids[parent if parent in ids else None].append(c)
    for v in kids.values(): v.sort(key=lambda c: c.get('postedAt') or '')
    out = [f"Title: {post['title']}", f"LessWrong-URL: {post['pageUrl']}", f"Posted: {post['postedAt'][:10]}",
           f"Fetched: {d['fetched']} (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)",
           f"Comments: {len(cs)} (commentCount field: {post.get('commentCount')})", '']
    def walk(parent, depth):
        for c in kids.get(parent, []):
            user = c.get('user') or {}
            u = user.get('username') or '[deleted user]'
            dn = user.get('displayName') or u
            tag = ' [AUTHOR]' if u.lower() == 'zack_m_davis' else ''
            body = ((c.get('contents') or {}).get('markdown') or '').strip() or '[empty or deleted comment]'
            out.append(f"#### [{'>' * depth or '-'}] {dn}{tag} · {c.get('baseScore')} karma · {(c.get('postedAt') or '')[:10]} · {post['pageUrl']}?commentId={c['_id']}")
            out.append(body); out.append('')
            walk(c['_id'], depth + 1)
    walk(None, 0)
    open(f"{DST}/{os.path.basename(f)[:-5]}.md", 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    n_files += 1; n_comments += len(cs)
print(f'rendered {n_files} threads, {n_comments} comments -> {DST}/')
