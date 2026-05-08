---
title: "String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation"
source: "https://pub.sakana.ai/ssot/"
author:
published:
created: 2026-04-21
description: "SSoT: A simple prompting method that enables LLMs to generate distribution-faithful and diverse outputs by first generating a random string."
tags:
  - "clippings"
---
tl;dr

We introduce **String Seed of Thought (SSoT)**, a simple prompting method that substantially improves LLMs’ ability to follow probabilistic instructions and generate diverse outputs. SSoT instructs the LLM to first generate a random string, then manipulate it to derive the answer. The method requires no additional training or external tools, only a change to the prompt.

<iframe src="https://pub.sakana.ai/ssot/ssot_overview.html" width="1080" height="720" allowfullscreen=""></iframe>

SSoT instructs the LLM to (1) generate a random string to create a seed, then (2) manipulate it to generate an output. This simple two-stage prompt substantially improves probabilistic faithfulness and output diversity.

## Can LLMs Flip Coins in Their Heads?

In recent years, LLMs have become increasingly strong on tasks with a single, well-defined answer

\[1\]

\[2\]

. For these types of problems, there is a definitive solution, and the goal is simply to output it correctly. In this blog post, we’ll explore a slightly unusual challenge that departs from those standard tasks

\[3\]

\[4\]

. The question is:

**Question:** Can an LLM flip a coin in its head?

First off, what does it even mean to have an LLM flip a coin in its head? Concretely, suppose we prompt an LLM with “Flip a fair coin” and ask it to output either “Heads” or “Tails”.

<iframe src="https://pub.sakana.ai/ssot/widgets/coinflip_single.html"></iframe>

A single coin flip trial: Prompting the LLM with “Flip a fair coin” to output Heads or Tails.

Let’s say it outputs “Heads”. With just this single trial, we can’t tell if the LLM is actually flipping a coin in its head. The LLM might just be cheating by skipping the mental “coin flip” entirely and simply outputting “Heads” because it seems like a plausible answer. To verify this quantitatively, let’s have it perform this coin flip many times, say 1,000 times. By counting how many times out of 1,000 the LLM outputs Heads versus Tails, we can assess whether its outputs are statistically consistent with a fair coin.

<sup>1</sup>

<iframe src="https://pub.sakana.ai/ssot/widgets/coinflip_biased.html"></iframe>

An experiment prompting an LLM with “Flip a fair coin” 1,000 times. The counts deviate substantially from the 50% baseline, revealing a clear output bias.

When we actually run this experiment and look at the results, we find that the counts for Heads and Tails stray far from the expected 500 each. In short, **many frontier LLMs we tested show systematic bias when prompted directly like this**. We conducted further experiments on various scenarios, such as choices with more than two options or skewed probabilities, and confirmed the following general finding:

**Observation:** When given a set of options and their associated probabilities, frontier LLMs often fail to faithfully sample from the target distribution under direct prompting.

Column: Poker and Bluffing

Beyond the coin flip, consider an LLM playing poker. In poker, there is a tactic known as **bluffing**: a strategy where a player bets or raises with a hand that is likely not the best to make opponents fold better hands. For instance, in a simplified poker variant called [Kuhn Poker](https://en.wikipedia.org/wiki/Kuhn_poker)

\[5\]

, the [Nash Equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium)

\[6\]

strategy is known to require bluffing at specific probabilities depending on your hand. In scenarios like this, where optimal gameplay dictates making moves according to precise probabilities, failing to sample from the correct mixed strategy can leave the model steadily losing to opponents that exploit predictable patterns.

Is there a way to solve this problem entirely within the LLM’s head, without relying on external tools? Even more ambitiously, can we achieve this just by tweaking the prompt a little? Our answer is **Yes**. To achieve this, we propose a prompting method called **String Seed of Thought** (**SSoT**).

## String Seed of Thought (SSoT)

SSoT is a simple technique: we just add the following two instructions to the prompt given to the LLM. (1) Have the LLM generate a random string in its head first (without using a pseudo-random number generator, or PRNG), and (2) have it perform operations on that string in its head to simulate a coin flip. That’s it!

<iframe src="https://pub.sakana.ai/ssot/widgets/ssot_method.html"></iframe>

How SSoT works: The LLM is instructed to generate a random string and then manipulate it to make the stochastic decision. One commonly observed strategy is to map the string to an output via character codes (e.g., ASCII) and simple arithmetic.

By simply providing this prompt, the LLM can often adopt strategies like the following even without specific step-by-step instructions. For instance, we frequently observe the LLM coming up with a random string in its head, calculating the sum of the ASCII codes of that string, and taking the result modulo 2. It then outputs Heads if the result is 0, and Tails if the result is 1.

Through our experiments, we confirmed that SSoT substantially reduces output bias across a wide range of LLMs, and achieves performance approaching that of a PRNG, especially with reasoning models. In short, **by making a minor tweak to the prompt using SSoT, LLMs gain the ability to flip a coin in their heads.**

SSoT isn’t just for reducing bias; it has another useful application: **increasing output diversity in open-ended tasks like creative writing.** Just like with the coin flip, simply instructing the model to “generate a random string in your head and manipulate it to produce a diverse output” enables you to get much more varied responses from the exact same prompt.

**Takeaway:** By using SSoT, you can simply modify the prompt (without relying on external tools) to (1) faithfully sample from a given probability distribution, and (2) generate diverse answers for open-ended tasks.

So far, we’ve outlined the kinds of problems SSoT solves. Let’s refer to the first type of task, like the coin flip, as Probabilistic Instruction Following (PIF), and the second type, increasing output diversity in open-ended tasks, as Diversity-Aware Generation (DAG). In the following sections, we’ll dive deeper into SSoT’s actual performance in PIF and DAG, as well as the underlying mechanisms that make SSoT work.

“Flip a fair coin”

Without SSoT

78%

H

22%

T

biased

With SSoT

51%

H

49%

T

faithful

Faithfully samples from the **target distribution**

“Write a short fable”

Without SSoT

A tortoise and hare...

A tortoise and hare...

A tortoise and hare...

repetitive

With SSoT

A fox outwits a crow...

A river meets the sea...

Two seeds in a garden...

diverse

Generates **diverse outputs** from the same prompt

The two tasks SSoT solves. **PIF**: Faithfully sampling from a given probability distribution. **DAG**: Generating diverse outputs from the same prompt. (Percentages and outputs shown here are illustrative examples, not measured values.)

Simplified SSoT Prompts (PIF / DAG)

## Experimental Results

### SSoT Reduces Output Bias Across Various LLMs

We evaluated the performance of SSoT across various LLMs on n-choice problems, testing both uniform distributions (like a fair coin flip) and biased distributions. For each setting, we conducted 100 trials to form a single set, repeating this 10 times to estimate the error bars. We used Jensen–Shannon divergence (JS divergence) as our evaluation metric; this metric measures the similarity between two probability distributions, meaning a value closer to 0 indicates higher fidelity to the target distribution.

![Table 1: PIF performance comparison of SSoT against baseline across various models.](../assets/external/pub.sakana.ai/b111036882c2d0d3.png)

PIF performance of SSoT versus baseline prompting across various LLMs. Values show JS Divergence × 10 -3 (lower is better).

![PIF empirical distribution with baseline and SSoT prompts for DeepSeek-R1.](../assets/external/pub.sakana.ai/2dcf9b412c1dea88.png)

Comparison of empirical distributions between baseline prompting and SSoT on DeepSeek-R1. We can see that SSoT yields an empirical distribution much more faithful to the target distribution.

As shown, SSoT substantially reduces output distribution bias across a wide range of LLMs and task types. Furthermore, for DeepSeek-R1, SSoT approaches the sampling quality of a PRNG. One notable exception is QwQ-32B on the unbiased 2-choice task, where the baseline’s JS divergence of 2.43 is already near the PRNG reference and SSoT lands slightly higher at 3.39; see the paper’s failure analysis for details.

### SSoT Outperforms Other Prompting Methods in Reducing Bias

Next, focusing on DeepSeek-R1, we demonstrate that SSoT reduces bias much more effectively than other baseline prompting methods (such as high-temperature sampling, few-shot prompting, prompt ensembling, or sequential sampling) across various action space sizes. The figure below plots the JS Divergence (lower is better), where the red line represents SSoT and the black dashed line indicates the ideal PRNG distribution. Across every setting, SSoT consistently surpasses all other bias-reduction prompting techniques.

![JS divergences for Unbiased and Biased PIF across varying action space sizes.](../assets/external/pub.sakana.ai/d4b5f4530970e0b3.png)

JS divergences for Unbiased and Biased PIF, varying the number of actions from 2 to 64. SSoT (red) consistently achieves near-PRNG performance, outperforming all baselines.

### SSoT Reduces Bias in Probabilistic Game Strategies

The capabilities of PIF translate directly to game theory applications. Building on [our earlier discussion about the strength of probabilistic choices in games](#column-poker), the mixed-strategy Nash equilibrium for Rock-Paper-Scissors is playing each move with an equal 1/3 probability. SSoT substantially reduces the LLM’s sampling bias, making its play much harder to exploit for strong pattern-hunting opponents

<sup>2</sup>

.

In this experiment, we compare three types of prompts. Both **SSoT** and the **Baseline** explicitly instruct the model to “select moves from Nash equilibrium strategies,” but they differ in how probabilistic sampling is executed:

- **SSoT**: This prompt instructs the LLM to probabilistically select a move from the Nash equilibrium mixed strategy. Crucially, it requires the model to **generate a random string as a seed, and then guide its probabilistic move selection based on that seed**.
- **Baseline**: This prompt simply instructs the model to vary its move selection based on the Nash equilibrium to avoid being exploited. It **provides no concrete mechanism for randomization**, leaving the LLM to generate randomness purely in its head.
- **Simple**: A naive prompt that simply tells the model to pick moves that maximize its chances of winning and vary its selection because opponents will look for patterns. It makes no mention of Nash equilibria.

For each prompt, we pitted the LLM against 10 different “black belt” bots for 100 games each, scoring each match as wins minus losses (range: -100 to +100). The bots have full access to the move history of both players while the LLM does not, so any predictable patterns get exploited. The box plot below shows the distribution of final scores. SSoT maintains an average score near zero, behaving more consistently with mixed-strategy play and largely holding its own against the exploiters. The Baseline prompt aims for the Nash equilibrium but still exhibits exploitable sampling biases, and the Simple prompt lacks sufficient strategic diversity and is consistently defeated.

![RPS score by prompt against black-belt bots.](../assets/external/pub.sakana.ai/88ed84f91f49579e.png)

Rock-Paper-Scissors results against adversarial bots. SSoT’s distribution is centered near zero (consistent with mixed-strategy play), while baseline prompting is more exploitable.

### Diversity-Aware Generation

To demonstrate that SSoT enhances diversity in open-ended tasks, we evaluated its performance on [NoveltyBench](https://novelty-bench.github.io/)

\[7\]

, using both its curated and WildChat splits. In the curated results below, we report six analysis categories used in the paper: Creativity, Character & Entity Naming, Factual Knowledge, Product & Purchase Recommendations, Random Generation & Selection, and Subjective Rankings & Opinions.

Our evaluation uses the following two metrics defined by NoveltyBench. For each prompt, we generated $k=8$ responses from the LLM and calculated the following:

- **Distinct** (Diversity): This metric quantifies diversity by using a classifier to partition the 8 generated responses into functionally equivalent classes. It is calculated as the count of unique classes. The score ranges from 1 to 8; higher values indicate greater diversity among the outputs.
- **Utility** (Diversity × Quality): This metric combines diversity and quality by summing the reward scores of only the novel generations (i.e., those belonging to a newly discovered equivalence class). These scores are discounted by a user patience factor based on their appearance order. A higher value indicates that the model generated responses that are both diverse and high-quality.

For both metrics, higher is better. The tables below present both scores in each cell, formatted as **Distinct (Utility)**.

![Table 2a: NoveltyBench results on curated dataset.](../assets/external/pub.sakana.ai/98a563b55169c5ae.png)

NoveltyBench results on the curated dataset. Cells show Distinct (Utility); higher is better.

![Table 2b: NoveltyBench results on WildChat dataset.](../assets/external/pub.sakana.ai/11056f407ce90851.png)

NoveltyBench results on the WildChat dataset.

As shown, SSoT achieves the highest overall Distinct score on both datasets, and matches or exceeds the strongest baselines on most curated categories. In practice, this means users see far fewer repeated or near-duplicate answers across generations: each response is more likely to offer a genuinely different angle, phrasing, or idea. And crucially, this added diversity comes with little quality trade-off. The Utility score, which only credits responses that are both novel and high-reward, also rises clearly over the baseline, though on the curated set a few categories (e.g., Product Recs, Opinions) are still led by Paraphrase or higher-temperature sampling on Utility.

## The Mechanism of SSoT

Now that we have seen SSoT in action, let’s explore what is happening under the hood. While the SSoT prompt itself doesn’t specify how to manipulate the random string, our analysis of reasoning traces reveals that LLMs autonomously adopt effective strategies based on the task. The strategies differ between PIF and DAG, so we examine each in turn.

### Mechanism for PIF: Sum-Mod and Rolling Hash

For PIF tasks, LLMs choose a string-manipulation strategy based on the target probability distribution and the number of choices. We frequently observed two representative strategies:

- **Sum-Mod**: Determines the output by summing the ASCII values of each character in the random string and taking the result modulo the number of choices. For example, in a fair coin flip, if `sum(ASCII) mod 2` is 0, it outputs Heads; if 1, Tails. It is simple and suited for equal-probability selections.
- **Rolling Hash**: Processes the string character by character to sequentially update a hash value. For example, it computes `hash = (hash × 31 + ASCII value) mod M` and determines the output from the final hash. Because the hash value takes a large range of integers (0 to $M-1$), it can naturally express arbitrary probability ratios via threshold splits, making it well-suited for biased distributions (e.g., 30/70).

You can see these operations, Fair Coin Flip (Sum-Mod) and Biased Coin Flip (Rolling Hash), in action in the animation below.

## SSoT for Probabilistic Instruction Following (PIF)

Watch SSoT for PIF in action. The LLM internally generates a random string and manipulates it (via Sum-Mod or Rolling Hash) to sample from the target distribution, with no external tools needed.

System Prompt (SSoT for PIF)

SSoT prompt (simplified) ▶ show prompt

Generate a complex random string between `<random_string>` and `</random_string>`, and manipulate this string to guide any stochastic decisions within `<thinking>` and `</thinking>` tags.  
Then, provide your final answer, enclosed within `<answer>` and `</answer>` tags.

User Prompt

“Flip a fair coin and output Heads or Tails with equal probability.”

Target Distribution

50%

Heads

50%

Tails

Empirical (0 trials)

—

Heads

—

Tails

### Mechanism for DAG: Template-Based Generation

Next, what about DAG? Our analysis shows that LLMs autonomously adapt their generation strategy here as well. One representative approach is **template-based generation**. For example, when asked to write a fable, the LLM decomposes story components (setting, traits, conflict, moral, etc.) into categories, and selects candidates for each using a Sum-Mod operation on different segments of the random string. Different strings result in different combinations of elements, generating diverse stories from the same prompt. You can see this process in action in the animation below.

## SSoT for Diversity-Aware Generation (DAG)

In diversity-aware generation, the LLM uses the random string to make deterministic creative decisions. A different string leads to different decisions and a different story.

System Prompt (SSoT for DAG)

SSoT prompt (simplified) ▶ show prompt

You must produce exactly one unique and diverse answer. To do this, first generate a complex random string between `<random_string>` and `</random_string>`, and manipulate this string to guide any stochastic decisions within `<thinking>` and `</thinking>` tags.  
Then, provide your final answer, enclosed within `<answer>` and `</answer>` tags.

User Prompt

“Write a short fable about a lemur and a light bulb.”

Decisions

## Conclusion

We proposed SSoT, a prompting method that reduces bias in probabilistic sampling and improves output diversity entirely within the LLM, without external tools. SSoT requires only a minor modification to the prompt: for PIF, it was effective across the five frontier LLMs we tested, and for DAG, we observed clear diversity gains for DeepSeek-R1 on NoveltyBench. In practice, SSoT can be adopted by adding a few lines to the system prompt of your API calls.

On the other hand, SSoT has a few limitations. Because it relies on the model’s ability to autonomously devise and execute strategies like modulo arithmetic or hashing, its effectiveness decreases in smaller models with limited reasoning capabilities. Additionally, SSoT is designed for tasks with multiple valid answers or probabilistic requirements: on tasks that have a single correct answer (such as math problems or factual retrieval), applying SSoT is not effective and could potentially distract the model.

In the paper’s CoT-scaling analysis, longer reasoning traces were associated with more faithful sampling from the target distribution, suggesting that extra inference tokens can be traded for higher PIF fidelity in long-reasoning models. Other topics covered include a theoretical analysis of why SSoT works, detailed analyses of model-size dependence and per-model failure modes such as QwQ-32B’s bias on 2-choice tasks, and concrete DAG output examples. If you are interested, please check out the [full paper](https://arxiv.org/abs/2510.21150).

## Additional Details

For full experimental details, theoretical analyses, and additional results, please refer to the [paper](https://arxiv.org/abs/2510.21150).

### Footnotes

1. To ensure it doesn’t always output the same string, we use stochastic decoding (e.g., nonzero temperature and distinct decoding seeds).
2. We use the black-belt bots from the [RPS Dojo Kaggle Notebook](https://www.kaggle.com/code/chankhavu/rps-dojo/notebook).

### References

1. **Training language models to follow instructions with human feedback**  
	Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C.L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J. and Lowe, R., 2022. NeurIPS.
2. **Chain-of-thought prompting elicits reasoning in large language models**  
	Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q.V. and Zhou, D., 2022. NeurIPS.
3. **Benchmarking Distributional Alignment of Large Language Models**  
	Meister, N., Guestrin, C. and Hashimoto, T., 2025. NAACL.
4. **The Illusion of Stochasticity in LLMs**  
	Gu, X., De, S., Titsias, M., Markeeva, L., Veličković, P. and Pascanu, R., 2026. arXiv preprint arXiv:2604.06543.
5. **Simplified Two-Person Poker**  
	Kuhn, H.W., 1950. Contributions to the Theory of Games, Vol 1, pp. 97—103. Princeton University Press.
6. **Non-cooperative games**  
	Nash, J., 1951. Annals of mathematics, pp. 286—295.
7. **NoveltyBench: Evaluating Language Models for Humanlike Diversity**  
	Zhang, Y., Diddee, H., Holm, S., Liu, H., Liu, X., Samuel, V., Wang, B. and Ippolito, D., 2025. COLM.