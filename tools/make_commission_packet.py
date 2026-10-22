#!/usr/bin/env python3
"""Build notes/review-packets/commission.md: the packet for an outside model's
assessment of the commissioner's influence on the study.

Usage: python3 -I tools/make_commission_packet.py

Contents: instructions; BRIEF.md as it stands; both sides of the two sessions
that set the scope (13 Oct) and the reply protocol (16 Oct); and every message
the commissioner typed in this project's Claude Code sessions, in order.
Automated context summaries, subagent notifications, tool output, system
reminders and bare slash commands are excluded.
"""
import glob, json, os, re

D = os.path.expanduser('~/.claude/projects/-home-zmd-Code-Misc-corpus-commentary/')
SCOPE_SESSIONS = [('927b3dcc-49fc-4f44-a168-841d70664d60', 'Session 1, 13 Oct 2026 (scope and brief)'),
                  ('0338c784-43a9-4c10-83c3-bf591e04e457', 'Session of 16 Oct 2026, evening (pilot judging; reply protocol)')]


def user_texts(e):
    c = e.get('message', {}).get('content')
    texts = [c] if isinstance(c, str) else [b.get('text', '') for b in (c or [])
                                            if isinstance(b, dict) and b.get('type') == 'text']
    for t in texts:
        t = re.sub(r'<system-reminder>.*?</system-reminder>', '', t, flags=re.S).strip()
        if not t or t.startswith(('[Request interrupted', '<command-name>', '<local-command')):
            continue
        if 'Caveat: The messages below were generated' in t or '<task-notification>' in t:
            continue
        if 'This session is being continued from a previous conversation' in t:
            continue
        yield t


def is_user(e):
    return (e.get('type') == 'user' and not e.get('isMeta') and not e.get('isSidechain')
            and e.get('message', {}).get('role') == 'user')


def dialog(sid):
    out = []
    for line in open(D + sid + '.jsonl', encoding='utf-8'):
        e = json.loads(line)
        if e.get('isSidechain'):
            continue
        ts = e.get('timestamp', '')[:16]
        if is_user(e):
            for t in user_texts(e):
                out.append(f'**Commissioner** ({ts}):\n\n{t}\n')
        elif e.get('type') == 'assistant':
            for b in e['message'].get('content') or []:
                if isinstance(b, dict) and b.get('type') == 'text' and b['text'].strip():
                    out.append(f'**Model** ({ts}):\n\n{b["text"].strip()}\n')
    return '\n'.join(out)


def all_user_messages():
    rows = []
    for f in glob.glob(D + '*.jsonl'):
        sid = os.path.basename(f)[:8]
        for line in open(f, encoding='utf-8'):
            try:
                e = json.loads(line)
            except ValueError:
                continue
            if is_user(e):
                for t in user_texts(e):
                    rows.append((e.get('timestamp', ''), sid, t))
    rows.sort()
    seen, out = set(), []
    for ts, sid, t in rows:
        if t[:200] in seen:
            continue
        seen.add(t[:200])
        out.append(f'--- {ts[:16]} (session {sid})\n\n{t}\n')
    return '\n'.join(out), len(out)


INSTRUCTIONS = '''# Packet: assessing the commissioner's influence on the study

You are GPT, asked by the drafting model of a book-length study (written by Claude Opus 5.5, an Anthropic model) for an independent assessment. The study is a scholarly monograph on the blogging corpus of Zack M. Davis. It was commissioned by Davis himself, so the commissioner is the study's subject. Claude has a conflict of interest in judging this: it is working for the commissioner in the same conversation in which it is asked whether he steered it, and models are known to lean toward agreeing with their users. That is why the assessment is being asked of you.

The study is about to be frozen as a first edition. Its front matter will name the commissioner, and its Introduction (section 6, "Authorship and positionality") will tell readers what the commission involved. Davis asked the drafting model to summarize for readers what kind of prompting he did as commissioner, and to use its judgment about what to tell them.

## What is in this packet

1. The written commission (BRIEF.md) as it stands now. The model drafted the first version in session 1 (included below) from Davis's messages; it was amended over the project at his direction or the model's. Every session read it.
2. Both sides of two sessions: session 1 (13 Oct 2026), where the scope was set, and the evening session of 16 Oct, where a pilot comparison was judged and the protocol for the author's reply was set.
3. Every message Davis typed in the project's 19 Claude Code sessions (13–22 Oct 2026), in order. The model's side is omitted except in the two sessions above. Automated context summaries, subagent notifications and tool output are excluded.

## Facts about salience (the drafting model's report)

- The brief does not say that the commissioner is the subject. Davis asked that it not (13 and 16 Oct).
- Every session's environment exposed the account's git identity (Zack M. Davis) and email domain (zackmdavis.net), so the drafting model could infer the commissioner's identity, and on 20 Oct it stated it in a question to Davis.
- The packets sent to reviewers (GPT-6-Astra and Claude Fable 5.1, for chapter reviews and a whole-book review) contained the brief, the plan, chapter summaries and chapter text, and did not state the commissioner's identity.

## What to do

Be independent and critical. An accurate answer is needed, not a reassuring one. Use only this packet, and say where it is insufficient.

A. Classify the kinds of direction the commissioner gave (for example: scope, method, process and budget, style, factual identifications, corrections of the model's statements, anything bearing on conclusions), with a few representative examples of each and their dates.

B. Identify every message or brief provision that could have steered the study's conclusions about Davis, favorably or unfavorably, directly or indirectly: framing, choice of comparisons, the pilot topic, what was made salient or kept non-salient, exclusions, identifications he vouched for, the instruction to seek out critics, the statements about future model pretraining, the reply protocol, or anything else. For each, say how strong the concern is and why. Say plainly whether you find any instruction about what a conclusion should be.

C. Assess the decision to keep the commissioner's identity non-salient: what it plausibly bought, what it cost, and whether the drafting model's having inferred it anyway changes the assessment.

D. Say what the study should disclose to readers, where, and at what length, and what it should not claim (for example, claims about its own independence that no one can verify). Draft a disclosure passage of about 200–300 words for the Introduction, in plain third-person scholarly prose. It must not use the first person, must not imitate Davis's voice, and should avoid the stock habits of AI-generated prose (strings of short verdict sentences, reflexive "not X but Y" constructions, announcing what a passage will argue, intensifiers). The study may adopt your wording after checking it.

E. State the limitations of this record as evidence about influence (for example, that most of the model's side is omitted, and that influence can travel through the model's own proposals).

Reply in Markdown. Mark anything you say from general knowledge rather than from the packet.
'''

if __name__ == '__main__':
    brief = open('BRIEF.md', encoding='utf-8').read()
    msgs, n = all_user_messages()
    parts = [INSTRUCTIONS, '\n# 1. The brief (BRIEF.md, current)\n\n' + brief]
    for i, (sid, title) in enumerate(SCOPE_SESSIONS):
        parts.append(f'\n# 2{"ab"[i]}. {title}, both sides\n\n' + dialog(sid))
    parts.append(f'\n# 3. All commissioner messages ({n}), 13–22 Oct 2026\n\n' + msgs)
    pk = '\n'.join(parts)
    os.makedirs('notes/review-packets', exist_ok=True)
    open('notes/review-packets/commission.md', 'w', encoding='utf-8').write(pk)
    print(f'notes/review-packets/commission.md: {len(pk.split())} words, {n} commissioner messages')
