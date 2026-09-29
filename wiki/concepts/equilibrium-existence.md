# Equilibrium existence (a resting point is not a location)

## Definition (working)

An equilibrium is a strategy profile nobody wants to leave given the others. **Existence** says such a profile is in the set. It does not say which one, that there is only one, or that a nearby game has a nearby one.

Working source: lecture 5 of [[wiki/sources/mit-6-254-game-theory-ozdaglar]] (Ozdaglar, 18 February 2010). The lecture does not invent the theorems. It states them and proves the finite case.

```
does a resting point exist?
        │
        ├─ finite action lists
        │     → mixed Nash always (Nash; best response has a fixed point)
        ├─ a continuum of actions, own payoff concave
        │     → pure Nash (Debreu–Glicksberg–Fan)
        ├─ a continuum, payoff merely continuous
        │     → mixed Nash (Glicksberg; proof not in this lecture)
        └─ continuum, not concave
              → pure Nash can fail (their example 2)
                       └─ "the equilibrium price" is then not a thing
```

## The finite case, as this lecture uses it

A mixed profile is a Nash equilibrium exactly when each player's mixture is a best response to the others. So existence is a fixed point of the best-response correspondence. Kakutani supplies the fixed point when the set is compact and convex, and the correspondence is nonempty, convex-valued, and closed-graph. For a finite game the mixed-strategy set is a product of simplices, and linearity of payoff in one's own mixture gives nonempty (Weierstrass), convex, and — with continuity — closed. The fixed point is a mixed equilibrium. Matching pennies is the named corollary: no pure equilibrium, so the mixed one is the whole content of the theorem.

## Where it fails

Debreu–Glicksberg–Fan needs three things for a *pure* equilibrium on infinite strategy sets: compact convex sets, continuity in the opponents' actions, concavity (quasi-concavity suffices) in one's own. Nash's theorem is this one with simplices and linear utility. Drop concavity and the lecture's second pricing game has a profitable deviation at every candidate pure price pair. Drop to mere continuity and Glicksberg still promises a *mixed* equilibrium, but the strategy space is infinite-dimensional and the proof is deferred to the next lecture (unread here).

Closed graph is not continuity. If payoffs move continuously with a parameter, the equilibrium correspondence has a closed graph. The slides say this does not make the set continuous: a small parameter change need not move the equilibrium a small amount.

## Why it matters for `pro/plan`

- One floor under [[wiki/concepts/margin-and-constraint]]. Naming the margin a policy moves is useful only if that margin has a resting point. A price-competition story whose payoff is not concave in own price may have no pure equilibrium to cite.
- [[wiki/concepts/causal-analysis]]: "a pure equilibrium exists" and "they play this profile" are different claims. Example 1 supports both (unique pure point at prices (1, 1/2), under an assumption proved elsewhere). Example 2 supports neither.
- [[wiki/concepts/efficiency-metric]]: the existence proof is the cheap step. Locating the equilibrium is lecture 9, not read here, and is the expensive one. Don't spend the location budget before the hypotheses hold.
- Not a claim that these proofs were checked line by line. The PDF's glyph encoding scrambles subscripts; statements and the two example conclusions were readable, intermediate algebra was not.

## Related

- Source: [[wiki/sources/mit-6-254-game-theory-ozdaglar]]
- Which margin: [[wiki/concepts/margin-and-constraint]]
- Don't collapse existence into the played profile: [[wiki/concepts/causal-analysis]]
- Existence is cheap, location is not: [[wiki/concepts/efficiency-metric]]
- Why the hypotheses outlast the 2007 routing paper: [[wiki/concepts/barbell-strategy]]
