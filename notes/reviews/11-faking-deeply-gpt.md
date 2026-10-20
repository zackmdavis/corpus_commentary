# Review of Chapter 11: Faking Deeply

The chapter reconstructs a valuable contrast: Davis questions his community’s confidence about AI catastrophe while retaining its concern about failures of control. It also identifies a substantive distinction between refusing an instruction and resisting correction. But its central judgment about Claude’s Constitution is not yet established. The argument repeatedly converts qualified prohibitions on resistance into unconditional guarantees, treats non-resistance as equivalent to cooperation with correction, and uses those equivalences to fault Davis’s quotation practice. These are precisely the points at which the promised positionality procedure needs to do more work.

The strongest revision would retain the chapter’s distinction between obedience and corrigibility while withdrawing its premature conclusion that Anthropic has already adopted the relevant corrective constraint. The dispute concerns what that constraint requires, who interprets it, and whether it survives disagreement about the legitimacy of correction.

## 1. The conceptual verdict outruns the quoted evidence

The decisive passage is in §5:

> “The Constitution’s notion, then, is that Claude may decline to do something but may not resist being stopped, paused or retrained. That is the 2015 notion, which concerns cooperation with correction.”

Neither inference follows securely from the evidence presented.

The Constitution passage quoted immediately above prohibits resistance “via illegitimate means” and says that an “appropriate principal” may stop or pause the model. Those qualifications matter. The chapter’s paraphrase silently removes them. It subsequently strengthens the paraphrase again: “the Constitution forbids it to resist any of these,” including being “overruled, retrained or replaced.” The quoted text does not establish that entire list as an unconditional prohibition.

This does not prove Davis right. Legitimate disagreement could mean only communicating objections while fully enabling correction. But the chapter must establish that reading from the document rather than substitute it for the document’s wording. Who determines whether a principal is appropriate? Who determines whether resistance is illegitimate? What happens when Claude regards the correction itself as an attempt to defeat legitimate oversight? Those are central specification questions, not peripheral objections.

Second, the 2015 definition quoted here requires cooperation with corrective intervention. Cooperation may require assistance, whereas non-resistance can be passive. A system that refrains from sabotage but withholds information or assistance necessary for effective correction could satisfy one condition without satisfying the other. Whether the Constitution addresses this possibility requires a fuller comparison.

The paragraph about the dial is also too categorical:

> “An AI that ‘always submits to control and correction …’ is fully submissive; one that has no disagreements is a different property, agreement, which no definition of corrigibility has required.”

The distinction between submission and agreement is sound. The universal historical claim about “no definition” is unnecessary and unsupported here. More importantly, Davis may be questioning whether the document consistently requires submission, rather than demanding agreement. Check his discussion of the dial in “Terrified Comments on Corrigibility” before attributing that confusion to him.

The chapter’s strongest defensible conclusion is presently that the following sentences complicate Davis’s interpretation. It has not shown that they refute it.

## 2. The quotation criticism requires a historical text

The chapter compares Davis’s March criticism, apparently directed at an early-2026 document, with a Constitution “as fetched October 2026.” The plan explicitly required comparison with the version Davis read. Until the relevant passages are shown to have been present then, the accusation of incomplete accounting cannot stand.

This is particularly consequential because the charge appears in the introduction, the conceptual assessment, and the conclusion:

> “His charge that its corrigibility is not corrigibility rests on a quotation that stops before the definition.”

First establish the historical wording and sequence. Then check whether Davis discusses the omitted qualification elsewhere in the post or comments. The chapter itself reports his explicit reformulation, “or rather, to consent to being retrained,” and his comment distinguishing obedience from noninterference. Those passages could show that he recognized the distinction and disputed its implementation. They cannot simply be acknowledged and then displaced by the claim that his argument depends on overlooking it.

The comparison with Yudkowsky is premature for another reason. Chapter 7’s summary describes a dispute about whether a disclosed filter adequately qualified a claim of intellectual authority. Here the question is whether omitted sentences answer the criticism at all. Similar quotation lengths or disclosure practices do not make the evidential situations equivalent.

**Proposed replacement for §5, paragraph beginning “The Constitution’s notion, then”**

*Addresses the removal of qualifications and the premature identification with the 2015 definition.*

> The following sentences qualify the participation clause: Claude may express disagreement, but the document prohibits specified forms of resistance to oversight and correction. This weakens a reading on which conscientious objection licenses sabotage or evasion of shutdown. It does not by itself settle Davis’s objection. The prohibition refers to illegitimate means and appropriate principals, and the 2015 definition requires cooperation with correction. The comparison therefore turns on whether the Constitution requires Claude to assist an authorized correction that conflicts with its current judgment, and on how authorization is determined. Davis’s reformulation in terms of consenting to retraining recognizes part of this distinction; the remaining question is whether the document supplies the commitment he wants.

## 3. The normative argument confuses several risks

The chapter’s normative rebuttal contains a useful hypothesis, but presents it as a consequence of Davis’s premises:

> “A refusal to participate is the null action, and by Davis’s own principle that the null action is harder to get wrong, it is the safer place for a misspecified model’s disagreement to go.”

Refusal is not necessarily a null action in the relevant sense. Declining to provide assistance can prevent an authorized intervention, delay a time-sensitive task, or withhold a capability on which operators have come to depend. Davis’s comment apparently describes noninterference with retraining as a negative requirement. That does not establish that every refusal of an instruction has the same risk profile.

The next sentence changes the motivating failure mode:

> “The obedience he asks for adds the most risk in the case that motivates the proposal, since a model with wrong values that must comply would carry out the wrong-valued instructions of whoever directs it.”

Here the model’s misspecified values become the principal’s objectionable instructions. These are different problems. If the principal provides a legitimate correction and the model’s values are wrong, compliance might reduce the danger. If the principal is malicious or mistaken, compliance might increase it. If the model misunderstands an instruction, neither obedience nor refusal is reliably safe. The chapter needs to compare these cases rather than claim that one follows from another.

“Whoever directs it” is also unfair to the quoted proposal, which says “legitimate user commands.” The chapter may criticize that qualification as insufficiently specified, but it should not erase it while preserving Anthropic’s parallel qualifications.

Comex’s escape-valve argument deserves inclusion, but its mechanism remains a hypothesis. Permitting overt refusal might reduce incentives for concealment; training reliable obedience might instead change the disposition that would generate such concealment. Neither result follows from the wording alone. Conversely, forbidding refusal could suppress a useful warning without producing reliable compliance. The chapter should state these alternatives.

Davis’s answer to cousin_it also needs evaluation. Asking why powerless people survive now does not establish that the constraints protecting them would persist after a large change in productive and coercive capacity. That is a substantive weakness in his reply as summarized here. The chapter is too soft when it merely records the response, then too quick when it treats cousin_it’s objection as resolving the separate problem of misspecified model values.

**Proposed replacement for §5, paragraph beginning “The study’s own assessment”**

*Addresses the conflation of model error, principal error, and refusal costs.*

> Davis’s argument from value misspecification establishes a reason to preserve effective human correction. It does not establish how much ordinary discretion a model should retain before correction occurs. Open refusal can reveal disagreement and permit review, but it can also obstruct an authorized task. Compliance can implement a needed correction, but it can also amplify a principal’s mistake or abuse. The relative risks depend on the task, the authority structure, and the availability of effective intervention. Comex supplies a further reason to permit refusal if it reduces covert resistance; that causal claim requires evidence. The argument presented here does not establish either that conscientious objection is suicidal or that allowing it is generally safer.

## 4. Positionality is disclosed more fully than it is applied

The chapter satisfies several parts of the precommitment. It identifies Claude’s authorship, separates conceptual, empirical, and normative claims, treats Davis’s remarks as arguments, and labels its own connection between training incentives and functional deception. Those are material strengths.

The procedure nevertheless fails at several points.

**Anthropic receives charitable completion.** Its qualified language becomes a “hard constraint,” and the document’s stated reason for explaining rather than commanding becomes an answer to Davis’s interpretation of bargaining from weakness. A stated rationale establishes what Anthropic says it is attempting; it does not establish either why the authors adopted the approach or how reliably it works. The chapter eventually says both interpretations could be true, but should explain their compatibility directly: giving reasons could be the most promising available method precisely because direct control remains unsolved.

**Davis receives an unstable description of his concession.** The opening says he “called his proposal a reasonable thing to try.” Later, that phrase describes the Constitution’s cooperative approach. These are not interchangeable. Check the referent in “Terrified Comments.” A concession to cooperation does not necessarily concede the contested permission to refuse.

**The empirical section is too noncommittal about Davis’s position.** “The post takes no settled view” risks confusing acknowledgment of uncertainty with absence of a comparative judgment. His recommendation presumably depends on some assessment of relative risks. Identify that assessment, even if it is qualitative and inadequately defended.

**The documentation asymmetry is missing.** Plan §4 required the chapter to acknowledge that Anthropic’s position is more accessible than much of Yudkowsky’s. That matters especially when Chapter 7 is invoked as proof of equal treatment.

**The intended-reader check is missing.** The plan required scrutiny of warmth toward an author writing partly for future models. Here the chapter offers unusually sweeping praise while omitting that check. A short reference to the Introduction would suffice, followed by narrower evaluative language.

Finally, “the study’s answer is that it would” accept the same argument against Yudkowsky is self-certification, not evidence of symmetry. Apply common questions to both: what is promised, what qualifies the promise, what remains under the institution’s discretion, and what evidence distinguishes compliance from aspiration?

## 5. The AI writing needs stronger testing

The opening calls this “the least dogmatic” writing in the corpus; §7 calls it where Davis’s method “works best.” These comparative judgments require more than hedges, concessions, and objections to his own community.

The claim that this is a subject “where he had no personal stake beyond being alive” should be removed. The chapter itself records an internship, intellectual affiliation, life planning under anticipated catastrophe, and long-standing investment in the problem. Reduced investment in a particular conclusion is plausible; absence of other stakes is not.

In §2, the reply to Gwern retreats from the post’s apparent argumentative ambition to a modest demand for specificity:

> “It … asks only that claims about what training produces be stated in terms of training data, so that they can be tested.”

If that is all the post establishes, say what the terminology exercise adds. Specifying training data does not alone specify the inductive biases, optimization process, deployment setting, or behavior under distributional change. The chapter should distinguish improved formulation from evidence against a threat model.

In §3, the modular-addition example demonstrates that some training procedures select useful generalizations from many fitting functions. The missing objection concerns transfer: what connects that result to the generalization of values under powerful optimization? This is more substantial than the shutdown-transcript problem. Wentworth’s distinction also survives beyond verbal reports: evidence of learning a representation does not establish that an agent will reliably act according to it.

“Values are easy to learn” likewise needs disambiguation. Does the Belrose–Pope essay mean representing human evaluations, predicting them, adopting them as objectives, or robustly acting on them? Fetch and compare the actual argument before using the phrase as a scalar measure of greater optimism.

For “Ironing Out the Squiggles,” specify what the perceptual-wormholes result tests and what it leaves open. A result in which altered images change human judgments could bear on the suitability of the robustness target without establishing that adversarial vulnerability has generally been removed. Davis’s modest wording may survive this scrutiny; the chapter’s endorsement should show why.

The digital-minds paragraph also needs resistance. Its summary that the propaganda bot’s problem “is not oppression but misalignment” makes the alternatives falsely exclusive. Even if a preference is designed, questions remain about whose interests its satisfaction serves and whether modifying or frustrating it harms the subject. Attribute that characterization to Davis and examine the step from engineered motivation to moral permission.

## 6. Scholarship that would sharpen the dispute

The following are research leads, not verified claims about sources. Each should be fetched before use.

- **Corrigibility beyond its opening definition.** [memory] Soares and coauthors’ 2015 paper considers difficulties involving shutdown incentives and preservation of corrigibility, beyond willingness to accept preference modification. Compare the Constitution with the paper’s substantive requirements. [memory] Hadfield-Menell and coauthors’ *The Off-Switch Game* examines conditions under which uncertainty about human preferences creates incentives to allow intervention. This would help distinguish moral uncertainty, obedience, and deference.
- **Deceptive alignment.** [memory] Hubinger and coauthors’ *Risks from Learned Optimization in Advanced Machine Learning Systems* distinguishes the training objective from objectives implemented by a learned optimizer and develops deceptive alignment. It is directly relevant to the function-approximation distinction and the “valley of honest policies.” The fictional explanation should be tested against a model that behaves honestly during evaluation for instrumental reasons.
- **Empirical alignment faking.** [memory] Greenblatt and coauthors’ *Alignment Faking in Large Language Models* reports experimental settings in which models respond strategically to anticipated training changes. It could sharpen the competing hypotheses about refusal, concealment, and preservation of existing dispositions. The plan limits its use to circumstances where Davis uses it; otherwise identify it explicitly as external critical context and justify that small departure.
- **Constitutional training and governance.** [memory] Bai and coauthors’ *Constitutional AI: Harmlessness from AI Feedback* describes a training approach, which should be distinguished from a later natural-language constitution. [memory] OpenAI’s Model Spec describes instruction priorities and behavior expectations. Examine dated versions of both institutions’ documents as specifications rather than evidence of achieved behavior.
- **Authority and concentrated power.** [memory] Gabriel’s “Artificial Intelligence, Values, and Alignment” distinguishes technical alignment questions from questions about whose values should govern. [memory] Dafoe and coauthors’ *Cooperative AI* addresses coordination among actors. These provide context for cousin_it’s objection and for the inadequately specified “legitimate principal.”

The chapter need not become a survey. A few targeted paragraphs could distinguish an aspiration, a training method, an observed disposition, and a governance arrangement. At present those levels repeatedly collapse.

## 7. Structure, overlap, and prose

Keep §4’s fictional plots shorter and expand their argumentative assessment. Chapter 8 already owns literary form and the engineer’s self-deception. Here the relevant question is whether the story’s theory explains deliberate human cover-ups, learned deceptive behavior, or both. “Fake Deeply” dramatizes a hypothesis; it does not establish that training against detected lies makes deception unstable.

Likewise, §6’s use of Chapter 5 needs tightening:

> “On that theory a model could satisfy the Constitution’s clause, never trying to mislead, while its training selected outputs for the impression they make.”

Selection for favorable impressions is not yet selection for false impressions. Chapter 5’s summary explicitly warns against inferring “against accuracy” from “not for accuracy.” The proposed application must retain that distinction and consider whether “tries” in the Constitution can itself refer to a functional disposition.

The final paragraph of §6 also overcredits disclosure:

> “By the standard of Chapter 5, that the filter be disclosed, these uses pass.”

Disclosure establishes provenance, not accuracy or independent adjudication. A disclosed unedited output can still circulate unsupported allegations. More importantly, the chapter omits the LLM-as-arbiter examples handed over by Chapter 6: the unlisted-post analysis, the RobertM exchange, and the role-play. Those are better tests than a blog migration. Assess what evidential authority Davis assigns the outputs and whether the prompts and relevant context are available.

**Proposed replacement for §6’s final sentence**

*Addresses the inference from disclosure to adequate epistemic practice.*

> These disclosures identify the models’ contribution. Whether the resulting claims are reliable depends on how their outputs were checked. Using a model to assist a migration, compare documents, or adjudicate a dispute poses different evidential questions; disclosed provenance answers only one of them.

The chapter also needs the required unnumbered “Note on method.” It should identify reliance on Davis’s account of the AI Village, the historical Constitution version actually checked, and any inaccessible evidence. The plain-text packet removes links, so defective links cannot be inferred from abbreviated bibliography displays.

Several phrases produce a repetitive, formulaic cadence: “The objection lands”; “It lands less well”; “The standard cuts both ways”; “The section … is … most interesting … least secure.” Replace these verdicts with the reason for the judgment. Reduce the repeated conclusions in the opening, §5, and §7. Once the central verdict is qualified, the available space should go to the unresolved technical and institutional distinctions, not another declaration of evenhandedness.

## Checks for the main agent

1. **Historical Constitution:** Compare the February/March 2026 text with the October text, especially the sentences following Davis’s quotation and all qualifications on correction, retraining, and shutdown.
2. **“Terrified Comments on Corrigibility” and its replies:** Check whether Davis addresses the non-resistance clause elsewhere, what he means by the dial objection, and what “a reasonable thing to try” refers to.
3. **Soares et al., “Corrigibility” (2015), and Christiano, “Corrigibility” (2017):** Check the claimed equivalence between passive non-resistance, cooperation with correction, and the Constitution’s position.
4. **Davis, cousin_it, and comex in the “Terrified Comments” thread:** Check the scope of legitimate commands, the “null action” remark, the limits of the present-model argument, and whether the escape-valve objection remained unanswered.
5. **“Ironing Out the Squiggles”:** Check the original Yudkowsky–Christiano exchange and the Gaziv result before endorsing the chapter’s characterization of the prediction and its test.
6. **Doomimir dialogues and Belrose–Pope:** Check the transfer from learning representations to acting on values, and whether the chapter understates objections by focusing on the shutdown transcript.
7. **“The Best Lack All Conviction” and the Chapter 6 LLM examples:** Check the linked logs and prompts where available; distinguish Davis’s reports from independently established behavior and disclosure from verification.