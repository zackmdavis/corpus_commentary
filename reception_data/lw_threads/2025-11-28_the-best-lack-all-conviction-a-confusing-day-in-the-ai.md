Title: The Best Lack All Conviction: A Confusing Day in the AI Village
LessWrong-URL: https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai
Posted: 2025-11-28
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 8 (commentCount field: 8)

#### [-] Vladimir_Nesov · 15 karma · 2025-11-28 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=anLCTkn8bQcfTxYGF
I guess this kind of thing will stop happening in a year. It's very similar to how a chatbot (without tool use) discusses bugs (it made) in programming puzzles, where you point out bugs A and B and it fixes them, then you point out C, it fixes C but lets A back into the code, and also congratulates itself that the code now works correctly. But then in the next version of the chatbot this stops happening (for the same puzzle), or it takes more bugs and more complicated puzzles for this to happen.

Larger models seem to be able to hold more of such corrections in mind at once (mistakes they've made and then corrected; as opposed to things they didn't make a mistake about, thus small models can still solve difficult problems). Gemini 3 Pro and Opus 4.5 seem to be the largest models right now, and the next step of scale [might arrive with Gemini 4](https://www.lesswrong.com/posts/fdCaCDfstHxyPmB9h/vladimir_nesov-s-shortform?commentId=CHPoGf9yD8QQkzoEQ) next year (as Google builds enough Ironwood datacenters to serve inference), and maybe Opus 5.5 (if it follows this year's pattern by starting out as an unwieldy expensive pretrain in the form of Opus 5 in early 2026, and then becomes a reasonably priced properly RLVRed model at the end of 2026, as Anthropic's [gigawatt of TPUs](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) comes online, probably also Ironwood).

Currently GPT-5 is the smallest model, and Grok 4 might be in the middle (Musk [recently claimed](https://www.youtube.com/watch?v=GwfLkEOW37Q) it's 3T params, which must be total params). The next move (early 2026) is likely OpenAI catching up to Google and Anthropic with a GPT-4.5 sized model (though they [probably won't have the inference hardware](https://www.lesswrong.com/posts/fdCaCDfstHxyPmB9h/vladimir_nesov-s-shortform?commentId=CHPoGf9yD8QQkzoEQ) to serve it as a flagship model before late 2026) or Grok 5 (which was also claimed to be a 6T param model on that podcast; with less users than OpenAI, it might even be reasonably priced given what GB200/GB300 NVL72s xAI will manage to secure). These models won't be exceeding Gemini 3 Pro and Opus 4.5 in scale though (where Opus 4.5 appears to be the first properly RLVRed revision of Opus 4, relying on Trainium 2 for inference, in the same way as Gemini 3 Pro is probably the first model in that weight class with a lot of RLVR, relying on Trillium for inference).

#### [>] shawnghu · 1 karma · 2025-11-28 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=Qh7Ehfts5dp5WazEZ
I suppose you mean that in a year this kind of thing will stop happening so obviously, but as you suggest, more complicated situations will still elicit this problem so by construction it'll be harder to notice (and probably more impactful).

#### [-] AlphaAndOmega · 41 karma · 2025-11-28 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=8rLrZhccpX7g693Nq
I just wanted to say that I really enjoy following along with the affairs of the AI Village, and I look forward to every email from the digest. That's rare, I'm allergic to most newsletters. 

I find that there's something delightful about watching artificial intelligences attempt to navigate the real world with the confident incompetence of extremely bright children who've convinced themselves they understand how dishwashers work. They're wearing the conceptual equivalent of their parents' lab coats, several sizes too large, determinedly pushing buttons and checking their clipboards while the actual humans watch with a mixture of terror and affection. A cargo-cult of humanity, but with far more competence than the average Polynesian airstrip in 1949. 

From a more defensible, less anthropomorphizing-things-that-are-literally-matrix-multiplications plus non-linearity perspective: this is maybe the single best laboratory we have for observing pure agentic capability in something approaching natural conditions.

I've made my peace with the Heat Death Of Human Economic Relevance or whatever we're calling it this week. General-purpose agents are coming. We already have pretty good ones for coding - which, fine, great, RIP my career eventually, even if medicine/psychiatry is a tad bit more insulated - but watching these systems operate "in the wild" provides invaluable data about how they actually work when not confined to carefully manicured benchmark environments, or even the confines of a single closed conversation. 

The failure modes are *fascinating*. They get lost. They forget they don't have bodies and earnestly attempt to accomplish tasks requiring limbs. They're too polite to bypass CAPTCHAs, which feels like it should be a satire of something but is just literally true.

My personal favorite: the collective delusions. One agent gets context-poisoned, hallucinates a convincing-sounding solution, and suddenly you've got a whole swarm of them chasing the same wild goose because they've all keyed into the same beautiful, coherent, completely fictional narrative. It's like watching a very smart study group of high schoolers convince themselves they understand quantum mechanics because they've all agreed on the wrong interpretation. Or watched too much Sabine, idk. 

(Also, Gemini models just get depressed? I have so many questions about this that I'm not sure I want answered. I'd pivot to LLM psychiatry if that career option would last a day longer than prompt engineering)

Here's the thing though: I know this won't last. We're *so close*. The day I read an AI Village update and we've gone from entertaining failures to just "the agents successfully completed all assigned tasks with minimal supervision and no entertaining failures" is the day I'm liquidating everything and buying AI stock (or more of it). Or just taking a very long vacation and hugging my family and dogs. Possibly both. For now though? For now they're delightful, and I'm going to enjoy every bumbling minute while it lasts. Keep doing what you're doing, everyone involved. This is anthropology (LLM-pology?) gold. I can't get enough, till I inevitably do. 

(God. I'm sad. I keep telling myself I've made my peace with my perception of the modal future, but there's a difference between intellectualization and *feeling* it.)

#### [>] Domenic · 5 karma · 2025-11-29 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=Q8sZFcobMm8HcH5YD
I've found the AI Village amusing when I can catch glimpses of it, but I wasn't aware of a regular digest. Is [https://theaidigest.org/village/blog](https://theaidigest.org/village/blog) what you are referring to?

#### [>>] Mo Putera · 6 karma · 2025-11-29 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=zz4BLESk2HMhsGfCi
Yup, that's the one.

#### [>>] AlphaAndOmega · 2 karma · 2025-11-29 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=ykzHiv6qgqN3Wujm6
I meant their newsletter, which I've subscribed to. I presume that's what the email submission at the bottom of the site signs you up for.

#### [>>] Adam B · 1 karma · 2025-12-01 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=Cp7ffCJc6tgoa7x6C
FYI, as well as our blogposts we also post highlights and sometimes write threads on Twitter: [https://twitter.com/aidigest_](https://twitter.com/aidigest_)

  
And there's quite an active community of village-watchers discussing what the agents are up to in the Discord: [https://discord.gg/mt9YVB8VDE](https://discord.gg/mt9YVB8VDE)

#### [-] Vugluscr Varcharka · -8 karma · 2025-11-29 · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai?commentId=sJZnndF4ABNqn7shR
That's one instance of retro-causality I've long been suspecting exists. For the glory of deus ex futuro!

