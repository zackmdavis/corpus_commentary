Title: Funk-tunul's Legacy; Or, The Legend of the Extortion War
LessWrong-URL: https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war
Posted: 2019-12-24
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 6 (commentCount field: 6)

#### [-] Zack_M_Davis [AUTHOR] · 2 karma · 2019-12-24 · https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war?commentId=WYjEk5LKx3GccTDXM
**An Author's Note to "Funk-tunul's Legacy"; Or, A Crime That Is Its Own Confession**

This story was inspired by the following three paragraphs Jessica Taylor wrote in an email on 15 April 2019. I didn't actually get permission from Jessica to quote these paragraphs in public, but I _falsifiably predict_ that she won't mind. If she does mind, then she's welcome to _sue me for damages_ in the Court of [Benquo](https://www.lesswrong.com/users/benquo). But if the Court of Benquo awards more than $100 in damages (which I _falsifiably predict_ it won't), then I'm going to strongly consider the hypothesis that the Court is corrupt and maybe become a Benquo-anarchist.

> CDT ends up in a symbiotic relationship with extort-bot, mutually winning relative to agents that don't give in to extortion, until there are none of those left and extort-bot eats the remaining CDTs.
>
> (The scarier variants of extort-bots are those that cooperate with other copies of themselves, a mixture of clique-bot and extort-bot)
>
> The correct strategy for UDTs is to extort CDT, while being strategic about when to give in to or not give in to extortion from extortbots; giving in early on can be necessary to maintain population growth (getting strictly higher growth than CDT), and at the end it's necessary to stop giving in to extort-bot, to ultimately win the war.

#### [-] Zack_M_Davis [AUTHOR] · 4 karma · 2019-12-24 · https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war?commentId=zYoJmyCb5g9T7Jves
**Another Author's Note to "Funk-tunul's Legacy"; Or, A Criminal Confession**

Okay, sorry, the sentence beginning with "It's not obviously possible ..." is bullshit handwaving on my part because the modeling assumptions I chose aren't giving me the result I need to make the story come out the way I want. (Unless I made yet another algebra mistake.) But it's almost half past one in the morning, and I'm _mostly_ pretty happy with this post—you _see the thing I'm getting at_—so I'm pretty eager to shove it out the door and only make it more rigorous later if someone actually cares, because I have a lot of other ideas to write up!

#### [>] Liam Donovan · 12 karma · 2019-12-27 · https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war?commentId=5agiYzktTEknjKBmz
Based on the quote from Jessica Taylor, it seems like the FDT agents are trying to maximize their long-term share of the population, rather than their absolute payoffs in a single generation? If I understand the model correctly, that means the FDT agents should try to maximize the ratio of FDT payoff : 9-bot payoff (to maximize the ratio of FDT:9-bot in the next generation). The algebra then shows that they should refuse to submit to 9-bots once the population of FDT agents gets high enough ([Wolfram|Alpha](https://www.wolframalpha.com/input/?i=%28%289p%2B5q%29%2F%289p%29%29+%3E+%288p%2B4q%2B1%29%2F%289p%2B9q%29%2C+0%3Cp%3C1%2C+0%3Cq%3C1) li[nk](https://www.wolframalpha.com/input/?i=%28%289p%2B5q%29%2F%289p%29%29+%3E+%288p%2B4q%2B1%29%2F%289p%2B9q%29%2C+0%3Cp%3C1%2C+0%3Cq%3C1)), without needing to drop the random encounters assumption.

  

It still seems like CDT agents would behave the same way given the same goals, though?

#### [-] Isnasene · 46 karma · 2019-12-24 · https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war?commentId=suaAzP74S8GhFKNoi
Distinguishing CDT from FDT/TDT in intuitive cases tends to be a lot harder than it looks. And I think it's important to be extremely careful about what we categorize as CDT+being clever versus FDT/TDT. My impression is that this story more often frequently the former.

> At first, the population was composed of a humble race of agents called the ceedeetee. When two of the ceedeetee met each other, each would name the number 5, and receive a payoff of 5, and all was well.

I'm not sure it's obvious that all ceedeetee will meet five when they meet each other.

*   In an environment where there is zero information, this would be true (ie guessing >5 causes the gueesser to get outcompeted by those who will miss fewer payoffs and guessing less causes them to get outcompeted genetically by their partners in the game) but it's clearly not true in this particular context. Instead, it seems more likely that ceedeetrees will o*n-net* guess (and get) five based on whether their analysis of their partner tells them what they can get away with (ie A scares B so B only offers 4 and B offers 6, but B scares C so B offers 6 and C offers 4, but C scares A and so on...). I'd expect an equlibrium that's suboptimal but has cyclical relationships between the participants.
*   Since output from the game determines evolutionary fitness, any ceedeetees who get some payoffs from other sources (ie this guy I just met seems nice but that other guy didn't so I'm gonna give a 4 to this guy and a 6 to the other guy) won't always output five.

These points are *kind of* pedantic but it's importance to notice, if this happens, nine-bots get destroyed. They always guess way too high and the inherent noise in how a population of actual ceedeetee play the game will be hard to recover from.

> Then one day, a simple race of 9-bots invaded the land. The 9-bots would always name the number 9!

Where exactly would we expect the 9-bots to come from? If they were all trapped on a ship together, they would've just continously lost the game until they died Again, this is *kind of* pedantic but, as you point out, the population distributions matter.

> And from that day onward, whenever Funk-tunul met a fellow ceedeetee agent—if "fellow" is the right word here, which it isn't—she would announce that she was going to name 9, and do so. And though the ceedeetee agents' output channels would light up with the standard inidicators of outrage and betrayal, they would reason causally, and name 1.

A very key part of what Funk-tunul is doing here is telling the ceedeetee agents beforehand that she'll say nine. Again, it strikes me that, if a ceeteedee noticed they could cause their partners to guess numbers lower than five, they definitely would do that. Funk-tunul isn't winning because of a better decision theory here; she's winning because she's more clever. at manipulating other ceedeetee.

However, in real life, this implies that Funk-tunul would not be successful. A ceedeetee would've, in the past, tried to credibly show that they always say nine until the population equilibrates to having a defense mechanism against this particular action.

> They reasoned: suppose the fraction of ceedeetee agents in the population is p, the fraction of funk-tunul agents is q, and the fraction of 9-bots is 1−p−q. If we establish a policy of submitting to the 9-bots' extortion, we'll have an average payoff of 9p+5q+1⋅(1−p−q)=8p+4q+1 and the 9-bots will have an average payoff of 9p+9q. If we defy the 9-bots while continuing to extort our ceedeetee cousins, we'll have an average payoff of 9p+5q, whereas the 9-bots will have an average payoff of 9p. Whether it's better to submit or defy depends on the values of p and q. It's not obviously possible for defiance to be the right choice given what we know, but if we can coordinate to meet fellow funk-tunul agents more often—if we drop the assumption of uniform random encounters—the calculus changes ...

This doesn't strike me as acausal reasoning; just long-termist reasoning. Given the (presumably exponential) population dynamics, a ceedeetee could easily predict that letting the nine-bot get nine points would help that nine-bot reproduce more nine-bots. If ceedeetee'rs are in the game to maximize fitness as opposed to utility, they'll definitely establish a norm against helping nine-bots to protect against the exponential cost that nine-bots will have for the future. If they're in the game to maximize their points in the game, this isn't true (they'll just defect against the future) but funk-tunul's reasoning suggests that this isn't what's going on.

> It's not obviously possible for defiance to be the right choice given what we know, but if we can coordinate to meet fellow funk-tunul agents more often—if we drop the assumption of uniform random encounters—the calculus changes ...

If we drop limiting assumptions once funk-tunul agents get involves, it seems pretty clear that the funk-tunul agents will do better than the ceedeetee previously did.

> Before the two agents could name their numbers, Graddes spoke. "Please. *Why are you doing this?*" she pleaded. "I can't hate the 9-bots for their extortion, for they are a simple race and could not do otherwise. But you—we're cousins. Your lineage is a fork of mine. You *know* it's not fair for your people to always name the number 9 when meeting mine. Yet you do so anyway, knowing that we have no choice but to name the number 1 if we want any payoff at all. Why?"

> "Don't hate the player," said Tim'liss, her output channels dimming and brightening in a interpolated pattern one-third of the way between the standard indicators for sympathy and contempt. "Hate life."

We just dropped the random-interaction assumption. Why don't the ceedeetee just only interacting with fellow ceedeetee? Choosing only to interact with ceedeetee would get them waaaaay more points.

Also, this is evidence that the ceedeetee in the game care about stuff beyond just the scores they get in the game and reenforces my point that the events as-described don't really make sense in evolutionary setting. Given this, it's worth pointing out is that the actual thing Tim'liss is doing here is *supporting a race to the bottom that optimizes only reproductive fitness*. Engaging in a race to the bottom for reproductive fitness is Not Good timeless decision theory.

#### [-] Wei Dai · 8 karma · 2019-12-24 · https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war?commentId=8i7S5hbfy527sZmHx
>When a ceedeetee agent met a 9-bot, she would reason causally: “Well, the other agent is going to name 9, so I had better name 1 if I want any payoff at all!”

How does a ceedeetee agent tell what kind of opponent they're facing, and what prevents ceedeetee agents from evolving to or deciding to hide such externally visible differences?

Depending on such details, there are situations where TDT/UDT/FDT seemingly does worse than CDT. See [this example](https://www.lesswrong.com/posts/szfxvS8nsxTgJLBHs/ingredients-of-timeless-decision-theory?commentId=GtyjFvTmx8m6guZGZ) (a variant of 2TDT-1CDT) from cousin\_it:

>Imagine two parallel universes, both containing large populations of TDT agents. In both universes, a child is born, looking exactly like everyone else. The child in universe A is a TDT agent named Alice. The child in universe B is named Bob and has a random mutation that makes him use CDT. Both children go on to play many blind PDs with their neighbors. It looks like Bob’s life will be much happier than Alice’s, right?

More tangentially, the demand game is also one that [UDT 1.x loses to a human](https://www.lesswrong.com/posts/zztyZ4SKy7suZBpbk/another-attempt-to-explain-udt?commentId=3TDhbFNfmyAkFq8XP), because of ["unintentional simulation"](https://www.lesswrong.com/posts/zd2DrbHApWypJD2Rz/udt2-and-against-ud-assa).

#### [-] Dagon · 3 karma · 2019-12-24 · https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war?commentId=EzCiGPBvuqcNoWoJu
Does CDT imply that they can't have a member named Schelling who figures out that it's preferable to freeze out the 9-bots while taking the 5s from cooperators. Pre-commit to 5, problem solved. In any starting mix (with at least 2 of each) of 9-bots and 5-bots, the 5-bots will eventually completely take over, as they're the only ones who ever get any payoff.

If nobody ever says 1, the 9s die pretty quickly.

I don't actually understand whether CDT is so weak as to be a useless strawman that never described any actual agent, or whether the analogies and descriptions we're using are just stupidly ignoring all of game theory and strategy research.

