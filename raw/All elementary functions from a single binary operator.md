---
title: "All elementary functions from a single binary operator"
source: "https://www.alphaxiv.org/abs/2603.21852v2"
author:
  - "[[Andrzej Odrzywołek]]"
published: 2026-04-04
created: 2026-04-14
description: "View 1 comment: Cool thing :)"
tags:
  - "clippings"
---
[Paper](https://www.alphaxiv.org/abs/2603.21852v2) [Blog](https://www.alphaxiv.org/overview/2603.21852v2) [Resources](https://www.alphaxiv.org/resources/2603.21852v2)

/ 23

All elementary functions from a single operator  
Andrzej Odrzywo lek  
Institute of Theoretical Physics, Jagiellonian University, 30-348 Krakow, Poland  
E-mail: andrzej.odrzywolek@uj.edu.pl  
  
Abstract  
A single two-input gate suffices for all of Boolean logic in digital hardware. No com-  
parable primitive has been known for continuous mathematics: computing elementary  
functions such as sin, cos,√, and log has always required multiple distinct operations.  
Here we show that a single binary operator,  
eml(x, y) = exp(x) − ln(y),  
together with the constant 1, generates the standard repertoire of a scientific calcula-  
tor.This includes constants such as e,π, and i; arithmetic operations including +,  
−,×,/, and exponentiation as well as the usual transcendental and algebraic func-  
tions.For example,e x \= eml(x,1), ln x \= eml(1,eml(eml(1, x),1)), and likewise for  
all other operations.That such an operator exists was not anticipated; I found it  
by systematic exhaustive search and established constructively that it suffices for the  
concrete scientific-calculator basis.In EML (Exp-Minus-Log) form, every such ex-  
pression becomes a binary tree of identical nodes, yielding a grammar as simple as  
S → 1 | eml(S, S).This uniform structure also enables gradient-based symbolic re-  
gression:using EML trees as trainable circuits with standard optimizers (Adam), I  
demonstrate the feasibility of exact recovery of closed-form elementary functions from  
numerical data at shallow tree depths up to 4. The same architecture can fit arbitrary  
data, but when the generating law is elementary, it may recover the exact formula.  
1  
arXiv:2603.21852v2 \[cs.SC\] 4 Apr 2026

Summary paragraph  
Elementary functions such as exponentiation, logarithms and trigonometric functions are  
the standard vocabulary of STEM education.Each comes with its own rules and a dedi-  
cated button on a scientific calculator; our derivations rely on many of them simultaneously,  
even though we know they are heavily redundant and can be expressed through one an-  
other, e.g.sin x \= cos(x − π/ 2),√ x \= x 1 / 2, etc.They are the workhorse of quantitative  
science, appearing in basic and empirical laws and inside the engines of numerical methods  
like differential equation solvers, integration quadratures and Fourier analysis \[1\]. In digital  
electronics, a remarkable fact underlies universality:a single two-input gate, NAND (the  
Sheffer stroke), suffices to build any Boolean circuit \[2\]. Continuous mathematics has lacked  
such a primitive: calculators must expose many distinct buttons. Classical reductions, from  
logarithm tables \[3, 4\] and the slide rule through Euler’s formula \[5\] to the exp-log repre-  
sentation \[6\] with algebraic adjunctions \[7\], reduced them to a few, but no further. Despite  
this, it remains unclear whether this apparent diversity is intrinsic, or whether a smaller  
generative basis exists. Here we show that the operator eml(x, y) = exp(x) − ln(y), together  
with the constant 1, does exactly that: it reconstructs arithmetic, all standard elementary  
transcendental functions, and constants including integers, fractions, radicals,e,π and i. In  
simpler terms, a two-button calculator (1,eml) suffices for everything a full scientific calcula-  
tor can do. Existence of the EML operator reveals that elementary functions are members of  
a much simpler class than previously recognized. Every EML expression is a binary tree of  
identical nodes, yielding an exceptionally simple grammar:S → 1 | eml(S, S), a context-free  
language that is isomorphic to well-studied combinatorial objects like full binary trees and  
Catalan structures. Elementary formulas become circuits \[8\] composed of identical elements,  
much like digital hardware built from NAND gates. This uniform representation provides a  
complete and regular search space for continuous symbolic regression \[9, 10\]: parameterized  
EML trees can be optimized by standard gradient methods, and when the generating law  
is elementary, trained weights can snap to exact closed-form expressions. In effect, a single  
trainable architecture gains the potential to discover \[11\] any elementary formula from data.  
The EML operator may be the tip of an iceberg. Preliminary searches have already returned  
related operators with even stronger properties, including a ternary variant that requires no  
distinguished constant.  
2

Highlight & Ask

Select any part of the paper to ask specific questions

Add Context

Type @ to reference other papers and expand the discussion

Additional

•

• See how others cite this work

• Literature reviews

• Community context

Try asking "What's the intuition behind section 3.2?"