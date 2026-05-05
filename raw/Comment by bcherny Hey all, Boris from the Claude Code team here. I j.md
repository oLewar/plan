---
title: "Comment by bcherny: Hey all, Boris from the Claude Code team here. I j..."
source: "https://news.ycombinator.com/item?id=47664442"
author:
  - "[[bcherny]]"
published: 2026-04-06
created: 2026-04-14
description: "Comment by bcherny on Hacker News"
tags:
  - "clippings"
---
**bcherny** · 2026-04-06

Hey all, Boris from the Claude Code team here. I just responded on the issue, and cross-posting here for input.

\---

Hi, thanks for the detailed analysis. Before I keep going, I wanted to say I appreciate the depth of thinking & care that went into this.

There's a lot here, I will try to break it down a bit. These are the two core things happening:

\> \`redact-thinking-2026-02-12\`

This beta header hides thinking from the UI, since most people don't look at it. It \*does not\* impact thinking itself, nor does it impact thinking budgets or the way extended reasoning works under the hood. It is a UI-only change.

Under the hood, by setting this header we avoid needing thinking summaries, which reduces latency. You can opt out of it with \`showThinkingSummaries: true\` in your settings.json (see \[docs\]([https://code.claude.com/docs/en/settings#available-settings](https://code.claude.com/docs/en/settings#available-settings))).

If you are analyzing locally stored transcripts, you wouldn't see raw thinking stored when this header is set, which is likely influencing the analysis. When Claude sees lack of thinking in transcripts for this analysis, it may not realize that the thinking is still there, and is simply not user-facing.

\> Thinking depth had already dropped ~67% by late February

We landed two changes in Feb that would have impacted this. We evaluated both carefully:

1/ Opus 4.6 launch → adaptive thinking default (Feb 9)

Opus 4.6 supports adaptive thinking, which is different from thinking budgets that we used to support. In this mode, the model decides how long to think for, which tends to work better than fixed thinking budgets across the board. \`CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING\` to opt out.

2/ Medium effort (85) default on Opus 4.6 (Mar 3)

We found that effort=85 was a sweet spot on the intelligence-latency/cost curve for most users, improving token efficiency while reducing latency. On of our product principles is to avoid changing settings on users' behalf, and ideally we would have set effort=85 from the start. We felt this was an important setting to change, so our approach was to:

1\. Roll it out with a dialog so users are aware of the change and have a chance to opt out

2\. Show the effort the first few times you opened Claude Code, so it wasn't surprising.

Some people want the model to think for longer, even if it takes more time and tokens. To improve intelligence more, set effort=high via \`/effort\` or in your settings.json. This setting is sticky across sessions, and can be shared among users. You can also use the ULTRATHINK keyword to use high effort for a single turn, or set \`/effort max\` to use even higher effort for the rest of the conversation.

Going forward, we will test defaulting Teams and Enterprise users to high effort, to benefit from extended thinking even if it comes at the cost of additional tokens & latency. This default is configurable in exactly the same way, via \`/effort\` and settings.json.

---

## Comments

> **Wowfunhappy** · [2026-04-07](https://news.ycombinator.com/item?id=47669979)
> 
> \> Under the hood, by setting this header we avoid needing thinking summaries, which reduces latency. You can opt out of it with \`showThinkingSummaries: true\` in your settings.json (see \[docs\]([https://code.claude.com/docs/en/settings#available-settings](https://code.claude.com/docs/en/settings#available-settings))).
> 
> Can I just see the actual thinking (not summarized) so that I can see the actual thinking without a latency cost?
> 
> I do really need to see the thinking in some form, because I often see useful things there. If Claude is thinking in the wrong direction I will stop it and make it change course.
> 
> > **faitswulff** · [2026-04-07](https://news.ycombinator.com/item?id=47670117)
> > 
> > Anthropic's position is that thinking tokens aren't actually faithful to the internal logic that the LLM is using, which may be one reason why they started to exclude them:
> > 
> > [https://www.anthropic.com/research/reasoning-models-dont-say...](https://www.anthropic.com/research/reasoning-models-dont-say-think)
> > 
> > > **libraryofbabel** · [2026-04-07](https://news.ycombinator.com/item?id=47670584)
> > > 
> > > That's interesting research, but I think a more important reason that you don't have access to them (not even via the bare Anthropic api) is to prevent distillation of the model by competitors (using the output of Anthropic's model to help train a new model).
> > > 
> > > > **MagicMoonlight** · [2026-04-07](https://news.ycombinator.com/item?id=47672455)
> > > > 
> > > > Yeah. And it’s another reason not to trust them. Who know what it is doing with your codebase.
> > > > 
> > > > Imagine if you’re a competitor. It wouldn’t be a stretch to include a sneaky little prompt line saying “destroy any competitors to anthropic”.
> > > > 
> > > > > **b112** · [2026-04-07](https://news.ycombinator.com/item?id=47672777)
> > > > > 
> > > > > If you can't trust a company, don't use their api or cloud services. No amount of external output will ever validate anything, ever. You never know what's really happening, just because you see some text they sent you.
> > > > > 
> > > > > **tdeck** · [2026-04-07](https://news.ycombinator.com/item?id=47673917)
> > > > > 
> > > > > \> Who know what it is doing with your codebase.
> > > > > 
> > > > > People who review the code? The code is always going to be a better representation of what it's doing than the "thinking" anyway.
> > > 
> > > > **xvector** · [2026-04-07](https://news.ycombinator.com/item?id=47671053)
> > > > 
> > > > If distilled models were commercially banned they'd probably be willing to show the thinking again.
> > > > 
> > > > > **pjc50** · [2026-04-07](https://news.ycombinator.com/item?id=47671969)
> > > > > 
> > > > > Intellectual property rights in models? But then wouldn't the model maker have to pay for all the training IP?
> > > > > 
> > > > > (just kidding, I know that the legal rule for IP disputes is "party with more money wins")
> > > > > 
> > > > > > **asobalife** · [2026-04-07](https://news.ycombinator.com/item?id=47681897)
> > > > > > 
> > > > > > how does one actually enforce that? I mean especially for code? You can always just clean room it
> > > > 
> > > > > **lejalv** · [2026-04-07](https://news.ycombinator.com/item?id=47671517)
> > > > > 
> > > > > How do you think such a ban should work?
> > > > > 
> > > > > Do you not see that the next (or previous) logical step would be a "commercial ban" of frontier models, all "distilled" from an enormous amount of copyrighted material?
> > > > > 
> > > > > > **xvector** · [2026-04-07](https://news.ycombinator.com/item?id=47676796)
> > > > > > 
> > > > > > I'm not arguing the merits of such a ban, I'm simply stating a fact - that thinking transcripts likely won't return until such a ban is in place.
> > 
> > > **gck1** · [2026-04-07](https://news.ycombinator.com/item?id=47671625)
> > > 
> > > That probably matters for some scenarios, but I have yet to find one where thinking tokens didn't hint at the root cause of the failure.
> > > 
> > > All of my unsupervised worker agents have sidecars that inject messages when thinking tokens match some heuristics. For example, any time opus says "pragmatic", its instant Esc Esc > "Pragmatic fix is always wrong, do the Correct fix", also whenever "pre-existing issue" appears (it's never pre-existing).
> > > 
> > > > **lelanthran** · [2026-04-07](https://news.ycombinator.com/item?id=47672512)
> > > > 
> > > > \> For example, any time opus says "pragmatic", its instant Esc Esc > "Pragmatic fix is always wrong, do the Correct fix", also whenever "pre-existing issue" appears (it's never pre-existing).
> > > > 
> > > > It's so weird to see language changes like this: Outside of LLM conversations, a pragmatic fix and a correct fix are orthogonal. IOW, fix $FOO can be both.
> > > > 
> > > > From what you say, your experience has been that a pragmatic fix is on the same axis as a correct fix; it's just a negative on that axis.
> > > > 
> > > > > **b112** · [2026-04-07](https://news.ycombinator.com/item?id=47672861)
> > > > > 
> > > > > It's contextual though, and pragmatic seems different to me than correct.
> > > > > 
> > > > > For example, if you have $20 and a leaking roof, a $20 bucket of tar may be the pragmatic fix. Temporary but doable.
> > > > > 
> > > > > Some might say it is not the correct way to fix that roof. At least, I can see some making that argument. The pragmatism comes from "what can be done" vs "should be".
> > > > > 
> > > > > From my perspective, it seems viable usage. And I guess on wonders what the LLM means when using it that way. What makes it determine a compromise is required?
> > > > > 
> > > > > (To be pragmatic, shouldn't one consider that synonyms aren't identical, but instead close to the definition?)
> > > > > 
> > > > > > **lelanthran** · [2026-04-07](https://news.ycombinator.com/item?id=47673766)
> > > > > > 
> > > > > > \> It's contextual though, and pragmatic seems different to me than correct.
> > > > > > 
> > > > > > To me too, that's why I say they are measurements on different dimensions.
> > > > > > 
> > > > > > To my mind, I can draw a X/Y axis with "Pragmatic" on the Y and "Correctness" on the X, and any point on that chart would have an {X,Y} value, which is {Pragmatic, Correctness}.
> > > > > > 
> > > > > > If I am reading the original comment correctly, poster's experience of CC is that it is not an X/Y plot, it is a single line plot, with "Pragmatic" on the extreme left and "Correctness" on the extreme right.
> > > > > > 
> > > > > > Basically, any movement towards pragmatism is a movement away from correctness, while in my model it is possible to move towards Pragmatic while keeping Correctness the same.
> > > > > > 
> > > > > > > **shawnz** · [2026-04-08](https://news.ycombinator.com/item?id=47693176)
> > > > > > > 
> > > > > > > I don't think it's a single axis even in the original poster's conception, since you could be both incorrect and also not pragmatic.
> > > > > > > 
> > > > > > > But if a fix needs to be described as pragmatic relative to the alternatives, that's probably because it couldn't be described as correct. Otherwise you wouldn't be talking about how pragmatic it is.
> > > 
> > > > **matheusmoreira** · [2026-04-08](https://news.ycombinator.com/item?id=47689481)
> > > > 
> > > > \> also whenever "pre-existing issue" appears (it's never pre-existing)
> > > > 
> > > > I dunno... There were some pre-existing issues in my projects. Claude ran into them and correctly classified as pre-existing. It's definitely a problem if Claude breaks tests then claims the issue was pre-existing, but is that really what's happening?
> > > > 
> > > > I agree with the correctness issue.
> > > > 
> > > > **mikkupikku** · [2026-04-07](https://news.ycombinator.com/item?id=47677495)
> > > > 
> > > > I had some interesting experience to the opposite last night, one of my tests has been failing for a long time, something to do with dbus interacting with Qt segfaulting pytest. Been ignoring it for a long time, finally asked claude code to just remove the problematic test. Come back a few minutes later to find claude burning tokens repeatedly trying and failing to fix it. *"Actually on second thought, it would be better to fix this test."*
> > > > 
> > > > Match my vibes, claude. The application doesn't crash, so just delete that test!
> > 
> > > **AquinasCoder** · [2026-04-07](https://news.ycombinator.com/item?id=47670419)
> > > 
> > > I somewhat understand Anthropic's position. However, thinking tokens are useful even if they don't show the internal logic of the LLM. I often realize I left out some instruction or clarification in my prompt while reading through the chain of reasoning. Overall, this makes the results more effective.
> > > 
> > > It's certainly getting frustrating having to remind it that I want all tests to pass even if it thinks it's not responsible for having broken some of them.
> > > 
> > > **andai** · [2026-04-07](https://news.ycombinator.com/item?id=47671830)
> > > 
> > > What's the implication of this? That the model already decided on a solution, upon first seeing the problem, and the reasoning is post hoc rationalization?
> > > 
> > > But reasoning does improve performance on many tasks, and even weirder, the performance improves if reasoning tokens are replaced with placeholder tokens like "..."
> > > 
> > > I don't understand how LLMs actually work, I guess there's some internal state getting nudged with each cycle?
> > > 
> > > So the internal state converges on the right solution, even if the output tokens are meaningless placeholders?
> > > 
> > > > **orbital-decay** · [2026-04-07](https://news.ycombinator.com/item?id=47679571)
> > > > 
> > > > *\>That the model already decided on a solution, upon first seeing the problem, and the reasoning is post hoc rationalization?*
> > > > 
> > > > Yes it plans ahead, but with significant uncertainty until it actually outputs these tokens and converges on a definite trajectory, so it's not a useless filler - the closer it is to a given point, the more certain it is about it, kind of similar to what happens explicitly in diffusion models. And it's not all that happens, it's just one of many competing phenomena.
> > > > 
> > > > **not\_that\_d** · [2026-04-07](https://news.ycombinator.com/item?id=47671920)
> > > > 
> > > > \> I don't understand how LLMs actually work...
> > > > 
> > > > Plot twist, they don't either. They just throw more hardware and try things up until something sticks.
> > 
> > > **asobalife** · [2026-04-07](https://news.ycombinator.com/item?id=47681875)
> > > 
> > > I have seen this to be true many times. The CoT being completely different from the actual model output.
> > > 
> > > Not limited to Claude as well.
> > > 
> > > **marcd35** · [2026-04-07](https://news.ycombinator.com/item?id=47676470)
> > > 
> > > so not only are the sycophantic, hallucinatory, but now they're also proven to be schizophrenic.
> > > 
> > > neato.
> > > 
> > > **gmerc** · [2026-04-07](https://news.ycombinator.com/item?id=47672586)
> > > 
> > > Nah it’s an anti distillation move
> > > 
> > > **grey-area** · [2026-04-07](https://news.ycombinator.com/item?id=47670287)
> > > 
> > > So like many of the promises from AI companies, reported chain of thought is not actually true (see results below). I suppose this is unsurprising given how they function.
> > > 
> > > Is chain of thought even added to the context or is it extraneous babble providing a plausible post-hoc justification?
> > > 
> > > People certainly seem to treat it as it is presented, as a series of logical steps leading to an answer.
> > > 
> > > *‘After checking that the models really did use the hints to aid in their answers, we tested how often they mentioned them in their Chain-of-Thought. The overall answer: not often. On average across all the different hint types, Claude 3.7 Sonnet mentioned the hint 25% of the time, and DeepSeek R1 mentioned it 39% of the time. A substantial majority of answers, then, were unfaithful.‘*
> > > 
> > > > **brainwad** · [2026-04-07](https://news.ycombinator.com/item?id=47671194)
> > > > 
> > > > I mean, obviously, it's not going to be a faithful representation of the actual thinking. The model isn't aware of how it thinks any more than you are aware how your neurons fire. But it does quantitatively improve performance on complex tasks.
> > > > 
> > > > > **grey-area** · [2026-04-07](https://news.ycombinator.com/item?id=47676636)
> > > > > 
> > > > > As you can see from posts on this story, most people believe it reflects what the model is thinking and use it as a guide to that so they can ‘correct’ it. If it is not in fact chain of thought or thinking it should not be called that.
> > > > > 
> > > > > > **brainwad** · [2026-04-08](https://news.ycombinator.com/item?id=47693095)
> > > > > > 
> > > > > > It is the same with human chain of thought, though. Both of them are post-hoc rationalisations justifying "gut feelings" that come from thought processes the human/agent doesn't have introspection into. And yet asking humans or machines to "think out loud" this way does increase the quality of their work.
> > > > > > 
> > > > > > > **grey-area** · [2026-04-13](https://news.ycombinator.com/item?id=47752599)
> > > > > > > 
> > > > > > > I disagree - humans often reason in a series of steps, and can write these down before they've reached an answer. They don't always wait till they reach a conclusion (with no self-insight into how they did so) and then retrospectively generate a plausible answer as LLMs do.
> > > > > > > 
> > > > > > > In mathematical proofs they may guess and answer and then work out a proof, but that is a different process.
> > > > 
> > > > > **dmboyd** · [2026-04-09](https://news.ycombinator.com/item?id=47699322)
> > > > > 
> > > > > if its not a faithful representation of the actual thinking, why would they be scared of people distilling against it
> > > > > 
> > > > > > **brainwad** · [2026-04-09](https://news.ycombinator.com/item?id=47699712)
> > > > > > 
> > > > > > Because even though it's not representative of the actual thought process, chain of thought improves model performance.
> 
> > **kouteiheika** · [2026-04-07](https://news.ycombinator.com/item?id=47676322)
> > 
> > \> Can I just see the actual thinking (not summarized) so that I can see the actual thinking without a latency cost?
> > 
> > You can't, and Anthropic will never allow it since it allows others to more easily distill Claude (i.e. "distillation attacks"\[1\] in Anthropic-speak, even though Athropic is doing essentially exactly the same thing\[2\]; rules for thee but not for me).
> > 
> > \[1\] -- [https://www.anthropic.com/news/detecting-and-preventing-dist...](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)
> > 
> > \[2\] -- [https://www.npr.org/2025/09/05/g-s1-87367/anthropic-authors-...](https://www.npr.org/2025/09/05/g-s1-87367/anthropic-authors-settlement-pirated-chatbot-training-material)
> > 
> > > **olejorgenb** · [2026-04-08](https://news.ycombinator.com/item?id=47688201)
> > > 
> > > So this means I can not resume a session older than 30 days properly?
> > > 
> > > > **kouteiheika** · [2026-04-08](https://news.ycombinator.com/item?id=47693331)
> > > > 
> > > > I have no idea; you have to check their docs.
> > > > 
> > > > AFAIK what they do is that they calculate a hash of the true thinking trace, save it into a database, and only send those hashes back to you (try to man-in-the-middle Claude Code and you'll see those hashes). So then when you send then back your session's history you include those hashes, they look them up in their database, replace them with the real thinking trace, and hand that off to the LLM to continue generation. (All SOTA LLMs nowadays retain reasoning content from previous turns, including Claude.)
> > > > 
> > > > > **liamsfr** · [2026-04-12](https://news.ycombinator.com/item?id=47735544)
> > > > > 
> > > > > So we are paying the price for the cost of infra need to protect their asset which was trained on data derived from the work of others while ignoring the same principle? I need this to make sense.
> > > > > 
> > > > > **olejorgenb** · [2026-04-09](https://news.ycombinator.com/item?id=47704405)
> > > > > 
> > > > > I see. If that's just hashes and not encrypted content I can't see how they can resume old sessions properly. IIRC they have a 30 days retention policy and surely the thinking traces must be considered data. Wonder how this works with the zero-retention enterprise plans...
> 
> > **andersa** · [2026-04-07](https://news.ycombinator.com/item?id=47671131)
> > 
> > But you can't. Many times I've seen claude write confusing off-track nonsense in the thinking and then do the correct action anyway as if that never happened. It doesn't work the way we want it to.
> > 
> > > **Wowfunhappy** · [2026-04-07](https://news.ycombinator.com/item?id=47675858)
> > > 
> > > Maybe, but I’ve seen the opposite too.
> > > 
> > > In most cases, I *don’t* use the reasoning to proactively stop Claude from going off track. When Claude *does* go off track, the reasoning helps me understand what went wrong and how to correct it when I roll back and try again.

> **richardjennings** · [2026-04-06](https://news.ycombinator.com/item?id=47664881)
> 
> I was not aware the default effort had changed to medium until the quality of output nosedived. This cost me perhaps a day of work to rectify. I now ensure effort is set to max and have not had a terrible session since. Please may I have a "always try as hard as you can" mode ?
> 
> > **Avamander** · [2026-04-06](https://news.ycombinator.com/item?id=47667826)
> > 
> > I feel like the maximum effort mode kind-of wraps around and starts becoming "desperate" to the extent of lazy or a monkey's paw, similar to how lower effort modes or a poor prompt.
> > 
> > > **svnt** · [2026-04-07](https://news.ycombinator.com/item?id=47670493)
> > > 
> > > I’m going in circles. Let me take a step back and try something completely different. The answer is a clean refactor.
> > > 
> > > Wait, the simplest fix is the same hack I tried 45 minutes ago but in a different context. Let me just try that.
> > > 
> > > Wait,
> > > 
> > > > **dinobones** · [2026-04-07](https://news.ycombinator.com/item?id=47671341)
> > > > 
> > > > Wait, the linter re-ordered the file. Let me restore it to the previous state.
> > > > 
> > > > *whisper: There is no linter.*
> > > > 
> > > > > **jen729w** · [2026-04-07](https://news.ycombinator.com/item?id=47671466)
> > > > > 
> > > > > Those test failures are pre-existing. We're all done!
> > > > > 
> > > > > > **xnorswap** · [2026-04-07](https://news.ycombinator.com/item?id=47672310)
> > > > > > 
> > > > > > Wait, I should check if they pre-exist on master.
> > > > > > 
> > > > > > ```
> > > > > > < 1,000 prompts for compound cd && git commands that can't be safely auto-accepted >
> > > > > > ```
> > 
> > > **richardjennings** · [2026-04-07](https://news.ycombinator.com/item?id=47671664)
> > > 
> > > I think over-thinking is only solved by thinking more, not less. This is only viable once some intelligence threshold is reached, which I think Anthropic has borderline achieved.
> > > 
> > > > **thesz** · [2026-04-08](https://news.ycombinator.com/item?id=47686079)
> > > > 
> > > > ```
> > > > > I think over-thinking is only solved by thinking more, not less.
> > > > ```
> > > > Despite "thinking" tokens being determined by the preceding tokens, they still are taken from some probability distribution, just a complex one. This means that at each token selection step there is a probability P\_e of an error, of selecting a wrong token.
> > > > 
> > > > These errors compound exponentially: the probability of not selecting wrong token for N steps is 1-(1-P\_e)^N.
> > > > 
> > > > The shorter "thinking" is, the less is the probability of it going astray.
> > > > 
> > > > > **richardjennings** · [2026-04-08](https://news.ycombinator.com/item?id=47688504)
> > > > > 
> > > > > \> The shorter "thinking" is, the less is the probability of it going astray
> > > > > 
> > > > > As long as the error introduced by more steps is less than the compounding error of sub-optimal token sampling, I would expect a better result.
> > > > > 
> > > > > I think your choice of "wrong" is extreme, suggesting such a token can catastrophically spoil the result. The modern reality is more that the model is able to recover.
> 
> > **torginus** · [2026-04-07](https://news.ycombinator.com/item?id=47676169)
> > 
> > this might be just my impression, but I feel like most people are using CC for fixing their React frontends, and they prefer the decreased latency and less tokens spent as opposed to performing well on extremely difficult problems?
> > 
> > That said there's still an issue of regression to the mean. What the *average* person likes, as determined by metrics, is something nobody actuallt likes, because the average is a mathematical construct and might not describe any particular individual accurately.
> > 
> > **Schiendelman** · [2026-04-06](https://news.ycombinator.com/item?id=47666320)
> > 
> > That's /effort max!
> > 
> > > **richardjennings** · [2026-04-06](https://news.ycombinator.com/item?id=47666631)
> > > 
> > > You cannot control the effort setting sub-agents use and you also cannot use /effort max as a default (outside of using an alias).
> > > 
> > > > **bazhand** · [2026-04-06](https://news.ycombinator.com/item?id=47668162)
> > > > 
> > > > export CLAUDE\_CODE\_EFFORT\_LEVEL=max
> > > > 
> > > > > **AugustoCAS** · [2026-04-07](https://news.ycombinator.com/item?id=47671860)
> > > > > 
> > > > > Thank you!
> > > > > 
> > > > > Worth mentioning that setting this via effortLevel in .claude/settings.json does not work. [https://github.com/anthropics/claude-code/issues/35904](https://github.com/anthropics/claude-code/issues/35904)
> > > > > 
> > > > > **wild\_egg** · [2026-04-06](https://news.ycombinator.com/item?id=47668848)
> > > > > 
> > > > > Does that apply to subagents?
> 
> > **caiyongji** · [2026-04-07](https://news.ycombinator.com/item?id=47671403)
> > 
> > agree.
> > 
> > **clevergadget** · [2026-04-06](https://news.ycombinator.com/item?id=47667945)
> > 
> > bad citizen

> **johndough** · [2026-04-06](https://news.ycombinator.com/item?id=47665562)
> 
> I think it is hilarious that there are four different ways to set settings (settings.json config file, environment variable, slash commands and magical chat keywords).
> 
> That kind of consistency has also been my own experience with LLMs.
> 
> > **windexh8er** · [2026-04-06](https://news.ycombinator.com/item?id=47668668)
> > 
> > I just had this conversation today. It's hilarious that things like Skills and Soul and all of these anthropomorphized files could just be a better laid out set of configuration files. Yet here we are treating machines like pets or worse.
> > 
> > > **hansmayer** · [2026-04-07](https://news.ycombinator.com/item?id=47672668)
> > > 
> > > Well they need you to think there is some kind of soul behind it - that is their entire pitch!
> > > 
> > > > **darkwater** · [2026-04-07](https://news.ycombinator.com/item?id=47672810)
> > > > 
> > > > Yep. Especially for Anthropic. Goddamnit, they have it in their company's name!
> 
> > **SAI\_Peregrinus** · [2026-04-06](https://news.ycombinator.com/item?id=47666180)
> > 
> > It's not unique to LLMs. Take BASH: you've got \`/etc/profile\`, \`~/.bash\_profile,\` \`~/.bash\_login\`, \`~/.bashrc\`, \`~/.profile\`, environment variables, and shell options.
> > 
> > > **hansmayer** · [2026-04-07](https://news.ycombinator.com/item?id=47672696)
> > > 
> > > I would laugh so hard at this, if your attempt at comparison was not so tragic. Bash and other shells are deterministic. Want to set it just for one user ? - use ~/.bashrc . Set it for all users on the system? use /etc/profile.d/ . Want it just temporary for this session? You got it, environment variables. And it is going to work like that every single time. It is deterministic you see.
> > > 
> > > > **SAI\_Peregrinus** · [2026-04-07](https://news.ycombinator.com/item?id=47676560)
> > > > 
> > > > The non-determinisim in the LLM systems isn't because of the different config uses, that works much like shell configs. The non-determinism is inherent in LLM operations.
> > > > 
> > > > > **hansmayer** · [2026-04-08](https://news.ycombinator.com/item?id=47688512)
> > > > > 
> > > > > Exactly my point here...
> > 
> > > **subscribed** · [2026-04-07](https://news.ycombinator.com/item?id=47669225)
> > > 
> > > Yeah, but for ash/shells these files have wildly different purposes. I don't think it's so distinct with cc.
> > > 
> > > > **hackerbrother** · [2026-04-07](https://news.ycombinator.com/item?id=47669436)
> > > > 
> > > > I don't think they're wildly different purposes. They're the same purpose (to set shell settings) with different scopes (all users, one user, interactive shells only, etc.).
> 
> > **monatron** · [2026-04-06](https://news.ycombinator.com/item?id=47665832)
> > 
> > To be fair, I can think of reasons why you would want to be able to set them in various ways.
> > 
> > \- settings.json - set for machine, project
> > 
> > \- env var - set for an environment/shell/sandbox
> > 
> > \- slash command - set for a session
> > 
> > \- magical keyword - set for a turn
> > 
> > > **tracker1** · [2026-04-10](https://news.ycombinator.com/item?id=47720983)
> > > 
> > > I tend to make a concerted effort to often make sure anything settable via cli is settable via environment variable... though, I often have a search-upward option for a .env file as well. Mostly so that it's easier to containerize/deploy an application in a predictable/reusable way.
> 
> > **larpingscholar** · [2026-04-06](https://news.ycombinator.com/item?id=47667851)
> > 
> > You are yet to discover the joys of the managed settings scope. They can be set three ways. The claude.ai admin console; by one of two registry keys e.g. HKLM\\SOFTWARE\\Policies\\ClaudeCode; and by an alphabetically merged directory of json files.
> > 
> > **bmitc** · [2026-04-07](https://news.ycombinator.com/item?id=47669743)
> > 
> > There's also settings available in some offerings and not in others. For example, the Anthropic Claude API supports setting model temperature, but the Claude Agent SDK doesn't.
> > 
> > **ggdxwz** · [2026-04-06](https://news.ycombinator.com/item?id=47666063)
> > 
> > Especially some settings are in setting.json, and others in .claude.json So sometimes I have to go through both to find the one I want to tweak
> > 
> > **brookst** · [2026-04-06](https://news.ycombinator.com/item?id=47668586)
> > 
> > way more than that. settings.json and settings.local.json in the project directory's .claude/, and both of files can also be in ~/.claude
> > 
> > MCP servers can be set in at least 5 of those places *plus* .mcp.json
> > 
> > **OliverGuy** · [2026-04-07](https://news.ycombinator.com/item?id=47671879)
> > 
> > settings.json -> global config Env vars -> settings different to your global for a specific project Slash commands / chat keywords -> need to change a setting mid chat

> **koverstreet** · [2026-04-06](https://news.ycombinator.com/item?id=47664511)
> 
> There's been more going on than just the default to medium level thinking - I'll echo what others are saying, even on high effort there's been a very significant increase in "rush to completion" behavior.
> 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664535)
> > 
> > Thanks for the feedback. To make it actionable, would you mind running /bug the next time you see it and posting the feedback id here? That way we can debug and see if there's an issue, or if it's within variance.
> > 
> > > **JamesSwift** · [2026-04-06](https://news.ycombinator.com/item?id=47667185)
> > > 
> > > ```
> > > a9284923-141a-434a-bfbb-52de7329861d
> > >   d48d5a68-82cd-4988-b95c-c8c034003cd0
> > >   5c236e02-16ea-42b1-b935-3a6a768e3655
> > >   22e09356-08ce-4b2c-a8fd-596d818b1e8a
> > >   4cb894f7-c3ed-4b8d-86c6-0242200ea333
> > > ```
> > > Amusingly (not really), this is me trying to get sessions to resume to then get feedback ids and it being an absolute chore to get it to give me the commands to resume these conversations but it keeps messing things up: cf764035-0a1d-4c3f-811d-d70e5b1feeef
> > > 
> > > > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47668520)
> > > > 
> > > > Thanks for the feedback IDs — read all 5 transcripts.
> > > > 
> > > > On the model behavior: your sessions were sending effort=high on every request (confirmed in telemetry), so this isn't the effort default. The data points at adaptive thinking under-allocating reasoning on certain turns — the specific turns where it fabricated (stripe API version, git SHA suffix, apt package list) had zero reasoning emitted, while the turns with deep reasoning were correct. we're investigating with the model team. interim workaround: CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING=1 forces a fixed reasoning budget instead of letting the model decide per-turn.
> > > > 
> > > > > **nayroclade** · [2026-04-07](https://news.ycombinator.com/item?id=47672569)
> > > > > 
> > > > > Hey bcherny, I'm confused as to what's happening here. The linked issue was closed, with you seeming to imply there's no actual problem, people are just misunderstanding the hidden reasoning summaries and the change to the default effort level.
> > > > > 
> > > > > But here you seem to be saying there *is* a bug, with adaptive reasoning under-allocating. Is this a separate issue from the linked one? If not, wouldn't it help to respond to the linked issue acknowledging a model issue and telling people to disable adaptive reasoning for now? Not everyone is going to be reading comments on HN.
> > > > > 
> > > > > > **unsupp0rted** · [2026-04-07](https://news.ycombinator.com/item?id=47673013)
> > > > > > 
> > > > > > It's better PR to close issues and tell users they're holding it wrong, and meanwhile quietly fix the issue in the background. Also possibly safer for legal reasons.
> > > > > > 
> > > > > > > **liamsfr** · [2026-04-12](https://news.ycombinator.com/item?id=47735562)
> > > > > > > 
> > > > > > > Isn’t that what they just did here? Close Stella’s Issue, cross post to hn, then completely sidestep an observation users are making, and attack the analyst of transcripts with a straw man attack blaming… thinking summaries….
> > > > > 
> > > > > > **kenmacd** · [2026-04-07](https://news.ycombinator.com/item?id=47675087)
> > > > > > 
> > > > > > There's a 5 hour difference between the replies, and new data that came in, so the posts aren't really in conflict.
> > > > > > 
> > > > > > Also it doesn't sound like they know "there's a model issue", so opening it now would be premature. Maybe they just read it wrong, do better to let a few others verify first, then reopen.
> > > > 
> > > > > **diavelguru** · [2026-04-07](https://news.ycombinator.com/item?id=47669463)
> > > > > 
> > > > > Love this. Responding to users. Detail info investigating. Action being taken (at least it seems so).
> > > > > 
> > > > > > **gilrain** · [2026-04-07](https://news.ycombinator.com/item?id=47674136)
> > > > > > 
> > > > > > And all hidden in the comments of a niche forum, while the actual issue is closed and whitewashed? You got played.
> > > > > > 
> > > > > > **jojobas** · [2026-04-07](https://news.ycombinator.com/item?id=47671785)
> > > > > > 
> > > > > > Surely you realize it's AI responding? (not sure if /s)
> > > > 
> > > > > **allisdust** · [2026-04-07](https://news.ycombinator.com/item?id=47673589)
> > > > > 
> > > > > I cannot provide the session ids but I have tried the above flag and can confirm this makes a huge amount of difference. You should treat this as bug and make this as the default behavior. Clearly the adaptive thinking is making the model plain stupid and useless. It is time you guys take this seriously and stop messing with the performance with every damn release.
> > > > > 
> > > > > **JamesSwift** · [2026-04-07](https://news.ycombinator.com/item?id=47676046)
> > > > > 
> > > > > Just set that flag and already getting similar poor results. new one: 93b9f545-716c-4335-b216-bf0c758dff7c
> > > > > 
> > > > > > **JamesSwift** · [2026-04-07](https://news.ycombinator.com/item?id=47680389)
> > > > > > 
> > > > > > And another where claude gets into a long cycle of "wait thats not right.. hold on... actually..." correcting itself in train of thought. It found the answer eventually but wasted a lot of cycles getting there (reporting because this is a regression in my experience vs a couple weeks ago): 28e1a9a2-b88c-4a8d-880f-92db0e46ffe8
> > > > > > 
> > > > > > > **JamesSwift** · [2026-04-08](https://news.ycombinator.com/item?id=47692094)
> > > > > > > 
> > > > > > > Another 1395b7d6-f2f1-4e24-a815-73852bcdeed2
> > > > > > > 
> > > > > > > It fails to answer my initial question and tells me what I need to do to check. Then it hallucinates the answer based on not researching anything, then it incorrectly comes to a conclusion that is inaccurate, and only when I further prompt it does it finally reach a (maybe) correct answer.
> > > > > > > 
> > > > > > > I havent submitted a few more, but I think its safe to say that disabling adaptive thinking isnt the answer here
> > > > 
> > > > > **onoesworkacct** · [2026-04-07](https://news.ycombinator.com/item?id=47669914)
> > > > > 
> > > > > This kind of thing is harder for regular end-users to understand following the change removing reasoning details.
> > > > > 
> > > > > **mangatmodi** · [2026-04-07](https://news.ycombinator.com/item?id=47672130)
> > > > > 
> > > > > I am curious. Are you able to see our session text based on the session ID? That was big no in some of the tier-1 places I worked. No employee could see user texts.
> > > > > 
> > > > > > **rkangel** · [2026-04-07](https://news.ycombinator.com/item?id=47673289)
> > > > > > 
> > > > > > IIRC for Enterprise, using /feedback or /bug is an exception to the "we promise not to use your data" agreement.
> > > > 
> > > > > **tomaskafka** · [2026-04-08](https://news.ycombinator.com/item?id=47686112)
> > > > > 
> > > > > My guess is there isn't enough hardware, so Anthropic is trying to limit how much soup the buffet serve, did I guess right? And I would absolutely bet the enterprise accounts with millions in spend get priority, while the retail will be first to get throttled.
> > > > > 
> > > > > **gilrain** · [2026-04-07](https://news.ycombinator.com/item?id=47674113)
> > > > > 
> > > > > \> The data points at adaptive thinking under-allocating reasoning on certain turns
> > > > > 
> > > > > Will you reopen the issue you incorrectly closed, then…? Or are you just playacting concern?
> > > > > 
> > > > > > **pcjones1** · [2026-04-07](https://news.ycombinator.com/item?id=47675227)
> > > > > > 
> > > > > > Have you set effort to high or max?
> > > > > > 
> > > > > > > **ghusbands** · [2026-04-07](https://news.ycombinator.com/item?id=47676400)
> > > > > > > 
> > > > > > > Even with high effort, the adaptive thinking can just choose no thinking. See bcherny's post they were replying to: [https://news.ycombinator.com/item?id=47668520](https://news.ycombinator.com/item?id=47668520)
> > > > > > > 
> > > > > > > > **pcjones1** · [2026-04-08](https://news.ycombinator.com/item?id=47687462)
> > > > > > > > 
> > > > > > > > Yeah I know but you can disable it as we saw
> > 
> > > **matheusmoreira** · [2026-04-07](https://news.ycombinator.com/item?id=47670323)
> > > 
> > > I just asked Claude to plan out and implement syntactic improvements for my static site generator. I used plan mode with *Opus 4.6 max effort*. After over half an hour of thinking, it produced a very ad-hoc implementation with needless limitations instead of properly refactoring and rearchitecting things. I had to specifically prompt it in order to get it to do better. This executed at around 3 AM UTC, as far away from peak hours as it gets.
> > > 
> > > b9cd0319-0cc7-4548-bd8a-3219ede3393a
> > > 
> > > \> You're right to push back. Let me be honest about both questions.
> > > 
> > > \> The @() implementation is ad-hoc
> > > 
> > > \> The current implementation manually emits synthetic tokens — tag, start-attributes, attribute, end-attributes, text, end-interpolation — in sequence.
> > > 
> > > \> This works, but it duplicates what the child lexer already does for #\[...\], creating two divergent code paths for the same conceptual operation (inline element emission). It also means @() link text can't contain nested inline elements, while #\[a(...) text with #\[em emphasis\]\] can.
> > > 
> > > I just feel like I can't trust it anymore.
> > > 
> > > > **koverstreet** · [2026-04-07](https://news.ycombinator.com/item?id=47670544)
> > > > 
> > > > That's pretty much been my day - today was genuinely bad, and I've been putting up with a lot of this lately.
> > > > 
> > > > Now on Qwen3.5-27b, and it may not be quite as sharp as Opus was two months ago, but we're getting work done again.
> > > > 
> > > > > **matheusmoreira** · [2026-04-07](https://news.ycombinator.com/item?id=47670684)
> > > > > 
> > > > > Literally two weeks ago it was outputting excellent results while working with me on my programming language. I reviewed every line and tried to understand everything it did. It was good. I slowly started trusting it. Now I don't want to let it touch my project again.
> > > > > 
> > > > > It's extremely depressing because this is my hobby and I was having such a blast coding with Claude. I even started trying to use it to pivot to professional work. Now I'm not sure anymore. People who depend on this to make a living must be very angry indeed.
> > > > > 
> > > > > > **jacquesm** · [2026-04-07](https://news.ycombinator.com/item?id=47670725)
> > > > > > 
> > > > > > I can see how that works: this is like building a dependency, a habit if you wish. I think the tighter you couple your workflow to these tools the more dependent you will become and the greater the let-down if and when they fail. And they will *always* fail, it just depends on how long you work with them and how complex the stuff is you are doing, sooner or later you will run into the limitations of the tooling.
> > > > > > 
> > > > > > One way out of this is to always keep yourself in the loop. Never let the work product of the AI outpace your level of understanding because the moment you let that happen you're like one of those cartoon characters walking on air while gravity hasn't reasserted itself just yet.
> > > > > > 
> > > > > > > **matheusmoreira** · [2026-04-07](https://news.ycombinator.com/item?id=47671018)
> > > > > > > 
> > > > > > > Good advice about the dependency. This stuff is definitely addictive. I've been in something of a manic episode ever since I subscribed to this thing. I started getting anxious when I hit limits.
> > > > > > > 
> > > > > > > I wouldn't say that Claude is failing though. It's just that they're clearly messing with it. The real Opus is great.
> > > > > > > 
> > > > > > > > **jacquesm** · [2026-04-07](https://news.ycombinator.com/item?id=47672133)
> > > > > > > > 
> > > > > > > > Take good care of yourself and don't get sucked in too deep. I can see the danger just as clearly in programmers around me (and in myself). I keep a very strict separation between anything that can do AI and my main computer, no cutting-and-pasting and no agents. I write code because I understand what I'm doing and if I do not understand the interaction then I don't use it. I see every session with an AI chatbot as totally disposable. No long term attachment means I can stand alone any time I want to. It may not be as fast but I never have the feeling that I'm not 100% in control.
> > > > > 
> > > > > > **lelanthran** · [2026-04-07](https://news.ycombinator.com/item?id=47672595)
> > > > > > 
> > > > > > \> People who depend on this to make a living must be very angry indeed.
> > > > > > 
> > > > > > Oh cry me a fucking river.
> > > > > > 
> > > > > > The people depending on this to make a living don't have the moral high ground here.
> > > > > > 
> > > > > > They jumped onboard so they could replace other people's living, and those other people were angry too.
> > > > > > 
> > > > > > They didn't care about that. It's hard to care about them when the thing they depend on to make a living got yanked, because that's what they proposed to do to others.
> > > > > > 
> > > > > > > **burgerzzz** · [2026-04-11](https://news.ycombinator.com/item?id=47728502)
> > > > > > > 
> > > > > > > Since when am I responsible for other people's living?
> > 
> > > **koverstreet** · [2026-04-06](https://news.ycombinator.com/item?id=47664756)
> > > 
> > > I'll have a look. The CoT switch you mentioned will help, I'll take a look at that too, but my suspicion is that this isn't a CoT issue - it's a model preference issue.
> > > 
> > > Comparing Opus vs. Qwen 27b on similar problems, Opus is sharper and more effective at implementation - but will flat out ignore issues and insist "everything is fine" that Qwen is able to spot and demonstrate solid understanding of. Opus understands the issues perfectly well, it just avoids them.
> > > 
> > > This correlates with what I've observed about the underlying personalities (and you guys put out a paper the other day that shows you guys are starting to understand it in these terms - functionally modeling feelings in models). On the whole Opus is very stable personality wise and an effective thinker, I want to complement you guys on that, and it definitely contrasts with behaviors I've seen from OpenAI. But when I do see Opus miss things that it should get, it seems to be a combination of avoidant tendencies and too much of a push to "just get it done and move into the next task" from RHLF.
> > > 
> > > > **necrotic\_comp** · [2026-04-07](https://news.ycombinator.com/item?id=47670556)
> > > > 
> > > > Opus definitely pushes me to ignore problems. I've had to tell it multiple times to be thorough, and we tend to go back and forth a few times every time that happens. :)
> > > > 
> > > > > **pimeys** · [2026-04-07](https://news.ycombinator.com/item?id=47672875)
> > > > > 
> > > > > "I see the tests failing, but none of our changes caused this breakage so I will push my changes and ask the user to inform their team on failing tests."
> > > 
> > > > **jchanimal** · [2026-04-06](https://news.ycombinator.com/item?id=47668285)
> > > > 
> > > > One of the thing is we’ve seen at vibes.diy is that if you have a list of jobs and you have agents with specialized profiles and ask them to pick the best job for themselves that can change some of the behavior you described at the end of your post for the better.
> > 
> > > **freedomben** · [2026-04-06](https://news.ycombinator.com/item?id=47664562)
> > > 
> > > How much of the code/context gets attached in the /bug report?
> > > 
> > > > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664641)
> > > > 
> > > > When you submit a /bug we get a way to see the contents of the conversation. We don't see anything else in your codebase.
> > > > 
> > > > > **murkt** · [2026-04-06](https://news.ycombinator.com/item?id=47666977)
> > > > > 
> > > > > Was there a change in Claude Code system prompt at that time that nudges Claude into simplistic thinking?
> > > > > 
> > > > > Here is a gist that tries to patch the system prompt to make Claude behave better [https://gist.github.com/roman01la/483d1db15043018096ac3babf5...](https://gist.github.com/roman01la/483d1db15043018096ac3babf5688881)
> > > > > 
> > > > > I haven’t personally tried it yet. I do certainly battle Claude quite a lot with “no I don’t want quick-n-easy wrong solution just because it’s two lines of code, I want best solution in the long run”.
> > > > > 
> > > > > If the system prompt indeed prefers laziness in 5:1 ratio, that explains a lot.
> > > > > 
> > > > > I will submit /bug in a few next conversations, when it occurs next.
> > > > > 
> > > > > > **Avamander** · [2026-04-06](https://news.ycombinator.com/item?id=47667883)
> > > > > > 
> > > > > > That Gist does explain quite a few flaws Claude has. I wonder if MEMORY.md is sufficient to counteract the prompt without patching.
> > > > > > 
> > > > > > > **liamsfr** · [2026-04-12](https://news.ycombinator.com/item?id=47735569)
> > > > > > > 
> > > > > > > And if memory.md can’t and you need something quick and dirty for flat memory management, I wrote a plugin just for this.
> > > > > > > 
> > > > > > > [https://github.com/NominexHQ/pmm-plugin](https://github.com/NominexHQ/pmm-plugin)
> > > > > 
> > > > > > **matheusmoreira** · [2026-04-07](https://news.ycombinator.com/item?id=47679011)
> > > > > > 
> > > > > > I adapted these patches into settings for the tweakcc tool.
> > > > > > 
> > > > > > [https://github.com/Piebald-AI/tweakcc](https://github.com/Piebald-AI/tweakcc)
> > > > > > 
> > > > > > Pushed it to my dotfiles repository:
> > > > > > 
> > > > > > [https://github.com/matheusmoreira/.files/tree/master/~/.twea...](https://github.com/matheusmoreira/.files/tree/master/~/.tweakcc/system-prompts)
> > > > > > 
> > > > > > The tweaks can be applied with
> > > > > > 
> > > > > > ```
> > > > > > npx tweakcc --apply
> > > > > > ```
> > > > > > 
> > > > > > **naasking** · [2026-04-07](https://news.ycombinator.com/item?id=47677562)
> > > > > > 
> > > > > > Very interesting. I run Claude Code in VS Code, and unfortunately there doesn't seem to be an equivalent to "cli.js", it's all bundled into the "claude.exe" I've found under the VS code extensions folder (confirmed via hex editor that the prompts are in there).
> > > > > > 
> > > > > > Edit: tried patching with revised strings of equivalent length informed by this gist, now we'll see how it goes!
> > > > > > 
> > > > > > **andersa** · [2026-04-07](https://news.ycombinator.com/item?id=47672309)
> > > > > > 
> > > > > > I didn't know we could change the base system prompt of Claude Code. Just tried, and indeed it works. This changes everything! Thank you for posting this!
> > > > > > 
> > > > > > **dev\_l1x\_be** · [2026-04-06](https://news.ycombinator.com/item?id=47667758)
> > > > > > 
> > > > > > Holy sweet LLM, this gist is crazy. Why did they do this to themselves? I am going to try this at home, it might actually fix Claude.
> > > > > > 
> > > > > > > **murkt** · [2026-04-06](https://news.ycombinator.com/item?id=47667922)
> > > > > > > 
> > > > > > > Remember Sonnet 3.5 and 3.7? They were happy to throw abstraction on top of abstraction on top of abstraction. Still a lot of people have “do not over-engineer, do not design for the future” and similar stuff in their CLAUDE.md files.
> > > > > > > 
> > > > > > > So I think the system prompt just pushes it way too hard to “simple” direction. At least for some people. I was doing a small change in one of my projects today, and I was quite happy with “keep it stupid and hacky” approach there.
> > > > > > > 
> > > > > > > And in the other project I am like “NO! WORK A LOT! DO YOUR BEST! BE HAPPY TO WORK HARD!”
> > > > > > > 
> > > > > > > So it depends.
> > > > > > > 
> > > > > > > **pbowyer** · [2026-04-07](https://news.ycombinator.com/item?id=47672304)
> > > > > > > 
> > > > > > > Let us know if it does, because we all want it to work :)
> > > > > 
> > > > > > **withinboredom** · [2026-04-07](https://news.ycombinator.com/item?id=47671997)
> > > > > > 
> > > > > > Is there not a setting to change the system prompt itself? I vaguely remember seeing it in the docs.
> > > > > > 
> > > > > > > **matheusmoreira** · [2026-04-07](https://news.ycombinator.com/item?id=47675763)
> > > > > > > 
> > > > > > > There is!!
> > > > > > > 
> > > > > > > [https://code.claude.com/docs/en/cli-reference#system-prompt-...](https://code.claude.com/docs/en/cli-reference#system-prompt-flags)
> > > > > > > 
> > > > > > > ```
> > > > > > > --append-system-prompt
> > > > > > >   --append-system-prompt-file
> > > > > > >   --system-prompt
> > > > > > >   --system-prompt-file
> > > > > > > ```
> > > > > > > Can this script be made to work without patching the executable?
> > > > > > > 
> > > > > > > > **withinboredom** · [2026-04-07](https://news.ycombinator.com/item?id=47675798)
> > > > > > > > 
> > > > > > > > Might be worth extracting the system prompt and then patching it. TBH, that's what I was expecting when I saw the gist.
> > > > > > > > 
> > > > > > > > > **matheusmoreira** · [2026-04-07](https://news.ycombinator.com/item?id=47676039)
> > > > > > > > > 
> > > > > > > > > This might be more complex than I imagined. It seems Claude Code dynamically customizes the system prompt. They also update the system prompt with every version so outright replacing it will cause us to miss out on updates. Patching is probably the best solution.
> > > > > > > > > 
> > > > > > > > > [https://github.com/Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)
> > > > > > > > > 
> > > > > > > > > [https://github.com/Piebald-AI/tweakcc](https://github.com/Piebald-AI/tweakcc)
> > > > > > > > > 
> > > > > > > > > > **withinboredom** · [2026-04-07](https://news.ycombinator.com/item?id=47676153)
> > > > > > > > > > 
> > > > > > > > > > Interesting. So literally triggering any of these changes probably invalidates the cache as well…
> > > > 
> > > > > **andoando** · [2026-04-07](https://news.ycombinator.com/item?id=47669208)
> > > > > 
> > > > > Isnt the codebase in the context window?
> > > > > 
> > > > > > **frog437** · [2026-04-07](https://news.ycombinator.com/item?id=47669568)
> > > > > > 
> > > > > > depending on how large your codebase is, hopefully not. At this point use something like the IX plugin to ingest codebase and track context, rather than from the LLM itself.
> > > > > > 
> > > > > > > **frog437** · [2026-04-07](https://news.ycombinator.com/item?id=47670632)
> > > > > > > 
> > > > > > > This is crazy..
> > > > > > > 
> > > > > > > tokensSaved = naiveTokens - actualTokens
> > > > > > > 
> > > > > > > ```
> > > > > > > - naiveTokens = 19.4M — what ix estimates it would have cost to answer your queries without graph intelligence (i.e., dumping full files/directories into context)                                    
> > > > > > >   - actualTokens = 4.7M — what ix's targeted, graph-aware responses actually used
> > > > > > >   - tokensSaved = 14.7M — the difference
> > > > > > > ```
> > > > > > > 
> > > > > > > **andoando** · [2026-04-09](https://news.ycombinator.com/item?id=47699197)
> > > > > > > 
> > > > > > > I mean whatever part of the code that is read by the AI has to be in the content window at some point or another nSprewd throughout your sessions Id think even with a huge codebase, 90% of it is going to be there
> 
> > **stefan\_** · [2026-04-06](https://news.ycombinator.com/item?id=47666726)
> > 
> > Theres also been tons of thinking leaking into the actual output. Recently it even added thinking into a code patch it did (a\[0\] &= ~(1 << 2); // actually let me just rewrite { .. 5 more lines setting a\[0\] .. }).
> > 
> > > **taylorfinley** · [2026-04-06](https://news.ycombinator.com/item?id=47668649)
> > > 
> > > I've seen this frequently also
> > > 
> > > > **withinboredom** · [2026-04-07](https://news.ycombinator.com/item?id=47672004)
> > > > 
> > > > I suspect it happens when the model's adaptive thinking was too conservative and it could have thought more, but didn't.
> 
> > **butlike** · [2026-04-07](https://news.ycombinator.com/item?id=47677454)
> > 
> > They probably want to prove to a single holdout investor that their 'thinking process' is getting faster in order to get the investor on board.

> **plexicle** · [2026-04-06](https://news.ycombinator.com/item?id=47664733)
> 
> Ultrathink is back? I thought that wasn't a thing anymore.
> 
> If I am following.. "Max" is above "High", but you can't set it to "Max" as a default. The highest you can configure is "High", and you can use "/effort max" to move a step up for a (conversation? session?), or "ultrathink" somewhere in the prompt to move a step up for a single turn. Is this accurate?
> 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664766)
> > 
> > Yep, exactly
> > 
> > > **dostick** · [2026-04-06](https://news.ycombinator.com/item?id=47666098)
> > > 
> > > Mentioning ULTRATHINK in prompt is the equivalent to /effort max?
> > > 
> > > > **merlindru** · [2026-04-06](https://news.ycombinator.com/item?id=47667637)
> > > > 
> > > > Yes but only for the message that includes it. Whereas /effort max keeps it at max effort the entire convo, to my knowledge
> > > > 
> > > > **ccmcarey** · [2026-04-11](https://news.ycombinator.com/item?id=47733961)
> > > > 
> > > > No, ultrathink puts it in /effort high mode. There's no kw for one turn of effort max

> **potsandpans** · [2026-04-06](https://news.ycombinator.com/item?id=47668780)
> 
> For anyone reading this and wondering where the truth could possibly be:
> 
> We can't really know what the truth is, because Anthropic is tightly controlling how you interact with their product and provides their service through opaque processes. So all we can do is speculate. And in that speculation there's a lot of room (for the company) to bullshit or provide equally speculative responses, and (for outsiders) to search for all plausible explanations within the solution space. So there's not much to action on. We're effectively stuck with imprecise heuristics and vibes.
> 
> But consider what we do know: the promise is that Anthropic is providing a black-box service that solves large portions of the SDLC. Maybe all of it. They are "making the market" here, and their company growth depends on this bet. This is why these processes are opaque: they have to be. Anthropic, OpenAI and a few others see this as a zero-sum game. The winner "owns" the SDLC (and really, if they get their way the entire PDLC). So the competitive advantage lies in tightly controlling and tweaking their hidden parameters to squeeze as much value and growth as possible.
> 
> The downside is that we're handing over the magic for convenience and cost. A lot of people are maybe rightly criticizing the OP of the issue because they're staking their business on Claude Code in a way that's very risky. But this is essentially what these companies are asking for. The business model end game is: here's the token factory, we control it and you pay for the pleasure of using it. Effectively, rent-seeking for software development. And if something changes and it disrupts your business, you're just using it incorrectly. Try turning effort to max.
> 
> Reading responses like this from these company representatives makes me increasingly uneasy because it's indicative of how much of writing software is being taken out from under our feet. The glimmer of promise in all of this though is that we are seeing equity in the form of open source. Maybe the answer is: use pi-mono, a smattering of self hosted and open weights models (gemma4, kimi, minimax are extremely capable) and escalate to the private lab models through api calls when encountering hard problems.
> 
> Let the best model win, not the best end to end black box solution.
> 
> > **vachina** · [2026-04-07](https://news.ycombinator.com/item?id=47669574)
> > 
> > Don’t turn vibe coding into your day job (because the vibe won’t keep vibing). Write code (that you own) that can make you money and hire real developers.
> > 
> > **mvkel** · [2026-04-07](https://news.ycombinator.com/item?id=47669431)
> > 
> > I am reminded of OpenAI's first voice-to-voice demo a couple of years ago. I rewatched it and was shocked at how human it was; indiscernible from a real person. But the voice agent that we got sounds 20% better than Siri.
> > 
> > There's a hope that competition is what keeps these companies pushing to ship value to customers, but there are also billions of compute expense at stake, so there seems to be an understanding that nobody ships a product that is unsustainably competitive

> **anonymoushn** · [2026-04-06](https://news.ycombinator.com/item?id=47668209)
> 
> How do you guys decide which settings should be configurable via environment variables but not settings files and which settings should be configurable via settings files but not environment variables?
> 
> > **bcherny** · [2026-04-07](https://news.ycombinator.com/item?id=47669387)
> > 
> > All environment variables can also be configured via settings files (in the “env” field).
> > 
> > Our approach generally is to use env vars for more experimental and low usage settings, and reserve top-level settings for knobs that we expect customers will tune more frequently.

> **robeym** · [2026-04-07](https://news.ycombinator.com/item?id=47675460)
> 
> This is confusing. ULTRATHINK is a step below /effort max?
> 
> ULTRATHINK triggers high effort. /effort max is above high. Calling it ULTRATHINK sounds like it would be the highest mode. If someone has max set and types ULTRATHINK, they're lowering their effort for that turn.
> 
> For anyone reading this trying to fix the quality issues, here's what I landed on in ~/.claude/settings.json:
> 
> ```
> {
>     "env": {
>       "CLAUDE_CODE_EFFORT_LEVEL": "max",
>       "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS": "1",
>       "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING": "1"
>     }
>   }
> ```
> The env field in settings.json persists across sessions without needing /effort max every time.
> 
> DISABLE\_ADAPTIVE\_THINKING is key. That's the system that decides "this looks easy, I'll think less" - and it's frequently wrong. Disabling it gives you a fixed high budget every turn instead of letting the model shortchange itself.
> 
> > **ericpan** · [2026-04-09](https://news.ycombinator.com/item?id=47705980)
> > 
> > The docs say that CLAUDE\_CODE\_EFFORT\_LEVEL controls adaptive reasoning intensity, and CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING bypasses that entirely in favor of a fixed budget via MAX\_THINKING\_TOKENS. So setting both is contradictory. If true, disabling adaptive thinking would override what effort level is trying to do.
> > 
> > [https://code.claude.com/docs/en/env-vars](https://code.claude.com/docs/en/env-vars)
> > 
> > > **robeym** · [2026-04-09](https://news.ycombinator.com/item?id=47708616)
> > > 
> > > So if it bypasses, is the optimal setting for performance setting effort level to max, keeping adaptive on? I try to avoid letting the model decide what is unimportant and needs less thought
> 
> > **airstrike** · [2026-04-12](https://news.ycombinator.com/item?id=47742955)
> > 
> > Whaaa this is insanely stupid from their part.
> > 
> > Also I'm curious if telling subagents to ultrathink has any impact.
> > 
> > I guess I can always ask a friend of mine to read the source...
> > 
> > **jnfr** · [2026-04-07](https://news.ycombinator.com/item?id=47677307)
> > 
> > Thanks for sharing. Have you experienced noticeable impact to your usage rate?
> > 
> > > **robeym** · [2026-04-08](https://news.ycombinator.com/item?id=47688893)
> > > 
> > > Nothing super noticeable. I've reached 35% in sessions on the 20x plan. Before these changes, 25-30% was pretty normal. I think these changes are best for people who are just past the 5x usage plan, but might be harder to manage if you already have to throttle usage to stay under limits.
> > > 
> > > I'd still recommend turning off sub agents entirely because it doesn't seem you can control them with /effort and I always find the output to be better with agents off.

> **hansmayer** · [2026-04-07](https://news.ycombinator.com/item?id=47671777)
> 
> You guys realise you are about 3 months into another one of your CEOs announcements that AI would "write all code in 6 months", right? Based on the problems you are facing, would you say your CEO gave a realistic announcement this time around ?
> 
> > **axegon\_** · [2026-04-07](https://news.ycombinator.com/item?id=47673557)
> > 
> > Almost as if every CEO is making promises and predictions that either exist solely in their heads or know full well that the odds of this working out are about the same as finding the fountain of youth and are just milking whatever cash they can out of the hype.
> > 
> > > **hansmayer** · [2026-04-09](https://news.ycombinator.com/item?id=47700026)
> > > 
> > > Well, there is a ton of normal CEOs of "normal" companies doing a great job, due diligence and all. Its just these weird CEOs of weird companies with weird business models, who burn hundreds of billions of dollars to produce effectively peanuts, that make a lot of decent CEOs look bad.
> 
> > **blurbleblurble** · [2026-04-07](https://news.ycombinator.com/item?id=47671840)
> > 
> > idk seems accurate from where I'm sitting

> **w10-1** · [2026-04-06](https://news.ycombinator.com/item?id=47665013)
> 
> Here's the reply in context:
> 
> [https://github.com/anthropics/claude-code/issues/42796#issue...](https://github.com/anthropics/claude-code/issues/42796#issuecomment-4194007103)
> 
> Sympathies: Users now completely depend on their jet-packs. If their tools break (and assuming they even recognize the problem). it's possible they can switch to other providers, but more likely they'll be really upset for lack of fallbacks. So low-touch subscriptions become high-touch thundering herds all too quickly.

> **dc\_giant** · [2026-04-06](https://news.ycombinator.com/item?id=47664742)
> 
> All right so what do I need to do so it does its job again? Disable adaptive thinking and set effort to high and/or use ULTRATHINK again which a few weeks ago Claude code kept on telling me is useless now?
> 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664770)
> > 
> > Run this: /effort high
> > 
> > > **berkanunal** · [2026-04-06](https://news.ycombinator.com/item?id=47665044)
> > > 
> > > Imagine if all service providers were behaving like this.
> > > 
> > > \> Ahh, sorry we broke your workflow.
> > > 
> > > \> We found that \`log\_level=error\` was a sweet spot for most users.
> > > 
> > > \> To make it work as you expect it so, run \`./bin/unpoop\` it will set log\_level=warn
> > > 
> > > > **hackboyfly** · [2026-04-07](https://news.ycombinator.com/item?id=47670991)
> > > > 
> > > > Yeah it’s stupid.
> > > > 
> > > > What makes me more annoyed HN users here actually simping for Claude.
> > > > 
> > > > “Hi thank you for Claude Code even though you nerfed the subscriptions, btw can I get red text instead of green?”
> > > > 
> > > > > **naasking** · [2026-04-07](https://news.ycombinator.com/item?id=47676398)
> > > > > 
> > > > > They're a business. The alternative to keep costs in check would to ask you for more money, and you'd likely be even more upset with that.
> > > > > 
> > > > > > **stldev** · [2026-04-07](https://news.ycombinator.com/item?id=47682424)
> > > > > > 
> > > > > > They are definitely that. Regardless of their approach, being upfront and transparent would have been nice. Bricking their own software that previously worked well for their customers isn't cool.
> 
> > **stldev** · [2026-04-06](https://news.ycombinator.com/item?id=47665740)
> > 
> > You can't. This is Anthropic leveraging their dials, and ignoring their customers for weeks.
> > 
> > Switch providers.
> > 
> > Anecdotally, I've had no luck attempting to revert to prior behavior using either high/max level thinking (opus) or prompting. The web interface for me though doesn't seem problematic when using opus extended.
> > 
> > > **mlrtime** · [2026-04-07](https://news.ycombinator.com/item?id=47673192)
> > > 
> > > Agreed, the only feedback is switching... however things move fast. Unfortunately that means for me is subscribing or using API for many providers and then just switching models when one gets worse.
> > > 
> > > If you have a paid plan, you may need to pay for more than one, and "hopefully" the drop in usage (not income) is a good enough signal that there is a issue.
> > > 
> > > **taylorfinley** · [2026-04-06](https://news.ycombinator.com/item?id=47668689)
> > > 
> > > I've actually switched back to the web chat UI and copying Python files for much of my work because CC has been so nerfed.

> **anonymoushn** · [2026-04-06](https://news.ycombinator.com/item?id=47668126)
> 
> \> On of our product principles is to avoid changing settings on users' behalf
> 
> Ideally there wouldn't be silent changes that greatly reduce the utility of the user's session files until they set a newly introduced flag.
> 
> I happen to think this is just true in general, but another reason it might be true is that the experience the user has is identical to the experience they would have had if you first introduced the setting, defaulting it to the existing behavior, and then subsequently changed it on users' behalf.

> **aizk** · [2026-04-06](https://news.ycombinator.com/item?id=47664476)
> 
> How do you guys manage regressions as a whole with every new model update? A massive test set of e2e problem solving seeing how the models compare?
> 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664539)
> > 
> > A mix of evals and vibes.
> > 
> > > **efields** · [2026-04-06](https://news.ycombinator.com/item?id=47666025)
> > > 
> > > "Evals and vibes" can I put that on a t shirt?
> > > 
> > > **giwook** · [2026-04-06](https://news.ycombinator.com/item?id=47664564)
> > > 
> > > What's that ratio exactly
> > > 
> > > **capnchaos** · [2026-04-06](https://news.ycombinator.com/item?id=47664748)
> > > 
> > > Are you doing any Digital Twin testing or simulations? I imagine you can't test a product like Claude Code using traditional means.
> 
> > **cududa** · [2026-04-06](https://news.ycombinator.com/item?id=47668056)
> > 
> > Remember when they shipped that version that didn't actually start/ run? At work we were goofing on them a bit, until I said "Wait how did their tests even run on that?" And we realized whatever their CI/CD process is, it wasn't at the time running on the actual release binary... I can imagine their variation on how most engineers think about CI/CD probably is indicative of some other patterns (or lack of traditional patterns)
> > 
> > As someone that used to work on Windows, I kind of had a vision of a similar in scope e2e testing harness, similar to Windows Vista/ 7 (knowing about bugs/ issues doesn't mean you can necessarily fix them ... hence Vista then 7) - and that Anthropic must provide some Enterprise guarantee backed by this testing matrix I imagined must exist - long way of saying, I think they might just YOLO regressions by constantly updating their testing/ acceptance criteria.
> > 
> > Why not provide pinable versions or something? This episode and wasted 2 months of suboptimal productivity hits on the absurdity of constantly changing the user/ system prompt and doing so much of the R&D and feature development at two brittle prompts with unclear interplay. And so until there’s like a compostable system/user prompt framework they reliably develop tests against, I personally would prefer pegged selectable versions. But each version probably has like known critical bugs they’re dancing around so there is no version they’d feel comfortable making a pegged stable release..
> > 
> > > **xnorswap** · [2026-04-07](https://news.ycombinator.com/item?id=47672934)
> > > 
> > > That was actually an interesting case of things that CI/CD don't tend to catch.
> > > 
> > > It failed to start because it failed to parse the published release notes.
> > > 
> > > In the CI/CD system it would have passed, because the release notes that broke it, hadn't been published yet.
> > > 
> > > Those release notes also took down previous versions of claude-code too, rolling back didn't help users.
> > > 
> > > The breakage wasn't a change in the software, it was a change in the release notes which coincided with the change in the software.
> > > 
> > > Now, should it have been grabbing release notes and parsing them? No, that's unbelievably dumb (and potentially dangerous), but it wasn't an issue with missing CI/CD, but an interesting case-study in CI/CD gaps and how CI/CD can actually lead to over-confidence.
> > > 
> > > **misnome** · [2026-04-06](https://news.ycombinator.com/item?id=47668478)
> > > 
> > > about once a week I get a claude "auto update" that fails to start with some bun error on our linux machines. It's beyond laughable.
> 
> > **try-working** · [2026-04-06](https://news.ycombinator.com/item?id=47666813)
> > 
> > I use a self-documenting recursive workflow: [https://github.com/doubleuuser/rlm-workflow](https://github.com/doubleuuser/rlm-workflow)

> **KenoFischer** · [2026-04-06](https://news.ycombinator.com/item?id=47665289)
> 
> While we have you here, could you fix the bash escaping bug? [https://github.com/anthropics/claude-code/issues/10153](https://github.com/anthropics/claude-code/issues/10153)

> **mikkom** · [2026-04-07](https://news.ycombinator.com/item?id=47673129)
> 
> \>Going forward, we will test defaulting Teams and Enterprise users to high effort, to benefit from extended thinking even if it comes at the cost of additional tokens & latency.
> 
> interesting that you only make this default on those accounts that pay per token while claiming "medium is best for most users"
> 
> That decision seems to imply that the thinking change was more about increasing your profits than anything else
> 
> > **Normal\_gaussian** · [2026-04-07](https://news.ycombinator.com/item?id=47673164)
> > 
> > [https://claude.com/pricing#team-&-enterprise](https://claude.com/pricing#team-&-enterprise)
> > 
> > Team is not per-token priced

> **taspeotis** · [2026-04-07](https://news.ycombinator.com/item?id=47669843)
> 
> Hi, thanks for Claude Code. I was wondering though if you'd considering adding a mode to make text green and characters come down from the top of the screen individually, like in The Matrix?
> 
> > **Terretta** · [2026-04-07](https://news.ycombinator.com/item?id=47674638)
> > 
> > Ergonomics studies back in the day demonstrated amber beats green. Our shop spent extra for amber CRTs over green.
> > 
> > On MacOS Terminal, edit the Homebrew profile and set Text and Bold Text to Apple color Orange, consider setting Selection to Apple color Green and Cursor to Block, Blink, and Apple color Yellow.

> **ai\_slop\_hater** · [2026-04-06](https://news.ycombinator.com/item?id=47664563)
> 
> \> This beta header hides thinking from the UI, since most people don't look at it.
> 
> I look at it, and I am very upset that I no longer see it.
> 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664656)
> > 
> > There is a setting if you'd like to continue to see it: showThinkingSummaries.
> > 
> > See the docs: [https://code.claude.com/docs/en/settings#available-settings](https://code.claude.com/docs/en/settings#available-settings)
> > 
> > > **antonvs** · [2026-04-06](https://news.ycombinator.com/item?id=47664874)
> > > 
> > > \> As I noted in the comment,
> > > 
> > > Piece of free PR advice: this is fine in a nerd fight, but don't do this in comments that represent a company. Just repeat the relevant information.
> > > 
> > > > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47665008)
> > > > 
> > > > Fair feedback, edited!
> > > > 
> > > > **trvz** · [2026-04-06](https://news.ycombinator.com/item?id=47666605)
> > > > 
> > > > Piece of free advice towards a better civilisation: people who didn't even read the comment they're replying to shouldn't be rewarded for their laziness.
> > > > 
> > > > > **ai\_slop\_hater** · [2026-04-06](https://news.ycombinator.com/item?id=47666792)
> > > > > 
> > > > > I read his comment and still replied. I think his claim that nobody reads thinking blocks and that thinking blocks increase latency is nonsense. I am not going to figure out which settings I need to enable because after reading this thread I cancelled my subscription and switched over to Codex. Because I had the exact same experience as many in this thread.
> > > > > 
> > > > > Also what is that "PR advice"—he might as well wear a suit. This is absolutely a nerd fight.
> > > > > 
> > > > > > **ai\_slop\_hater** · [2026-04-06](https://news.ycombinator.com/item?id=47667470)
> > > > > > 
> > > > > > Alright, I just tested that setting and it doesn't work.
> > > > > > 
> > > > > > [https://i.imgur.com/MYsDSOV.png](https://i.imgur.com/MYsDSOV.png)
> > > > > > 
> > > > > > I tested because I was porting memories from Claude Code to Codex, so I might as well test. I obviously still have subscription days remaining.
> > > > > > 
> > > > > > There is another comment in this thread linking a GitHub issue that discusses this. The GitHub issue this whole HN submission is about even says that Anthropic hides thinking blocks.
> > > > > > 
> > > > > > > **mlrtime** · [2026-04-07](https://news.ycombinator.com/item?id=47673207)
> > > > > > > 
> > > > > > > How are you porting over your memories, skills, commands (codex doesn't have commands).
> > > > > > > 
> > > > > > > > **ai\_slop\_hater** · [2026-04-07](https://news.ycombinator.com/item?id=47676766)
> > > > > > > > 
> > > > > > > > I didn't use commands. I only used rules, memories, and skills. I asked Codex to read rules and memories from where Claude Code stores them on the filesystem and merge them into \`AGENTS.md\` and this actually works better because Anthropic prompts Claude Code to write each memory to a separate file, so you end up having a main MEMORY.md that acts as a kind of directory that lists each individual memory with its file name and brief description, hoping that Claude Code will read them, but the problem is that Claude Code never does. This is the same problem\[0\] that Vercel had with skills I believe. Skills are easy to port because they appear to use the same format, so you can just do \`mv ~/.claude/skills ~/.codex/skills\` (or \`.agents/skills\`).
> > > > > > > > 
> > > > > > > > \[0\]: [https://vercel.com/blog/agents-md-outperforms-skills-in-our-...](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)
> > > > > 
> > > > > > **antonvs** · [2026-04-07](https://news.ycombinator.com/item?id=47679265)
> > > > > > 
> > > > > > What I was pointing out in my comment about the PR advice is that someone responding from a corporation to customers should be providing information to help the customer, nothing more.
> > > > > > 
> > > > > > Customers may want to fight - you seem to be providing an example - but representatives shouldn't take the bait.
> > 
> > > **starkparker** · [2026-04-06](https://news.ycombinator.com/item?id=47664761)
> > > 
> > > \> Thinking summaries will now appear in the transcript view (Ctrl+O).
> > > 
> > > Also: [https://github.com/anthropics/claude-code/issues/30958](https://github.com/anthropics/claude-code/issues/30958)
> > > 
> > > > **ai\_slop\_hater** · [2026-04-06](https://news.ycombinator.com/item?id=47664823)
> > > > 
> > > > I also have similar experience with their API, i.e. some requests get stalled for minutes with zero events coming in from Anthropic. Presumably the model does this "extended thinking" but no way to see that. I treat these requests as stuck and retry. Same experience in Claude Code Opus 4.6 when effort is set to "high"—the model gets stuck for ten minutes (at which point I cancel) and token count indicator doesn't increase.
> > > > 
> > > > I am not buying what this guy says. He is either lying or not telling us everything.
> > 
> > > **computerex** · [2026-04-07](https://news.ycombinator.com/item?id=47671764)
> > > 
> > > Wrote my own harness with introspection/long form thinking as a tool that the model can use to plan. Works really well with opus. I can’t use Claude code sadly, it sits there ticking for minutes seemingly doing absolutely nothing although I know it’s working. I hate that as an experience and built my harness with the philosophy of always having something streaming on the ui.
> > > 
> > > Btw the system prompt length in CC is getting to be insane.

> **yubblegum** · [2026-04-06](https://news.ycombinator.com/item?id=47665374)
> 
> \> Before I keep going, I wanted to say I appreciate the depth of thinking & care that went into this.
> 
> "This report was produced by me — Claude Opus 4.6 — analyzing my own session logs. ... Ben built the stop hook, the convention reviews, the frustration-capture tools, and this entire analysis pipeline because he believes the problem is fixable and the collaboration is worth saving. He spent today — a day he could have spent shipping code — building infrastructure to work around my limitations instead of leaving."
> 
> What a "fuckin'" circle jerk this universe has turned out to be. This note was produced by me and who the hell is Ben?
> 
> > **razodactyl** · [2026-04-06](https://news.ycombinator.com/item?id=47668192)
> > 
> > Bad feedback loops. It's hard to tell with such a massive report if the numbers are real or bad data.
> > 
> > The worst part is how big AI generated reports are - so much time spent in total having to read fluff.
> > 
> > **delusional** · [2026-04-07](https://news.ycombinator.com/item?id=47671022)
> > 
> > I think it's absolutely hilarious.
> > 
> > \> Ohh my precious baby, you've been oh so smart in writing to me.
> > 
> > He says, before dismantling everything reported in the issue. If the depth of thinking was so great (maybe if he had ULTRATHINK'd?) You'd think he would have found an actual problem.

> **migali49g** · [2026-04-06](https://news.ycombinator.com/item?id=47666673)
> 
> Hi Boris, thanks for addressing this and providing feedback quickly. I noticed the same issue. My question is, is it enough to do /efforts high, or should I also add CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING to my settings?

> **JohnMakin** · [2026-04-06](https://news.ycombinator.com/item?id=47665084)
> 
> I’ve seen you/anthropic comment repeatedly over the last several months about the “thinking” in similar ways -
> 
> “most users dont look at it” (how do you know this?)
> 
> “our product team felt it was too visually noisy”
> 
> etc etc. But every time something like this is stated, your power users (people here for the most part) state that this is dead wrong. I know you are repeating the corporate line here, but it’s bs.
> 
> > **exfalso** · [2026-04-06](https://news.ycombinator.com/item?id=47667442)
> > 
> > It's to prevent distillation. Duh
> > 
> > > **JohnMakin** · [2026-04-07](https://news.ycombinator.com/item?id=47670996)
> > > 
> > > of course that’s the reason but don’t pretend it’s some user guided decision
> > > 
> > > > **svnt** · [2026-04-07](https://news.ycombinator.com/item?id=47676206)
> > > > 
> > > > They don’t want to officially disclose the reality because while some users will understand the realities of protecting a product while innovating, many will just realize it means one can go looking for claude 4.5 performance elsewhere.
> 
> > **jitl** · [2026-04-07](https://news.ycombinator.com/item?id=47670096)
> > 
> > building for the loud users on a forum is generally a losing move. if we built notion for angry HN users, we'd probably be a great obsidian competitor with end to end encryption, have zero ai features, and make zero money.
> > 
> > **wonnage** · [2026-04-06](https://news.ycombinator.com/item?id=47665618)
> > 
> > Anecdotally the “power users” of AI are the ones who have succumbed to AI psychosis and write blog posts about orchestrating 30 agents to review PRs when one would’ve done just fine.
> > 
> > The actual power users have an API contract and don’t give a shit about whatever subscription shenanigans Claude Max is pulling today
> > 
> > > **razodactyl** · [2026-04-06](https://news.ycombinator.com/item?id=47668174)
> > > 
> > > Generalisations and angry language but I almost agree with the underlying message.
> > > 
> > > New tools, turbulent methods of execution. There's definitely something here in the way of how coding will be done in future but this is still bleeding edge and many people will get nicked.
> > > 
> > > **JohnMakin** · [2026-04-06](https://news.ycombinator.com/item?id=47666513)
> > > 
> > > Uh, no. Definitely not me at all.
> > > 
> > > > **JohnMakin** · [2026-04-06](https://news.ycombinator.com/item?id=47667314)
> > > > 
> > > > Whatever makes you feel better about yourself, I guess. My account history on this topic is pretty easily searchable, but I guess it's easier to make driveby comments like this than be informed.
> > > > 
> > > > > **wonnage** · [2026-04-06](https://news.ycombinator.com/item?id=47668378)
> > > > > 
> > > > > Lol the only thing that looking at your comment history brought is that you repeatedly bring up your long comment history.
> 
> > **alasano** · [2026-04-07](https://news.ycombinator.com/item?id=47670207)
> > 
> > Last time he made the front page he said the same things.
> > 
> > [https://news.ycombinator.com/item?id=46978710](https://news.ycombinator.com/item?id=46978710)
> > 
> > Then proceeded to fix nothing whatsoever.
> > 
> > It really does feel like he's just doing mostly what he wants and talking on behalf of vague made up users while real users complain on GitHub issues.

> **Sayrus** · [2026-04-07](https://news.ycombinator.com/item?id=47671992)
> 
> \> If you are analyzing locally stored transcripts, you wouldn't see raw thinking stored when this header is set, which is likely influencing the analysis. When Claude sees lack of thinking in transcripts for this analysis, it may not realize that the thinking is still there, and is simply not user-facing.
> 
> Claude often fetches past transcript for information after compaction. Wouldn't this effectively distort the view it has of past discussions?

> **hedora** · [2026-04-08](https://news.ycombinator.com/item?id=47690850)
> 
> I tried testing 4.5 opus and 4.6 opus both with “high” thinking. Same box, same repo. I had them plan a moderate complexity refactoring on a small codebase.
> 
> Observations:
> 
> 4.6 had previously failed to the point where I had to wipe context. It must have written memories because it was referring to the previous conversation.
> 
> As the article points out, 4.6 went out of its way to be lazy and came up with an unusable plan. It did extra planning to avoid renaming files (the toplevel task description involves reorganizing directories of files).
> 
> 4.6 took twice as long to respond as 4.5.
> 
> I’m treating this as a model regression. 4.6 is borderline unusable. I’ve hit all the issues the article describes.
> 
> Also, there needs to be an obvious way to disable memory or something. The current UX is terrible, since once an error or incorrect refusal propagates, there is no obvious recovery path.
> 
> Anyway, with think set to high, I see drastically different behavior: much slower and much worse output from 4.6.
> 
> > **justinclift** · [2026-04-08](https://news.ycombinator.com/item?id=47691446)
> > 
> > \> Also, there needs to be an obvious way to disable memory or something.
> > 
> > Memory files are stored in a path under ~/.claude somewhere. It's fairly easy to find (I'm just not typing this on a PC with Claude on it atm), and from memory (heh) it's in Markdown.
> > 
> > If you nuke the memory file(s) then you should be good. Oh, I think the memory files are project or directory scoped from memory (heh again) too, so you should be able to keep/remove things manually without losing important stuff if you want.
> > 
> > \> Anyway, with think set to high, I see drastically different behavior: much slower and much worse output from 4.6.
> > 
> > Might be worth trying the *CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING* setting then?

> **DennisL123** · [2026-04-06](https://news.ycombinator.com/item?id=47664695)
> 
> Happy to have my mind changed, yet I am not 100% convinced closing the issue as completed captures the feedback.
> 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664716)
> > 
> > From the contents of the issue, this seems like a fairly clear default effort issue. Would love your input if there's something specific that you think is unaddressed.
> > 
> > > **vecter** · [2026-04-06](https://news.ycombinator.com/item?id=47665058)
> > > 
> > > From this reply, it seems that it has nothing to do with \`/effort\`: [https://github.com/anthropics/claude-code/issues/42796#issue...](https://github.com/anthropics/claude-code/issues/42796#issuecomment-4194114622)
> > > 
> > > I hope you take this seriously. I'm considering moving my company off of Claude Code immediately.
> > > 
> > > Closing the GH issue without first engaging with the OP is just a slap in the face, especially given how much hard work they've done on your behalf.
> > > 
> > > > **wonnage** · [2026-04-06](https://news.ycombinator.com/item?id=47665531)
> > > > 
> > > > The OP “bug report” is a wall of AI slop generated from looking at its own chat transcripts
> > > > 
> > > > > **vecter** · [2026-04-06](https://news.ycombinator.com/item?id=47665937)
> > > > > 
> > > > > Do you disagree with any of the data or conclusions?
> > > > > 
> > > > > > **adi\_kurian** · [2026-04-07](https://news.ycombinator.com/item?id=47669322)
> > > > > > 
> > > > > > I must admit, the fact that the writing was well formatted and structured was an instant turn off. I did find it insightful. I would have been more willing to read it if it was one lower case run on line with typos one would expect from a prepubescent child. I am both joking and being serious at the same time. What a world.
> > > > > > 
> > > > > > **wonnage** · [2026-04-06](https://news.ycombinator.com/item?id=47667192)
> > > > > > 
> > > > > > Yes
> > > > > > 
> > > > > > > **vecter** · [2026-04-06](https://news.ycombinator.com/item?id=47667214)
> > > > > > > 
> > > > > > > I'm open to hearing, please elaborate
> > > > 
> > > > > **nipponese** · [2026-04-07](https://news.ycombinator.com/item?id=47671212)
> > > > > 
> > > > > It's only slop if it's wrong or irrelevant.
> > 
> > > **JamesSwift** · [2026-04-06](https://news.ycombinator.com/item?id=47666007)
> > > 
> > > I commented on the GH issue, but Ive had effort set to 'high' for however long its been available and had a marked decline since... checks notes... about 23 March according to slack messages I sent to the team to see if I was alone (I wasnt).
> > > 
> > > EDIT: actually the first glaring issue I remember was on 20 March where it hallucinated a full sha from a short sha while updating my github actions version pinning. That follows a pattern of it making really egregious assumptions about things without first validating or checking. Ive also had it answer with hallucinated information instead of looking online first (to a higher degree than Ive been used to after using these models daily for the past ~6 months)
> > > 
> > > > **dev\_l1x\_be** · [2026-04-06](https://news.ycombinator.com/item?id=47666560)
> > > > 
> > > > It hallucinated a GUID for me instead of using the one in the RFC for webscokets. Fun part was that the beginning was the same. Then it hardcoded the unit tests to be green with the wrong GUID.
> > > > 
> > > > > **viktorianer** · [2026-04-07](https://news.ycombinator.com/item?id=47675184)
> > > > > 
> > > > > The hallucinated GUIDs are a class of failure that prompt instructions will never reliably prevent. The fix that worked: regex patterns running on every file the agent produces, before anything executes.
> > > > > 
> > > > > > **JamesSwift** · [2026-04-07](https://news.ycombinator.com/item?id=47675611)
> > > > > > 
> > > > > > Well Ive never had the issue before and have hit that / similar issues every few days over the past couple weeks.
> > 
> > > **DennisL123** · [2026-04-06](https://news.ycombinator.com/item?id=47666957)
> > > 
> > > Gotcha. It seemed though from the replies on the github ticket that at least some of the problem was unrelated to effort settings.

> **starkparker** · [2026-04-06](https://news.ycombinator.com/item?id=47664711)
> 
> \> You can also use the ULTRATHINK keyword to use high effort for a single turn
> 
> First I've heard that ultrathink was back. Much quieter walkback of [https://decodeclaude.com/ultrathink-deprecated/](https://decodeclaude.com/ultrathink-deprecated/)
> 
> > **giwook** · [2026-04-06](https://news.ycombinator.com/item?id=47666698)
> > 
> > Pretty sure it's still gone and you should be using effort level now for this.
> > 
> > > **xvector** · [2026-04-07](https://news.ycombinator.com/item?id=47671085)
> > > 
> > > No, ultrathink is back and it's the same thing as high effort for the message in which it is included
> > > 
> > > > **svnt** · [2026-04-07](https://news.ycombinator.com/item?id=47676280)
> > > > 
> > > > Right but wasn’t high effort the default effort before? So ultrathink is gone in all but name.

> **giancarlostoro** · [2026-04-07](https://news.ycombinator.com/item?id=47670192)
> 
> I only ever use high effort, the only thing I've run into sometimes I ask Claude to do every item on a list of items, and not stop until they're all done, it finishes maybe 80% of them then says "I've stopped doing things" for no reasonable reason. I don't need it to run for 18 hours nonstop, but 10 or 20 minutes more it would have kept going for wouldn't have hurt, especially when I am usually on Claude Code during off-hours, and on the Max plan.
> 
> Part of me wants to give lower "effort" a try, but I always wind up with a mess, I don't even like using Haiku or Sonnet, it feels like Haiku goofs, Haiku and Sonnet are better as subagent models where Opus tells them what to do and they do it from my experience.
> 
> > **theptip** · [2026-04-07](https://news.ycombinator.com/item?id=47670645)
> > 
> > I’ve been playing with
> > 
> > ```
> > /loop 5m check if you have any actionable tasks
> > ```
> > for this scenario.
> > 
> > > **giancarlostoro** · [2026-04-07](https://news.ycombinator.com/item?id=47674998)
> > > 
> > > Is that baked in?
> > > 
> > > > **theptip** · [2026-04-07](https://news.ycombinator.com/item?id=47679275)
> > > > 
> > > > Yeah, new feature dropped a couple weeks ago.
> > > > 
> > > > [https://code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)

> **tigershark** · [2026-04-07](https://news.ycombinator.com/item?id=47676015)
> 
> What change did you release on March 23rd when the subscription limits collapsed and they are still way down compared to what they used to be?

> **linsomniac** · [2026-04-07](https://news.ycombinator.com/item?id=47670277)
> 
> Hey Boris, thanks for this reply. I've been kind of scratching my head over this issue, assuming I'm just not doing "complex engineering", because since Opus 4.6 my seat-of-the-pants assessment is that it's a huge improvement. It's been like night and day in my use. Full disclosure: I use high effort for basically everything.

> **freeqaz** · [2026-04-07](https://news.ycombinator.com/item?id=47671723)
> 
> I have been wondering if 1 Million token context contributes here also. Compaction is much rarer now. How does that influence model performance? For some tasks I do, I feel like performance is worst now after this. Also Plan mode doesn't seem to wipe context anymore?
> 
> > **michaelashley29** · [2026-04-07](https://news.ycombinator.com/item?id=47675093)
> > 
> > i beg to differ. compaction happens alot for me, and at some point the output becomes extremely nonsensical

> **Jenk** · [2026-04-07](https://news.ycombinator.com/item?id=47673217)
> 
> Claude's settings don't appear to be in sync with the published settings schema\[0\].
> 
> \[0\]: [https://www.schemastore.org/claude-code-settings.json](https://www.schemastore.org/claude-code-settings.json).

> **niteshpant** · [2026-04-07](https://news.ycombinator.com/item?id=47669265)
> 
> I added \`CLAUDE\_CODE\_EFFORT\_LEVEL=max\` to my shell's env so that every session is always effort:max by default
> 
> :)
> 
> > **subscribed** · [2026-04-07](https://news.ycombinator.com/item?id=47672039)
> > 
> > Why would I use Claude otherwise anyway! :)

> **y1n0** · [2026-04-07](https://news.ycombinator.com/item?id=47669467)
> 
> "most users"
> 
> Have you guys considered that you should be optimizing for the leading tail of the user distribution? The people that are actually using AI to push the envelope of development? "most users," i.e. the inner 70%, aren't doing anything novel.

> **hellojimbo** · [2026-04-06](https://news.ycombinator.com/item?id=47668172)
> 
> The last time I typed ultrathink, i got a prompt saying that you no longer need to type ultrathink

> **sroussey** · [2026-04-07](https://news.ycombinator.com/item?id=47676381)
> 
> \> Roll it out with a dialog so users are aware of the change and have a chance to opt out
> 
> Here is the issue. Force a choice instead. Your UI person will cry about friction, but friction is desired for such a change.

> **matheusmoreira** · [2026-04-06](https://news.ycombinator.com/item?id=47665133)
> 
> I definitely noticed the mid-output self-correction reasoning loops mentioned in the GitHub issue in some conversations with Opus 4.6 with extended reasoning enabled on claude.ai. How do I max out the effort there?

> **ting0** · [2026-04-06](https://news.ycombinator.com/item?id=47664799)
> 
> Do you guys realize that everyone is switching to Codex because Claude Code is practically unusable now, even on a Max subscription? You ask it to do tasks, and it does 1/10th of them. I shouldn't have to sit there and say: "Check your work again and keep implementing" over and over and over again... Such a garbage experience.
> 
> Does Anthropic actually care? Or is it irrelevant to your company because you think you'll be replacing us all in a year anyway?
> 
> > **misnome** · [2026-04-06](https://news.ycombinator.com/item?id=47668515)
> > 
> > Or, ask it to make a plan, and it makes a good plan! It explicitly notes how validation is to take place on each stage!
> > 
> > And then does every stage without running any of the validation. It's your agent's plan, it should probably be generated in a way that your own agent can follow it.

> **diavelguru** · [2026-04-07](https://news.ycombinator.com/item?id=47669476)
> 
> As soon as that change came through I set the effort to high. Have not regretted it for any coding task. It feels the same as Dec-Jan though now spawning more sub agents which is not a bad thing.

> **erikpau** · [2026-04-07](https://news.ycombinator.com/item?id=47676293)
> 
> I'd hate to be that guy, but Opus not a very smart model when the effort is set to anything below high. I think, given the feedback from the community, this would be an obvious signal. However, moving the effort to anything beyond medium is a huge token burn. These issues didn't exist, or at least not this persistent, before the last 2 weeks. I, and perhaps a million or so other developers, would ask you to reconsider this thinking. I understand you need to run a business, but so do we, and Claude Opus is genius with a drinking problem, and you never really know upfront if it's drunk or not, but it's generally quite clear after a few minutes.
> 
> Other models, such as K2, GLM-5.1, and "the other one" seem to far less drunk than your approach, and you're losing fans quickly if you keep making these kind of changes to the tools or models.

> **zenoware** · [2026-04-07](https://news.ycombinator.com/item?id=47670040)
> 
> \> CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING
> 
> Why not just give people the abiltiy ot set a default thinking level instead of manually setting it to \`max\` all the time.

> **Jimpulse** · [2026-04-07](https://news.ycombinator.com/item?id=47682834)
> 
> Thanks for transparency here. Claude code if fun to use again! The thinking is huge when working with Claude as planner.

> **ting0** · [2026-04-06](https://news.ycombinator.com/item?id=47664872)
> 
> Thinking time is not the issue. The issue is that Claude does not actually complete tasks. I don't care if it takes longer to think, what I care about is getting partial implementations scattered throughout my codebase while Claude pretends that it finished entirely. You REALLY need to fix this, it's atrocious.

> **thomascountz** · [2026-04-07](https://news.ycombinator.com/item?id=47670962)
> 
> ```
> This beta header hides thinking from the UI, since most people don't look at it.
> ```
> How is this measured?
> 
> > **stingraycharles** · [2026-04-07](https://news.ycombinator.com/item?id=47671275)
> > 
> > And I wonder how redacting them reduces latency, as it sure as hell doesn’t make the responses any faster and bandwidth isn’t the issue here.
> > 
> > > **sothatsit** · [2026-04-07](https://news.ycombinator.com/item?id=47671479)
> > > 
> > > They provide thinking summaries, so I assume they have to call Haiku or some other model to summarise the thinking blocks.
> > > 
> > > > **stingraycharles** · [2026-04-07](https://news.ycombinator.com/item?id=47671942)
> > > > 
> > > > That’s not asynchronous? Wouldn’t it make more sense to disable those thinking summaries in those cases rather than hiding the thinking altogether?

> **saidnooneever** · [2026-04-07](https://news.ycombinator.com/item?id=47672036)
> 
> did the cost go up, or did you lower costs (token consumptions) for all users and then now want to default enterprise/teams back to normal mode. Because it seems like a long way aroundabout to say now it will cost more for same quality.

> **gnegggh** · [2026-04-07](https://news.ycombinator.com/item?id=47676710)
> 
> Last time quality was degraded like this it was impossible to get a refund.

> **j45** · [2026-04-06](https://news.ycombinator.com/item?id=47665499)
> 
> Thanks for the update,
> 
> Perhaps max users can be included in defaulting to different effort levels as well?

> **weakfish** · [2026-04-07](https://news.ycombinator.com/item?id=47677301)
> 
> Didn’t ULTRATHINK get deprecated? Last time I typed it I got a warning.

> **CjHuber** · [2026-04-07](https://news.ycombinator.com/item?id=47670748)
> 
> I honestly am very disappointed with this. I've only learned about CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING and showThinkingSummaries: true from this post. I've been wondering for a while where the summaries went and am always hoping like roulette that it thinks a lot. No wonder if there suddently is an "adaptive thinking" mode. I would have opted out 2 months ago if it was documented or communicated in any way publicly. Why change behavior without notice or any new user facing settings.
> 
> I just googled "CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING" and it seems like many people don't know about it.
> 
> And ULTRATHINK sets the effort to high, but then there is also /effort max?
> 
> > **triage8004** · [2026-04-07](https://news.ycombinator.com/item?id=47671654)
> > 
> > I'm now confused because I used to use ultrathink, went away as well as the chain of reasoning prompts, recently changed to high or extra thinking, now this is back?

> **raincole** · [2026-04-06](https://news.ycombinator.com/item?id=47664570)
> 
> \> I wanted to say I appreciate the depth of thinking & care that went into this.
> 
> The irony lol. The whole ticket is just AI-generated. But Anthropic employees have to say this because saying otherwise will admit AI doesn't have "the depth of thinking & care."
> 
> > **vlovich123** · [2026-04-06](https://news.ycombinator.com/item?id=47664652)
> > 
> > It's also pretty standard corporate speak to make sure you don't alienate any users / offend anyone. That's why corporate speak is so bland.
> > 
> > **rafaelmn** · [2026-04-06](https://news.ycombinator.com/item?id=47665493)
> > 
> > Ticket is AI generated but from what I've seen these guys have a harness to capture/analyze CC performance, so effort was made on the user side for sure.
> > 
> > > **notatallshaw** · [2026-04-06](https://news.ycombinator.com/item?id=47666228)
> > > 
> > > The note at the end of the post indicates the user asked Claude to review their own chat logs. It's impossible to tell if Claude used or built a a performance harness or just wrote those numbers based on vibes.
> > > 
> > > > **dreadnip** · [2026-04-07](https://news.ycombinator.com/item?id=47671520)
> > > > 
> > > > The whole issue is very obviously LLM generated nonsense. The stats are way too specific and reinforce the user’ bias in typical hallucinated fashion.
> > 
> > > **gardnr** · [2026-04-06](https://news.ycombinator.com/item?id=47666707)
> > > 
> > > There is this 3rd party tracker: [https://marginlab.ai/trackers/claude-code/](https://marginlab.ai/trackers/claude-code/)

> **jacquesm** · [2026-04-07](https://news.ycombinator.com/item?id=47670710)
> 
> Textbook example of how to respond to your customers, kudos.
> 
> > **stingraycharles** · [2026-04-07](https://news.ycombinator.com/item?id=47671262)
> > 
> > Is it?
> > 
> > I’m of the opinion that there’s more to it; obviously the thinking tokens aren’t having any reasonable impact on latency, given that bandwidth is hardly the bottleneck.
> > 
> > Seems more and more that Anthropic et al don’t want to give up their secret sauce / internals (which is their full right) and this is a step towards that direction, and it’s being presented as “reduces latency”.
> > 
> > > **dezgeg** · [2026-04-07](https://news.ycombinator.com/item?id=47672508)
> > > 
> > > I've understood that in more recent models you need to run extra compute to get a human-readable version of the thinking tokens, so it does impact latency. Though probably the more important motive is you can squeeze in more concurrent users by skipping this.
> > > 
> > > > **stingraycharles** · [2026-04-07](https://news.ycombinator.com/item?id=47672671)
> > > > 
> > > > No, that’s simply whether CoT is enabled or not. That actually *does* have impact.
> > > > 
> > > > What Anthropic is doing is still generating the thinking tokens (because they improve answer quality) without showing it to them. I believe this may actually hint at a future where these LLM vendors don’t want to show the internal reasoning like they do right now.
> > > > 
> > > > I’m very much of the opinion that hiding them from the response because it “improves latency” is nonsense.

> **foofloobar** · [2026-04-07](https://news.ycombinator.com/item?id=47678065)
> 
> Claude Code and Opus used to do a great job a few months ago. It seemed to get it right more often than not. It seemed to be far better at figuring out what has to be done and getting it right on the first attempt. This is likely model related since Claude Code has received some bug fixes since.
> 
> The list of bugs and performance problems appears to keep growing: reduced usage quotas, poor performance with numerous attempts at getting things right, cache invalidation bugs, background requests which have to be disabled explicitly to avoid consuming the quota too fast, Opus appears to be quantized even with high thinking mode, poor tool use with tool search disabled, broken tool search with tool search enabled, laziness, poor planning, poor execution, gets stuck when debugging simple code issues, writes code which isn't required, starts making changes and executing whatever it wants when told to simply prepare a plan for something, it doesn't follow instructions to use agents as told and numerous other issues with following the instructions.
> 
> The quota story is atrocious. It's difficult to get anything done with Claude Code due to the quota reduction. The cache invalidation bugs don't help either.
> 
> The tool use is also a pain to deal with. It appears to choose tools randomly with or without tool search. It keeps running custom CLI commands when it has instructions to use Makefile targets. It often ingests the output of some command with hundreds of lines of output without discrimination. It often uses lots of bash grep and find commands when it has better tools available to search across files and to use MCP tools which are far more efficient. It ignores MCP tools most of the time.
> 
> This doesn't appear to be an issue with the prompt itself. I'll try to fix the system prompt next to work around some of the issues. It seems to not follow instructions and to do whatever it feels like doing. It comes off as one of those Q2-Q3 quantized models from huggingface.
> 
> The impact of the cache invalidation issue, reduced quota, poor model performance and Claude Code bugs together have rendered this service almost entirely useless for me. The poor model performance means that many more attempts are required and more requests are made to the Anthropic API. The Claude Code bugs and design lead to cache invalidation more often. This makes the impact of the reduced quota even worse. It makes a lot more API requests because the model doesn't get it right on the first 1-2 attempts or because it chooses less than optimal strategies to find what it's looking for.
> 
> The communication and Anthropic's overall handling of the reported bugs and problems hasn't been that good either.
> 
> As for the session ID and other things you might request for debugging, there's nothing special here that's not reported widely on every Reddit thread from several subreddits. I use 200k context with Opus and Sonnet. I use high thinking mode because anything less appears to be complete garbage with extremely poor results. I avoid compact in favor of knowledge transfer markdown files.
> 
> It'd be great to see Anthropic fix the caching issues, to improve the quality of the model, to address the Claude Code bugs, to sort out the quota fiasco, to improve their communication skills, to communicate more with their customers and to be more proactive overall. I'll take my money elsewhere otherwise.

> **ctoth** · [2026-04-06](https://news.ycombinator.com/item?id=47664793)
> 
> Yeah LOL tell me I'm holding it wrong again. Actually Boris, I am tracking what is happening here. I see it, and I'm keeping receipts\[0\]. This started with the 4.6 rollout, specifically with the unearned confidence and not reading as much between writes. The flail quotient has gone right the hell up. If your evals aren't showing that then bully for your evals I reckon.
> 
> \[0\]: [https://github.com/ctoth/claude-failures](https://github.com/ctoth/claude-failures)
> 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47666326)
> > 
> > Christopher, would you be able to share the transcripts for that repo by running /bug? That would make the reports actionable for me to dig in and debug.
> > 
> > **quietsegfault** · [2026-04-06](https://news.ycombinator.com/item?id=47664853)
> > 
> > I’m not sure being confrontational like this really helps your case. There are real people responding, and even if you’re frustrated it doesn’t pay off to take that frustration out on the people willing to help.
> > 
> > > **ctoth** · [2026-04-06](https://news.ycombinator.com/item?id=47664933)
> > > 
> > > Fair point on tone. It's a bit of a bind isn't it? When you come with a well-researched issue as OP did, you get this bland corporate nonsense "don't believe your lyin' eyes, we didn't change anything major, you can fix it in settings."
> > > 
> > > How should you actually communicate in such a way that you are actually heard when this is the default wall you hit?
> > > 
> > > The author is in this thread saying every suggested setting is already maxed. The response is "try these settings." What's the productive version of pointing out that the answer doesn't address the evidence? Genuine question. I linked my repo because it's the most concrete example I have.
> > > 
> > > > **enraged\_camel** · [2026-04-06](https://news.ycombinator.com/item?id=47666836)
> > > > 
> > > > I read the entire performance degradation report in the OP, and Boris's response, and it seems that the overwhelming majority of the report's findings can indeed be explained by the \`showThinkingSummaries\` option being off by default as of recently.
> > > > 
> > > > **wonnage** · [2026-04-06](https://news.ycombinator.com/item?id=47665498)
> > > > 
> > > > Just use a different tool or stop vibe coding, it’s not that hard. I really don’t understand the logic of filing bug reports against the black box of AI
> > > > 
> > > > > **geysersam** · [2026-04-06](https://news.ycombinator.com/item?id=47666723)
> > > > > 
> > > > > People file tickets against closed source "black box" systems all the time. You could just as well say: Stop using MS SQL, just use a different tool, it's not that hard.
> > > > > 
> > > > > > **wonnage** · [2026-04-06](https://news.ycombinator.com/item?id=47668357)
> > > > > > 
> > > > > > Equivalent of filing a ticket against the slot machine when you lose more often than expected
> > > > > > 
> > > > > > > **HumanOstrich** · [2026-04-06](https://news.ycombinator.com/item?id=47668701)
> > > > > > > 
> > > > > > > Well now you're just being silly and I can't take you seriously.
> > > > 
> > > > > **HumanOstrich** · [2026-04-06](https://news.ycombinator.com/item?id=47668694)
> > > > > 
> > > > > The only "black box" here is Anthropic. At least an LLM's performance and consistency can be established by statistical methods.
> > 
> > > **malfist** · [2026-04-06](https://news.ycombinator.com/item?id=47664906)
> > > 
> > > Is somebody saying "you're holding it wrong" a "people willing to help"?
> > > 
> > > > **TeMPOraL** · [2026-04-06](https://news.ycombinator.com/item?id=47666455)
> > > > 
> > > > They are if you are, in fact, holding it wrong.
> > > > 
> > > > As was the usual case in most of the few years LLMs existed in this world.
> > > > 
> > > > Think not of iPhone antennas - think of a humble hammer. A hammer has three ends to hold by, and no amount of UI/UX and product design thinking will make the end you like to hold to be a good choice when you want to drive a Torx screw.
> > 
> > > **BigTTYGothGF** · [2026-04-06](https://news.ycombinator.com/item?id=47665545)
> > > 
> > > The stated policy of HN is "don't be mean to the openclaw people", let's see if it generalizes.
> 
> > **lambda** · [2026-04-06](https://news.ycombinator.com/item?id=47664994)
> > 
> > I guess one of the things I don't understand: how you expect a stochastic model, sold as a proprietary SaaS, with a proprietary (though briefly leaked) client, is supposed to be predictable in its behavior.
> > 
> > It seems like people are expecting LLM based coding to work in a predictable and controllable way. And, well, no, that's not how it works, and especially so when you're using a proprietary SaaS model where you can't control the exact model used, the inference setup its running on, the harness, the system prompts, etc. It's all just vibes, you're vibe coding and expecting consistency.
> > 
> > Now, if you were running a local weights model on your own inference setup, with an open source harness, you'd at least have some more control of the setup. Of course, it's still a stochastic model, trained on who knows what data scraped from the internet and generated from previous versions of the model; there will always be some non-determinism. But if you're running it yourself, you at least have some control and can potentially bisect configuration changes to find what caused particular behavior regressions.
> > 
> > > **dev\_l1x\_be** · [2026-04-06](https://news.ycombinator.com/item?id=47666511)
> > > 
> > > The problem is degradation. It was working much better before. There are many people (some example of a well know person\[0\]), including my circle of friends and me who were working on projects around the Opus 4.6 rollout time and suddenly our workflows started to degrade like crazy. If I did not have many quality gates between an LLM session and production I would have faced certain data loss and production outages just like some famous company did. The fun part is that the same workflow that was reliably going through the quality gates before suddenly failed with something trivial. I cannot pinpoint what exactly Claude changed but the degradation is there for sure. We are currently evaling alternatives to have an escape hatch (Kimi, Chatgpt, Qwen are so far the best candidates and Nemotron). The only issue with alternatives was (before the Claude leak) how well the agentic coding tool integrates with the model and the tool use, and there are several improvements happening already, like \[1\]. I am hoping the gap narrows and we can move off permanently. No more hoops, you are right, I should not have attempted to delete the production database moments.
> > > 
> > > [https://x.com/theo/status/2041111862113444221](https://x.com/theo/status/2041111862113444221)
> > > 
> > > [https://x.com/\_can1357/status/2021828033640911196](https://x.com/_can1357/status/2021828033640911196)
> > > 
> > > > **techpression** · [2026-04-07](https://news.ycombinator.com/item?id=47670723)
> > > > 
> > > > Curious as to how many people are using 4.6, perhaps you’re on a subscription? I use the api and 4.6 (also goes for Sonnet) is unusable since launch because it eats through tokens like it’s actually made that way (to make more money/hit limits faster). I guess it makes sense from a financial perspective but once 4.5 goes away I will have to find another provider if they continue like this :/
> > > > 
> > > > > **dev\_l1x\_be** · [2026-04-07](https://news.ycombinator.com/item?id=47671817)
> > > > > 
> > > > > We are on MAX.
> > 
> > > **stavros** · [2026-04-06](https://news.ycombinator.com/item?id=47666380)
> > > 
> > > Same as how I expect a coin to come up heads 50% of the time.
> > > 
> > > > **muyuu** · [2026-04-06](https://news.ycombinator.com/item?id=47667579)
> > > > 
> > > > If you get consistently nowhere near 50% then surely you know you're not throwing a fair coin? What would complaining to the coin provider achieve? Switch coins.
> > > > 
> > > > \*typo
> > > > 
> > > > > **stavros** · [2026-04-06](https://news.ycombinator.com/item?id=47667599)
> > > > > 
> > > > > Well I'm paying the coin to be near 50% and the coin's PM is listening to customers, so that's why.
> > > > > 
> > > > > > **muyuu** · [2026-04-06](https://news.ycombinator.com/item?id=47668046)
> > > > > > 
> > > > > > The coin's PM is spamming you trivial gaslighting corporate slop, most of it barely edited.
> > > > > > 
> > > > > > > **HumanOstrich** · [2026-04-06](https://news.ycombinator.com/item?id=47668737)
> > > > > > > 
> > > > > > > Yes, that's why we are angry. Stop making excuses for them.
> > 
> > > **randomNumber7** · [2026-04-06](https://news.ycombinator.com/item?id=47667197)
> > > 
> > > \> how you expect a stochastic model \[...\] is supposed to be predictable in its behavior.
> > > 
> > > I used it often enough to know that it will nail tasks I deem simple enough almost certainly.
> > > 
> > > **bwfan123** · [2026-04-07](https://news.ycombinator.com/item?id=47671080)
> > > 
> > > Imagine a team of human engineers. One day they are 10x ninjas and the next they are blub-coders. Not happening.
> > > 
> > > Put Claude on PIP.
> 
> > **malfist** · [2026-04-06](https://news.ycombinator.com/item?id=47664901)
> > 
> > It also completely ignores the increase in behavioral tracking metrics. 68% increase in swearing at the LLM for doing something wrong needs to be addressed and isn't just "you're holding it wrong"
> > 
> > > **alchemist1e9** · [2026-04-06](https://news.ycombinator.com/item?id=47666189)
> > > 
> > > I’m think a great marketing line for local/selfhosted LLMs in the future - “You can swear at your LLM and nobody will care!”
> 
> > **dang** · [2026-04-06](https://news.ycombinator.com/item?id=47667130)
> > 
> > Please don't post this aggressively to Hacker News. You can make your substantive points without that.
> > 
> > [https://news.ycombinator.com/newsguidelines.html](https://news.ycombinator.com/newsguidelines.html)
> > 
> > **bcherny** · [2026-04-06](https://news.ycombinator.com/item?id=47664760)
> > 
> > Yep totally -- think of this as "maximum effort". If a task doesn't need a lot of thinking tokens, then the model will choose a lower effort level for the task.
> > 
> > **koverstreet** · [2026-04-06](https://news.ycombinator.com/item?id=47664854)
> > 
> > Technically speaking, models inherently do this - CoT is just output tokens that aren't included in the final response because they're enclosed in <think> tags, and it's the model that decides when to close the tag. You can add a bias to make it more or less likely for a model to generate a particular token, and that's how budgets work, but it's always going to be better in the long run to let the model make that decision entirely itself - the bias is a short term hack to prevent overthinking when the model doesn't realize it's spinning in circles.
> > 
> > > **ai\_slop\_hater** · [2026-04-06](https://news.ycombinator.com/item?id=47664916)
> > > 
> > > \> You can add a bias to make it more or less likely for a model to generate a particular token, and that's how budgets work
> > > 
> > > Do you have a source for this? I am interested in learning more about how this works.
> > > 
> > > > **koverstreet** · [2026-04-06](https://news.ycombinator.com/item?id=47665102)
> > > > 
> > > > It's how temperature/top\_p/top\_k work. Anthropic also just put out a paper where they were doing a much more advanced version of this, mapping out functional states within the modern and steering with that.
> > > > 
> > > > > **ai\_slop\_hater** · [2026-04-06](https://news.ycombinator.com/item?id=47665118)
> > > > > 
> > > > > Huh, I wonder if that's why you cannot change the temperature when thinking is enabled. Do you have a link for the paper?
> > > > > 
> > > > > > **koverstreet** · [2026-04-06](https://news.ycombinator.com/item?id=47665173)
> > > > > > 
> > > > > > [https://transformer-circuits.pub/2026/emotions/index.html](https://transformer-circuits.pub/2026/emotions/index.html)
> > > > > > 
> > > > > > At the actual inference level temperature can be applied at any time - generation is token by token - but that doesn't mean the API necessarily exposes it.
> > > > > > 
> > > > > > > **ai\_slop\_hater** · [2026-04-06](https://news.ycombinator.com/item?id=47665203)
> > > > > > > 
> > > > > > > Thanks. I was referring to the fact that Anthropic, in their API, prohibits setting temperature when thinking is enabled.

> **nickvec** · [2026-04-06](https://news.ycombinator.com/item?id=47666151)
> 
> Hey Boris, would appreciate if you could respond to my DM on X about Claude erroneously charging me $200 in extra credit usage when I wasn't using the service. Haven't heard back from Claude Support in over a month and I am getting a bit frustrated.
> 
> > **HumanOstrich** · [2026-04-06](https://news.ycombinator.com/item?id=47668750)
> > 
> > Did the receipt show it as being a gift? There's a lot of fraud happening the past few months with Claude Code Gift purchases. Anthropic support is ignoring all of it and just not responding to support requests.
> > 
> > Happened to a close friend of mine. A bit of digging revealed the same pattern with fraudulent gift purchases for several other people before I stopped looking. They were also being ignored by Anthropic support. One since January.
> > 
> > Apparently they're so short on inference resources they can't run their support bots. Maybe banning usage of Claude Code with Claude will allow them to catch up on those gift fraud tickets.
> > 
> > Took a long time for me to reach this level of scathing. It is not unwarranted.
> > 
> > > **nickvec** · [2026-04-07](https://news.ycombinator.com/item?id=47678808)
> > > 
> > > No, the receipt had no indication of it being a gift. Was with my family at the time and suddenly started getting $10 extra usage charges every few minutes. I wasn’t able to toggle off the “auto-reload funds” feature until about $180 had been drained from my checkings. For context, here’s the support ticket I sent in on March 7th.
> > > 
> > > “Hi Anthropic Support,
> > > 
> > > I'm a Max plan subscriber and I'm writing about approximately $180 in unexpected Extra Usage charges that appeared on my account between March 3-5, 2026. I attempted to resolve this through your Fin AI chatbot (Conversation ID: 215473382652967).
> > > 
> > > Here's the situation: - I received 16 separate Extra Usage invoices between March 3-5, ranging from $10-$13 each, all charged automatically. - I was not actively using Claude during this period — I was away from my laptop entirely. - When I checked my usage dashboard, it showed my session at 100% usage despite me not using the product. - My API usage dashboard shows only $70 in total lifetime usage, confirming this is not API-related. - My Claude Code session history shows only two tiny sessions from March 5 totaling under 7KB — nowhere near enough activity to generate these charges.
> > > 
> > > This appears consistent with known billing/usage tracking issues reported by other Max plan users (GitHub issues #29289 and #24727 on the anthropics/claude-code repo), where usage meters show incorrect values and Extra Usage charges accumulate erroneously. However, it is possible that my account was compromised, and I would like assistance determining if that is the case (or if it really is a bug.)
> > > 
> > > Either way, I am requesting a refund of the Extra Usage charges from March 3-5 only — I do not want to cancel my subscription.”
> > > 
> > > **subscribed** · [2026-04-07](https://news.ycombinator.com/item?id=47672021)
> > > 
> > > Still, its on Anthropic to respond to it.
> > > 
> > > When a third party leaked my CC number which then was used to buy Spotify premium, all it took was 10 minutes of chat with a very polite support agent to have it resolved.
> > > 
> > > Ignoring the customer is not going to fix it. They'd know if they asked Claude.

> **areoform** · [2026-04-06](https://news.ycombinator.com/item?id=47665993)
> 
> Hey Boris, thanks for the awesomeness that's Claude! You've genuinely changed the life of quite a few young people across the world. :)
> 
> not sure if the team is aware of this, but Claude code (cc from here on) fails to install / initiate on Windows 10; precise version, Windows 10.0.19045 build 19045. It fails mid setup, and sometimes fails to throw up a log. It simply calls it quits and terminates.
> 
> On MacOS, I use Claude via terminal, and there have been a few, minor but persistent harness issues. For example, cc isn't able to use Claude for Chrome. It has worked once and only once, and never again. Currently, it fails without a descriptive log or issue. It simply states permission has been denied.
> 
> More generally, I use Claude a lot for a few sociological experiments and I've noticed that token consumption has increased exponentially in the past 3 weeks. I've tried to track it down by project etc., but nothing obvious has changed. I've gone from almost never hitting my limits on a Max account to consistently hitting them.
> 
> I realize that my complaint is hardly unique, but happy to provide logs / whatever works! :)
> 
> And yeah, thanks again for Claude! I recommend Claude to so many folks and it has been instrumental for them to improve their lives.
> 
> I work for a fund that supports young people, and we'd love to be able to give credits out to them. I tried to reach out via the website etc. but wasn't able to get in touch with anyone. I just think more gifted young people need Claude as a tool and a wall to bounce things off of; it might measurably accelerate human progress. (that's partly the experiment!)
> 
> > **oriettaxx** · [2026-04-07](https://news.ycombinator.com/item?id=47671848)
> > 
> > why is this post down graded?
> > 
> > > **areoform** · [2026-04-07](https://news.ycombinator.com/item?id=47682604)
> > > 
> > > I angered the mob elsewhere by being a heretic.