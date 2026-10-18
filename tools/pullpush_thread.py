#!/usr/bin/env python3
"""Render a Reddit thread from PullPush (api.pullpush.io) archive JSON to text.
Usage: python3 -I tools/pullpush_thread.py SUBMISSION.json COMMENTS.json OUT.txt
The JSON files are fetched separately (curl) from
  /reddit/search/submission/?ids=<id>  and  /reddit/search/comment/?link_id=<id>&size=500
Comments are printed in chronological order with author, score, date and permalink
(scores are as of PullPush's capture, not live). Output is cited as `Path:` in
notes/reception.md Part B so check_note_quotes.py can verify quotations."""
import sys, json, datetime, html

def day(t): return datetime.datetime.fromtimestamp(int(t), datetime.timezone.utc).date()
sub = json.load(open(sys.argv[1]))['data']
com = json.load(open(sys.argv[2]))['data']
out = []
for s in sub:
    out.append(f"Title: {s['title']}\nSubreddit: r/{s['subreddit']}\nAuthor: u/{s['author']}\n"
               f"Posted: {day(s['created_utc'])}\nURL: https://www.reddit.com{s['permalink']}\n"
               f"Link: {s.get('url')}\nSource: PullPush archive (scores as captured)\n")
    if s.get('selftext'):
        out.append(html.unescape(s['selftext']) + '\n')
out.append(f"Comments archived: {len(com)}\n")
for c in sorted(com, key=lambda c: int(c['created_utc'])):
    out.append(f"#### u/{c['author']} · {c.get('score')} points · {day(c['created_utc'])} · "
               f"https://www.reddit.com{c.get('permalink', '')}\n{html.unescape(c.get('body', ''))}\n")
open(sys.argv[3], 'w', encoding='utf-8').write('\n'.join(out))
