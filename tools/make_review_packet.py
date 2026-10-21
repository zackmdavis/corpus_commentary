#!/usr/bin/env python3
"""Build a self-contained review packet for one chapter of the study.

Usage: python3 -I tools/make_review_packet.py [STEM ...]
       (no arguments: build packets for every chapter in study/)
       python3 -I tools/make_review_packet.py whole-book
       (one packet for a review of the whole study: instructions, BRIEF.md,
       notes/plan.md, and the front matter, every chapter (without its works
       cited) and the hand-written apparatus as plain text; written to
       notes/review-packets/whole-book.md)

Writes notes/review-packets/<stem>.md: reviewer instructions, BRIEF.md,
notes/plan.md, notes/chapter-summaries.md, and the chapter as plain Markdown
(markup, data-src attributes and link targets stripped). The packet is
model-agnostic: a reviewer (Fable subagent, Codex/GPT, or anything else) reads
this one file and returns the review as its reply. Reviews and the model that
wrote each are logged in notes/reviews/LOG.md.
"""
import html, os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'notes', 'review-packets')

# Areas of scholarship the reviewer should consider, per chapter.
FOCUS = {
    '00-introduction': "whether the thesis as stated here is the one the chapters deliver (compare the chapter summaries); the positionality disclosure (the study is written by Claude, and Ch. 11 assesses Davis's criticism of Claude's constitution); the accuracy and fairness of the reception survey as presented; the method statement. Scholarship: author-centred studies of online or self-published writers, histories of the rationalist community, methodological writing on studying living authors.",
    '01-apprentice': "the early blog (2011–2016) and whether the chapter's reading of it as formation is earned or retrospective. Scholarship: history of LessWrong and the rationalist community, the reception of Yudkowsky's Sequences, Bayesian epistemology as popularized there, autodidact and blog-as-notebook traditions.",
    '02-testimony': "self-report as evidence, first-person testimony and its limits. Scholarship: epistemology of testimony and self-knowledge, introspection research, philosophy of sexual and gender identity, autobiography studies.",
    '03-two-type-taxonomy': "the sexology and its contested empirical literature, including the critics. Scholarship: the Blanchard typology and its critics (Serano, Moser, Veale and others), measurement and sampling issues, recent empirical work. Mark anything from memory.",
    '04-categorization': "philosophy of language, conceptual engineering and ethics, natural kinds, social ontology, philosophy of biology, signaling theory, cognitive science of categorization.",
    '05-deception': "philosophy of deception and lying, teleosemantics and function attribution, signaling theory and evolutionary accounts of deception, philosophy of motive attribution.",
    '06-discourse-norms': "norms of discourse and assertion, social epistemology, moderation and community governance, the ethics of criticism.",
    '07-whole-dumb-story': "fairness to every named party (Yudkowsky, Alexander and others are living people whose accounts may differ from Davis's); whether the chapter separates the role-relative 'fraud' charge from inference about motive as the plan requires; the press section. Scholarship and other sources: journalism and histories of the rationalist community, writing on intellectual authority and charismatic leadership in communities, memoir as evidence.",
    '08-forms': "the literary forms (dialogue, humor, allegory, verse, fiction) and whether the chapter's claims about what each form does for the argument hold. Scholarship: the philosophical dialogue, satire and allegory, theories of humor, the didactic fable.",
    '09-obedience-tests': "school, psychiatry, and coercion; fairness to Davis and to institutions he describes (do not name hospital staff). Scholarship: philosophy of education and compulsory schooling, psychiatric coercion and consent, critiques of credentialism, sociology of total institutions.",
    '10-politics-race': "the politics of description and the race/IQ material; whether the chapter's empirical verdicts match the literature it cites and whether it treats Davis's claims at the strength he states them. Scholarship: behavioral genetics and the group-differences debate (including critics on both sides), philosophy of race, game theory of norms and conventions, free-speech theory.",
    '11-faking-deeply': "the AI alignment writing and the critique of Claude's constitution. The study is written by Claude, and the plan (§4) pre-commits to a positionality procedure: check whether the chapter applies it, and whether it is softer or harsher on Anthropic and Claude than on anyone else. Scholarship: corrigibility and the alignment literature, deceptive alignment, AI-governance and model-specification documents.",
    '12-conclusion': "whether the conclusion states what the chapters actually showed (compare the chapter summaries), whether its verdicts are stronger or weaker than the chapters', and whether the open questions are the right ones.",
}

INSTRUCTIONS = """\
# Review packet: {title}

You are reviewing one chapter of a book-length scholarly study, written by
Claude (an Anthropic model), of the blogging of Zack M. Davis: the blogs *An
Algorithmic Lucidity* and *The Scintillating But Ultimately Untrue Thought*,
his LessWrong posts, and his public drafts. Everything you need is in this
file, in this order: these instructions; the study's standing brief
(BRIEF.md); the thesis and chapter plan (notes/plan.md); summaries of all
chapters as drafted (notes/chapter-summaries.md); and the chapter under
review, converted to plain text with links and markup removed.

Do not read any other files and do not browse the web. You do not have the
corpus. Whatever you say about what a post, comment or paper contains is
unverified until the main agent checks it against the source, so where you
question how something is characterized, name the post (or commenter and
thread) so it can be checked. The brief's section "Per-chapter review"
defines your job; the brief's rules on voice and citation apply to any prose
you write.

Cover, with specifics (quote the chapter's sentence you are criticizing, or
give the section number):
- weak or overstated arguments;
- places where Davis is treated unfairly, including concessions the chapter
  acknowledges and then ignores, or readings less charitable than the text
  supports; and also places where the chapter is too soft on Davis;
- missing objections, from Davis's side as well as his critics';
- relevant scholarship left out. For this chapter, consider: {focus}
  Be specific, and mark every claim you make from memory with [memory]. The
  main agent will fetch and check anything before using it;
- overlap or drift relative to the plan (§1 thesis and this chapter's entry
  in §3) and to the other chapters' summaries, and anything that should move
  to another chapter;
- structure, clarity and prose: where the chapter is hard to follow,
  repetitive, compressed past clarity, or reads as AI-generated (the brief
  lists the habits to look for).

You may also write prose: revised passages, new paragraphs, or a restructured
section, wherever you can do better than the draft. Put it in clearly labeled
blocks ("Proposed replacement for §N, paragraph beginning '…'"). Write in the
study's voice: plain, exact scholarly prose; Davis is "Davis" (he/him). Do not
invent quotations from Davis or anyone else; where proposed prose needs one,
write [QUOTE NEEDED: what it should show]. Prose is welcome wherever you
can do better than the draft; with each proposed passage, say what problem in
the draft it addresses, so the change can be judged. If prose of yours is
adopted, the study will credit it to your model by name (see "Attribution of
reviewers' contributions" in the brief), so write it to the study's
publication standard.

End with a short numbered list, "Checks for the main agent": factual claims in
the chapter you suspect are wrong or overstated, each with the post or thread
to check.

Be candid and specific; a useful review is a critical one. Aim for roughly
2,000–3,500 words. Your reply is the review, in Markdown, starting with a
level-1 heading naming the chapter. It will be saved as the review file.
Do not state which model you are; the main agent records that from the run.
"""

SKIP = {'script', 'style', 'head', 'nav'}

class ToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.quote, self.list = [], 0, 0, []
    def nl(self, n=2):
        self.out.append('\n' * n + '> ' * self.quote)
    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        elif self.skip:
            return
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.nl(); self.out.append('#' * (int(tag[1]) + 1) + ' ')
        elif tag == 'p':
            self.nl()
        elif tag == 'blockquote':
            self.quote += 1; self.nl()
        elif tag in ('ul', 'ol'):
            self.list.append(tag); self.nl(1)
        elif tag == 'li':
            self.nl(1); self.out.append('  ' * (len(self.list) - 1) + '- ')
        elif tag == 'br':
            self.nl(1)
        elif tag == 'dt':
            self.nl(); self.out.append('**')
        elif tag == 'dd':
            self.nl(1); self.out.append('- ')
        elif tag in ('i', 'em', 'cite'):
            self.out.append('*')
        elif tag == 'q':
            self.out.append('“')
    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
        elif self.skip:
            return
        elif tag == 'blockquote':
            self.quote = max(0, self.quote - 1); self.nl()
        elif tag in ('ul', 'ol'):
            self.list and self.list.pop(); self.nl()
        elif tag == 'dt':
            self.out.append('**')
        elif tag in ('i', 'em', 'cite'):
            self.out.append('*')
        elif tag == 'q':
            self.out.append('”')
    def handle_data(self, data):
        if not self.skip:
            self.out.append(re.sub(r'\s+', ' ', data))

def chapter_text(path, drop_works=False):
    p = ToMarkdown()
    src = open(path, encoding='utf-8').read()
    if drop_works:
        src = re.sub(r'<section class="works[^"]*"[^>]*>.*?</section>', '', src, flags=re.S)
    src = re.sub(r'<span class="chapno">([^<]*)</span>', r'\1: ', src)
    p.feed(src)
    text = ''.join(p.out)
    lines = ['' if re.fullmatch(r'[> ]*', l) else l.rstrip() for l in text.split('\n')]
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

def title_of(path):
    m = re.search(r'<title>(.*?)</title>', open(path, encoding='utf-8').read(), re.S)
    return html.unescape(m.group(1).strip()) if m else os.path.basename(path)

def read(rel):
    return open(os.path.join(ROOT, rel), encoding='utf-8').read().strip() + '\n'

def build(stem):
    chap = os.path.join(ROOT, 'study', stem + '.html')
    title = title_of(chap)
    parts = [
        INSTRUCTIONS.format(title=title, focus=FOCUS[stem]),
        '\n---\n\n# BRIEF.md\n\n' + read('BRIEF.md'),
        '\n---\n\n# notes/plan.md\n\n' + read('notes/plan.md'),
        '\n---\n\n# notes/chapter-summaries.md\n\n' + read('notes/chapter-summaries.md'),
        '\n---\n\n# The chapter under review: study/' + stem + '.html (plain text)\n\n' + chapter_text(chap),
    ]
    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, stem + '.md')
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(''.join(parts))
    words = sum(len(p.split()) for p in parts)
    print(f'{os.path.relpath(dest, ROOT)}: {words} words')

WHOLE_BOOK = 'whole-book'

# Pieces in reading order. The thematic index and the bibliography are
# generated from the chapters' own links (tools/build_apparatus.py), so they
# are left out; the hand-written apparatus is included.
BOOK = ['index'] + sorted(FOCUS) + ['a-chronology', 'd-questions']

WHOLE_INSTRUCTIONS = """\
# Review packet: the whole study

You are reviewing a complete book-length scholarly study, written by Claude
(an Anthropic model), of the blogging of Zack M. Davis: the blogs *An
Algorithmic Lucidity* and *The Scintillating But Ultimately Untrue Thought*,
his LessWrong posts, and his public drafts. Each chapter has already had at
least one review of its own, and the drafting model has made a cross-chapter
pass and a length pass. Your job is the review no single-chapter reader could
do: of the book as a whole.

Everything you need is in this file, in this order: these instructions; the
study's standing brief (BRIEF.md); the thesis and chapter plan
(notes/plan.md); and the whole study as plain text with links and markup
removed: the front matter, the Introduction, Chapters 1–11, the Conclusion,
the chronology and the questions appendix. (The generated thematic index and
bibliography, and each chapter's works cited, are omitted.)

Do not read any other files and do not browse the web. You do not have the
corpus. Whatever you say about what a post, comment or paper contains is
unverified until the main agent checks it against the source, so where you
question how something is characterized, name the post (or commenter and
thread) and the chapter and section where the study discusses it. The
brief's rules on voice and citation apply to any prose you write.

Cover, with specifics (quote the sentence you are criticizing and give
chapter and section):
- the thesis: whether the Introduction's four claims are the ones the
  chapters deliver, whether the Conclusion states what the chapters showed,
  and where any of the three overstates or understates the others;
- consistency: the same post, person, event or argument characterized
  differently in different chapters; verdicts that conflict; terms (the
  criterion, the norm of accounting, the coordination argument and its three
  forms, disclosure and its conditions) used in different senses;
- even-handedness across the book: whether the same evidential standard is
  applied to Davis, to Yudkowsky, Alexander and his other interlocutors, to
  institutions, and to Anthropic and Claude (the study is written by Claude,
  and Chapter 11 assesses Davis's criticism of Claude's constitution); places
  where Davis is treated unfairly, including concessions acknowledged in one
  chapter and ignored in another, and places where the book is too soft on
  him;
- repetition and cross-references: material said twice, references to
  another chapter that the other chapter does not fulfil, and things one
  chapter leaves to another that nothing picks up;
- missing objections and relevant scholarship that the book as a whole
  leaves out (not chapter-level gaps already likely to have been raised).
  Mark every claim you make from memory with [memory]; the main agent will
  fetch and check anything before using it;
- length. The book is about 96,000 words against a target of roughly 80,000
  and a ceiling of 100,000, after a length pass that cut what could go
  without losing an argument step, a concession to Davis, or an objection a
  review had added. Say which further cuts you would make (chapter, section,
  approximate words, what is lost);
- structure and prose: the order of parts and chapters, chapters that do
  not earn their length, and prose habits that recur across the book or read
  as AI-generated (the brief lists the habits to look for).

You may also write prose: revised passages or replacement paragraphs, in
clearly labeled blocks ("Proposed replacement for Ch. N §M, paragraph
beginning '…'"), each with a sentence on the problem it addresses. Write in
the study's voice: plain, exact scholarly prose; Davis is "Davis" (he/him).
Do not invent quotations from Davis or anyone else; where proposed prose
needs one, write [QUOTE NEEDED: what it should show]. If prose of yours is
adopted, the study will credit it to your model by name (see "Attribution of
reviewers' contributions" in the brief), so write it to the study's
publication standard.

Put the most important problems first. End with a numbered list, "Checks for
the main agent": factual claims or characterizations you suspect are wrong,
overstated or inconsistent, each with chapter, section, and the post or
thread to check.

Be candid and specific; a useful review is a critical one. Aim for roughly
4,000–7,000 words. Your reply is the review, in Markdown, starting with a
level-1 heading. It will be saved as the review file. Do not state which
model you are; the main agent records that from the run.
"""

def build_whole_book():
    parts = [
        WHOLE_INSTRUCTIONS,
        '\n---\n\n# BRIEF.md\n\n' + read('BRIEF.md'),
        '\n---\n\n# notes/plan.md\n\n' + read('notes/plan.md'),
    ]
    for stem in BOOK:
        path = os.path.join(ROOT, 'study', stem + '.html')
        parts.append('\n---\n\n# study/' + stem + '.html (plain text)\n\n'
                     + chapter_text(path, drop_works=True))
    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, WHOLE_BOOK + '.md')
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(''.join(parts))
    words = sum(len(p.split()) for p in parts)
    print(f'{os.path.relpath(dest, ROOT)}: {words} words')

stems = sys.argv[1:] or sorted(s for s in FOCUS
                               if os.path.exists(os.path.join(ROOT, 'study', s + '.html')))
for s in stems:
    build_whole_book() if s == WHOLE_BOOK else build(s)
