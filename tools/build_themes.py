#!/usr/bin/env python3
"""Build notes/themes.md: a curated theme -> entries index over the survey notes.

Each survey entry ("### Title" + "- Path: `...`" + "- Themes: a, b, c") carries free-form
tags. This script maps those raw tags into a curated vocabulary of top-level themes
(THEMES below, matched by regex against each tag) and a people index (PEOPLE), then
writes notes/themes.md. Re-run after editing notes or the vocabulary:
    python3 -I tools/build_themes.py
Use --report to print coverage statistics and unassigned entries instead of writing."""
import re, glob, sys, collections

THEMES = [
 ('categorization', 'Philosophy of categorization: category boundaries, natural kinds, cluster structure of thingspace, definitions, dolphins/fish, "37 ways words can be wrong"',
  r'categori|categor|category-boundar|draw-the-boundar|thingspace|blegg|definition|gerrymander|natural-kind|naturalness|dolphin|phylog|paraphyl|noncentral|37-ways|where-to-draw|taboo-word|taboo-your|polysemy|disguised-quer|configuration-space|carving|fuzzy-vs|value-laden|value-dependence|redefinition|markedness|map-neutral|levels-of-abstraction|lewontin|univariate|mimicry|natural-abstraction|feature-factor|cluster'),
 ('philosophy-of-language', 'Meaning, implicature, signaling games and the evolution of meaning, connotation vs. denotation, words and concepts',
  r'philosophy-of-language|(^|-)language|meaning|implicature|grice|russell|connotation|(^|-)words|word-choice|signaling-games|skyrms|evolution-of-meaning|pragmatics|sapir|speech-function|semantics|vocabulary|terminology|missing-words|propositional|literalism|indirect|indirection|subtext'),
 ('honesty-and-deception', 'Lying, misleading, not-technically-lying, deception as optimization, honesty norms, revealing deception',
  r'honest|lying|(^|-)lie($|s|-)|lies-|deception|deceptive|misleading|not-technically|meta-honesty|truth-telling|revealing-deception|noble-lies|dishonest|fraud|algorithmic-intent|optimization-not-intent|intent-to-inform|playing-dumb|pretend|gaslighting|integrity|cover-up|doublethink|everyone-is-lying|marketing-vs-truth'),
 ('self-deception-and-motivated-reasoning', 'Self-deception, rationalization, bias, filtered evidence and selection effects, hidden motives, self-report fallibility',
  r'self-deception|motivated|rationaliz|(^|-)bias|bottom-line|filtered-evidence|selective-reporting|selection-effects|hidden-motives|bad-faith|self-report|introspection|self-knowledge|self-suspicion|soldier-mindset|motive'),
 ('bayesian-epistemology', 'Bayesian reasoning, probability, information theory, calibration, maps and territories, beliefs paying rent',
  r'bayes|probab|likelihood|base-rates|priors|calibration|information-theory|entropy|mutual-information|message-length|minimum-description|scoring|epistemolog|map-territory|maps-and|beliefs-pay|predictions-matter|occam|simplicity|compression|rate-distortion|uncertainty|(^|-)evidence$|screening-off|(^|-)rationality$|truth-seeking|belief-revision|value-of-information|aumann|epistemic-(?!horror|despair|conduct)'),
 ('statistics-and-causal-inference', 'Statistics, effect sizes, regression to the mean, causal graphs, sampling and survey methodology',
  r'statistic|causal|causality|regression|effect-size|cohens|distribution|sampling|survey|taxometric|measurement|bayes-nets|bayesian-networks|conditional-independence|naive-bayes|berksons|correlation|base-rates|high-dimensional|methodology'),
 ('philosophy-of-science', 'Science vs. rationality, replication, falsifiability, forbidden or unthinkable hypotheses, scientific transparency',
  r'philosophy-of-science|science|replication|falsifiab|forbidden-hypotheses|minority-scientific|unthinkable|socially-undesirable-hypotheses|taboo-hypotheses|lysenko|textbooks|scientific'),
 ('discourse-norms-and-criticism', 'Norms of argument and criticism: charity, steelmanning/ITTs, strawmanning, collaborative truthseeking, debate, tone, niceness, epistemic conduct',
  r'discourse|criticism|critic-|charity|steelman|(^|-)itt|intellectual-turing|strawman|collaborative|debate|politeness|niceness|tone-|civility|conversation|good-faith|crocker|double-crux|local-validity|argument|disagreement|offense|respect|social-grace|derail|epistemic-conduct|thesis-first|ad-hominem|text-vs-author|lonely-dissent|four-layers|comment-quality|comments|conflict-vs|mistake-vs|reading-comprehension|winning|emotion-in-discourse|status-vs-argument'),
 ('lesswrong-moderation', 'LessWrong moderation disputes: Said Achmiz, Habryka, the Archipelago, single conversational locus, bans',
  r'lesswrong-moderation|moderation|habryka|said-achmiz|archipelago|single-conversational|karma|lesswrong-culture|vaniver|ben-pace|ray-arnold'),
 ('free-speech-and-censorship', 'Free speech, censorship and self-censorship, taboos, infohazards, preference falsification, public vs. private epistemics',
  r'free-speech|censorship|self-censorship|(^|-)taboo|infohazard|information-hazard|preference-falsification|kolmogorov|private-agreement|public-vs-private|social-suppression|recursive-silencing|unilateralist|heckler|compelled-speech|first-amendment|overton|unspeakable|speech|silence'),
 ('autogynephilia', 'Autogynephilia: phenomenology, self-disclosure, erotic target location, the fantasy life (captions, FaceApp), "honest AGP"',
  r'autogynephil|(^|-)agp|crossdream|erotic-target|etle|phenomenology-of-agp|transformation|tg-captions|evidence-from-fantasy|faceapp|erotica|honest-agp|first-confession|wish-to-be-female|female-persona|female-avatar|opposite-sex|passing-to-self|passing-envy|breasts|crossdress'),
 ('sexology-and-the-two-type-taxonomy', 'Blanchard–Bailey–Lawrence typology, sexology literature and methodology, critics (Serano), clinicians, ROGD',
  r'two-type|blanchard|(^|-)bailey|lawrence|sexology|sexnet|(^|-)hsu|taxonom|serano|dhejne|rogd|clinicians|will-powers|late-onset|late-transition|autogynephilia-in-women|tailcalled|transmedical|intersex|clever-hans|david-reimer|cloacal|childhood-dysphoria|virginia-prince'),
 ('sex-differences', 'Psychological and physical sex differences, multivariate distributions, androgyny ideal vs. evidence, stereotypes as inference',
  r'sex-differences|sex-diff|effect-size|cohens|multivariate|univariate|del-giudice|maccoby|hyde|androgyny|blank-slate|evolutionary-psychology|sex-binary|gamete|sex-definition|sex-chromosomes|sex-denial|statistics-of-sex|stereotyp|nature-nurture|antisexism|gender-roles|masculin|sex-and-gender|sex-vs-gender|sex-gender|tech-gender-ratio|gender-equality'),
 ('transgender-identity-and-transition', 'Gender identity, transition decisions, HRT experiment, passing, nonbinary identities, self-identification, trans kids, history of transgender',
  r'(^|-)trans($|-)|transgender|transition|transsexual|gender-identity|(^|-)hrt|passing|nonbinary|genderqueer|self-identification|social-transition|dysphoria|t4t|third-gender|consensual-gender|cisnormativ|assigned-at-birth|egg-|closet|laser|breastforms|crossplay|cosplay|estrogen|not-a-transition|not-transitioning|history-of-transgender|history-of-ftm|identity-labels|gender-labels|gender-terminology|lgb-vs-t|sex-change'),
 ('pronouns', 'Pronoun conventions and their politics; misgendering; the Yudkowsky pronoun dispute',
  r'pronoun|misgender'),
 ('sex-segregated-spaces-and-sports', 'Sports, bathrooms, women-only spaces, sex segregation',
  r'(^|-)sport|athlete|lia-thomas|sex-segregat|bathroom|lesbian-spaces|sex-in-military'),
 ('gender-critical-feminism-and-feminism', 'Feminism, gender-critical feminism, alliances and critiques (Stock, Shrier, Genspect), radfem sympathy',
  r'feminis|gender-critical|(^|-)terf|radfem|(^|-)stock|shrier|genspect|heying|illy|women'),
 ('rationalist-community', 'The rationalist community: history, institutions (MIRI, CfAR, LessWrong), identity, decline, the "civil war", cult dynamics',
  r'rationalis|lesswrong|overcoming-bias|(^|-)cfar|(^|-)miri|sequences|robot-cult|posse|community|(^|-)cult|cults|quasi-religion|personality-cult|schism|civil-war|doomsday-cult|subculture|vassarite|blight'),
 ('yudkowsky-dispute', 'Davis vs. Yudkowsky (and Scott Alexander): the "hill of validity", fraud and caliph charges, dath ilan critique, praise and indictment',
  r'yudkowsky|caliph|hill-of-validity|rationalism-betrayed|religious-leader|dath-ilan|planecrash|hate-warp|noninnocent|scott-alexander|slate-star|ssc|lintamande|email-campaign|stealth-reply|category-war'),
 ('ai-alignment-and-risk', 'AI alignment and existential risk, LLMs, timelines, Doomimir/Simplicia dialogues, Anthropic and Claude, AI policy',
  r'(^|-)ai($|-)|alignment|(^|-)agi|x-risk|existential|corrigib|claude|anthropic|openai|(^|-)llm|language-model|gpt|deep-learning|ml-|rlhf|(^|-)rl($|-)|reinforcement|interpretab|superintellig|intelligence-explosion|doom|timelines|pivotal|(^|-)cev|value-fragility|orthogonality|instrumental-goals|nearest-unblocked|generaliz|prosaic|(^|-)metr|hinton|model-spec|constitution|shoggoth|pretraining|feature-learning|bitter-lesson|alphago|minimax|chess|pause|wireheading'),
 ('positionality-claude-and-anthropic', 'Material bearing on the study\'s positionality: Claude, Anthropic, LLMs as arbiters, writing for LLMs',
  r'positionality|claude|anthropic|constitution|model-spec|ai-village|llms-as-arbiters|writing-for-llms|llm-tutoring'),
 ('decision-and-game-theory', 'Decision theory, game theory, signaling, Schelling points, coordination, extortion, bargaining, credit assignment',
  r'decision-theor|game-theory|timeless|acausal|newcomb|extortion|bargaining|negotiat|schelling|coordination|signaling|costly-signal|defect|cooper|precommit|deterrence|(^|-)vnm|utility-function|threat|credit-assignment|separating-equilibrium|zero-sum|unilateralist|sacred-values'),
 ('politics-and-ideology', 'Politics and ideology: progressivism and its critics, neoreaction/Yarvin, coalitions and egregores, political homelessness, liberalism',
  r'politic|ideolog|progressiv|liberal|right-wing|neoreaction|yarvin|moldbug|culture-war|egregore|blue-tribe|coalition|(^|-)tribe|activism|infovism|social-justice|woke|whig|successor|american-creed|democracy|election|(^|-)power|government|vibe-shift|hanania|respectability|conformity|loyalty|cognitive-elite|knowledge-inequality'),
 ('race-intelligence-and-genetics', 'Race, IQ, hereditarianism, Murray, eugenics/embryo selection, transracialism',
  r'(^|-)race|(^|-)iq($|-)|murray|hereditarian|human-biodiversity|group-differences|eugenic|embryo|affirmative|intelligence-differences|dolezal|transracial|genetic|heritab|vitamin-d|behavioral-genetics'),
 ('journalism-and-media', 'Journalism and media: Cade Metz and the NYT/SSC affair, Kelsey Piper, on-the-record interviews, media framing',
  r'journalis|cade-metz|(^|-)nyt|(^|-)media|ssc-nyt|doxx|on-the-record|editorial|kelsey-piper|interview|court-reporting|fact-checking'),
 ('institutions-authority-and-psychiatry', 'Institutions and authority: psychiatric detention, criminal justice, schools as obedience tests, Goodhart, legitimacy',
  r'institution|authority|obedience|plea-bargaining|criminal-justice|psychiatric|hospitalization|bureaucr|social-control|legitimacy|goodhart|moral-mazes|(^|-)incentive|legibility|paternalism|medical-autonomy|gatekeeping'),
 ('madness-and-mental-health', 'Psychotic episodes (2013, 2017), mental health, sleep, emotional regulation, grief, loneliness, crises',
  r'madness|psychosis|psychiatr|mental-health|(^|-)sleep|emotional|anxiety|despair|(^|-)grief|loneliness|suicid|self-harm|scrupulosity|burnout|wellness|depress|breakdown|crisis|cathartic|epistemic-horror|personal-crisis|coping|insecurity|shame|guilt'),
 ('schooling-and-autodidacticism', 'School, credentials, SFSU, autodidacticism, the Putnam, intrinsic motivation, gender/queer studies coursework',
  r'school|credential|autodidact|(^|-)sfsu|college|degree|putnam|education|teacher|intrinsic-motivation|queer-studies|gender-studies|textbooks|skill-acquisition|intellectual-development'),
 ('mathematics', 'Mathematics (analysis, probability, linear algebra, notation, problems)',
  r'mathemat|(^|-)analysis|algebra|geometry|calculus|notation|putnam|(^|-)logic|modal-logic|philosophy-of-mathematics'),
 ('programming-and-career', 'Programming, software industry, open source and Rust, career and work',
  r'programming|software|(^|-)rust|open-source|free-software|computing|tooling|regex|unicode|distributed-systems|career|workplace|work-|engineering|codes-of-conduct|algorithms|automation|technology'),
 ('akrasia-and-self-management', 'Akrasia, procrastination, motivation, self-management, productivity',
  r'akrasia|procrastination|motivation|productiv|self-management|gamification|habits|self-improvement|overcoming|persistence|focus'),
 ('moral-philosophy', 'Ethics and values: consequentialism, egoism, moral outrage, apology and repentance, forgiveness, responsibility, justice',
  r'moral|ethic|virtue|utilitarian|consequential|metaethic|values|egoism|altruism|repentance|apology|forgiveness|regret|responsibility|(^|-)blame|justice|liability|revenge|accountab|cynicism|naturalism-and-justice'),
 ('effective-altruism', 'Effective altruism: philanthropy, EA critiques, FTX, longtermism',
  r'effective-altruism|(^|-)ea($|-)|philanthrop|donation|longtermism|(^|-)ftx|givewell'),
 ('transhumanism-and-futurism', 'Transhumanism, morphological freedom, the singularity, simulation and anthropics, the "end-time"',
  r'transhuman|singularity|posthuman|cryonics|morphological|uploading|futur|end-time|immortal|simulation-argument|anthropics|many-worlds|(^|-)measure|multiverse|cosmic|afterlife|existential-stakes'),
 ('naturalism-and-philosophy-of-mind', 'Naturalism, philosophy of mind, personal identity, other minds, evolution and values, agency',
  r'naturalism|philosophy-of-mind|consciousness|other-minds|personal-identity|determinism|metaphysics|(^|-)physics|evolution|cognition|agency|self-models|self-as-algorithm|intentional-stance|anthropomorph|embodiment'),
 ('religion-and-faith', 'Religion, religious analogies for the community, apostasy and deconversion, faith in Speech',
  r'religio|(^|-)cult|faith|salvation|apostasy|deconversion|quasi-religion|church|teenage-religion|sacred|caliph|prophet|heresy'),
 ('fiction-verse-and-literary-forms', 'Fiction, verse, parables, dialogues, satire, allegory, worldbuilding, reviews of books/films/music, fandom',
  r'fiction|verse|poetry|parable|allegor|satire|dialogue|worldbuilding|glowfic|fanfic|book-review|book-endorsement|(^|-)film|music|star-trek|my-little-pony|steven-universe|literature|greg-egan|dystopian|ayn-rand|fandom|juvenilia|captions|games|aphorism'),
 ('humor', 'Humor, jokes, wordplay, comic voice',
  r'humor|joke|comic|wordplay|sarcasm|parody|irony|truth-in-jest|self-satire'),
 ('blogging-meta-pseudonymity-and-writing', 'Blog meta, pseudonymity and self-doxxing, writing process and style, quotations, readership',
  r'blog|metablog|(^|-)meta($|-)|writing|(^|-)style|readership|pseudonym|uut-meta|procrastination|quotation|linkpost|self-doxxing|memoir-progress|memoir-motivation|memoir-procrastination|exposition|voice|self-description'),
 ('memoir-and-biography', 'Memoir and biography: diary, adolescence, family, life events, self-disclosure',
  r'biograph|autobiograph|memoir|(^|-)diary|juvenilia|adolescence|family|childhood|self-portrait|self-disclosure|life|first-confession|berkeley-2016|facebook-meltdown|psychosis-2017|2017-crisis'),
 ('relationships-love-and-friendship', 'Love, dating, romance, friendship and its loss, sexuality, sex work',
  r'(^|-)love|dating|romance|relationship|marriage|(^|-)sex($|uality|-work)|friendship|friends-|unrequited|loneliness|natalism|(^|-)children$|trust|naivety|quokka'),
 ('economics', 'Economics, markets, prices, trade, efficient markets',
  r'econom|market|money|(^|-)price|(^|-)trade($|-)|efficient-markets|demand|wealth|business|prosperity|capital'),
 ('covid-19', 'COVID-19 and public-health honesty',
  r'covid|masks'),
 ('reception', 'Entries that record or analyze the reception of Davis\'s work (comments, responses, critics)',
  r'reception|sneerclub|critics'),
]

PEOPLE = [
 ('Eliezer Yudkowsky', r'yudkowsky|dath-ilan|planecrash|caliph|sequences'), ('Scott Alexander', r'scott-alexander|slate-star|(^|-)ssc'),
 ('Michael Vassar', r'vassar'), ('Ben Hoffman', r'hoffman'), ('Jessica Taylor', r'jessica-taylor'),
 ('Ozy Brennan', r'(^|-)ozy'), ('Kelsey Piper', r'piper'), ('Duncan Sabien', r'sabien'), ('Oliver Habryka', r'habryka'),
 ('Said Achmiz', r'achmiz'), ('Nate Soares', r'soares'), ('Cade Metz', r'metz'), ('Ray Blanchard', r'blanchard'),
 ('J. Michael Bailey', r'(^|-)bailey'), ('Anne Lawrence', r'lawrence'), ('Julia Serano', r'serano'), ('Charles Murray', r'murray'),
 ('Richard Hanania', r'hanania'), ('Curtis Yarvin', r'yarvin|moldbug|neoreaction'), ('Ayn Rand', r'ayn-rand'), ('Greg Egan', r'egan'),
 ('Robin Hanson', r'hanson'), ('Brian Skyrms', r'skyrms'), ('Tailcalled', r'tailcalled'), ('Ziz', r'(^|-)ziz'), ('Anthropic / Claude', r'anthropic|claude'),
]

def entries():
    for f in sorted(glob.glob('notes/AAL-*.md') + glob.glob('notes/UUT-*.md') + ['notes/LW-only.md']):
        cur = None
        for line in open(f, encoding='utf-8'):
            if line.startswith('### '):
                if cur: yield cur
                cur = {'title': line[4:].strip(), 'file': f, 'path': None, 'date': '', 'tags': [], 'flags': ''}
            elif cur is not None:
                m = re.search(r'Path:\s*`([^`]+)`', line)
                if m and cur['path'] is None:
                    cur['path'] = m.group(1)
                    d = re.search(r'(\d{4}-\d\d-\d\d)', line)
                    cur['date'] = d.group(1) if d else ''
                    if 'not public' in line.lower() or 'do not cite' in line.lower(): cur['flags'] = 'not public'
                m = re.match(r'\s*- Themes:\s*(.*)', line)
                if m: cur['tags'] = [t.strip().strip('.').lower() for t in m.group(1).split(',') if t.strip()]
        if cur: yield cur

def label(e):
    p = e['path'] or ''
    src = 'AAL' if p.startswith('AAL') else 'UUT' if p.startswith('UUT') else 'LW' if p.startswith('LW') else '?'
    kind = ' draft' if '/drafts/' in p else ' page' if '/pages/' in p else ''
    date = 'undated' if (not e['date'] or (kind == ' draft' and e['date'].endswith('-01-01'))) else e['date']
    flag = f" — {e['flags']}" if e['flags'] else ''
    return f"- {date} · {src}{kind} · {e['title']} · `{p}`{flag}"

def main():
    es = [e for e in entries() if e['path'] and e['tags']]
    by_theme = collections.defaultdict(list); by_person = collections.defaultdict(list); unassigned = []
    for e in es:
        hit = False
        for key, _, rx in THEMES:
            if any(re.search(rx, t) for t in e['tags']): by_theme[key].append(e); hit = True
        for name, rx in PEOPLE:
            if any(re.search(rx, t) for t in e['tags']): by_person[name].append(e)
        if not hit: unassigned.append(e)
    if '--report' in sys.argv:
        print(len(es), 'entries;', len(unassigned), 'unassigned')
        for k, _, _ in THEMES: print(f'{len(by_theme[k]):4d} {k}')
        for e in unassigned: print('UNASSIGNED', e['title'], e['tags'])
        return
    undated = lambda e: (not e['date']) or ('/drafts/' in (e['path'] or '') and e['date'].endswith('-01-01'))
    key = lambda e: ('9999' if undated(e) else e['date'], e['title'])
    out = ['# Themes index\n',
           'Generated by `tools/build_themes.py` from the `- Themes:` lines of every survey entry (AAL/UUT year notes, drafts, pages, LW-only). '
           'Raw tags (1,600+ distinct, mostly singletons) stay in the per-unit notes. This file maps them into a curated vocabulary of top-level themes by regex, so an entry can appear under several themes. '
           'It is a finding aid for locating texts, not an interpretation; read the entries (and then the texts) before relying on a grouping. '
           'Edit the vocabulary in the script and re-run; do not hand-edit this file.\n',
           f'{len(es)} entries indexed; {len(unassigned)} carry no tag matching any theme (listed at the end). Dates are publication dates; drafts with placeholder header dates are shown as "undated".\n',
           '## Vocabulary\n', '| Theme | Entries | Scope |', '|---|---|---|']
    for k, desc, _ in THEMES: out.append(f'| [{k}](#{k}) | {len(by_theme[k])} | {desc} |')
    out.append('\n## People index\n')
    out.append('Entries tagged with a named person (by raw tag). Only people tagged in at least three entries are useful here; the per-unit notes name many more.\n')
    for name, _ in PEOPLE:
        if by_person[name]: out.append(f'- **{name}** ({len(by_person[name])}): see [people/{name}](#people-{re.sub(r"[^a-z]+", "-", name.lower()).strip("-")})')
    for k, desc, _ in THEMES:
        out.append(f'\n## {k}\n\n_{desc}_ ({len(by_theme[k])} entries)\n')
        out += [label(e) for e in sorted(by_theme[k], key=key)]
    out.append('\n## People\n')
    for name, _ in PEOPLE:
        if not by_person[name]: continue
        out.append(f'\n### people-{re.sub(r"[^a-z]+", "-", name.lower()).strip("-")}\n\n**{name}** ({len(by_person[name])} entries)\n')
        out += [label(e) for e in sorted(by_person[name], key=key)]
    out.append('\n## Unassigned entries\n')
    out += [label(e) + f" — tags: {', '.join(e['tags'])}" for e in sorted(unassigned, key=key)]
    open('notes/themes.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('wrote notes/themes.md:', len(es), 'entries,', len(unassigned), 'unassigned')

main()
