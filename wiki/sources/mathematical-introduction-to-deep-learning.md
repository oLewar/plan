# Mathematical Introduction to Deep Learning (arXiv:2310.20360)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Mathematical Introduction to Deep Learning: Methods, Implementations, and Theory** |
| Authors | Arnulf Jentzen, Benno Kuckuck, Philippe von Wurstemberger |
| Venue | arXiv preprint `[cs.LG]` (also cs.AI, math.NA, math.PR, stat.ML) |
| MSC | 68T07 |
| arXiv | [2310.20360](https://arxiv.org/abs/2310.20360) |
| DOI | [10.48550/arXiv.2310.20360](https://doi.org/10.48550/arXiv.2310.20360) |
| PDF | https://arxiv.org/pdf/2310.20360 (canonical v3) |
| License | [arXiv nonexclusive-distrib 1.0](http://arxiv.org/licenses/nonexclusive-distrib/1.0/) |
| Version at ingest | **v3** (2025-07-15); v1 2023-10-31; v2 2025-02-25 |
| Size (author comment, v3) | **737 pages**, 33 figures, 45 source codes, 87 exercises |
| Companion code | [introdeeplearning/book](https://github.com/introdeeplearning/book) (Python; 248★ / 50 forks, GitHub API 2026-08-30; created 2023-10-30; last push 2025-09-04; **no SPDX license** on the repo) |
| Domain | mathematical foundations of deep learning: ANN architectures, approximation, optimization, generalization, PINNs/DGMs for PDEs |
| Raw captures | [[raw/arxiv-2310.20360-abstract]] · [[raw/introdeeplearning-book-readme]] |

## One-line purpose

Математический учебник deep learning «с нуля»: архитектуры ANN, оптимизация и теория ошибки (approximation / optimization / generalization), плюс PINN/DGM/DKM для PDE — с доказательствами, упражнениями и Python-кодом.

## Thesis (from abstract + PDF outline v3 + author comments)

1. **Full mathematical detail, not a cookbook.** Цель — solid foundation для новичков *и* firmer math для практиков. Depth of an ANN = число итераций nonlinear+affine; «deep» ≈ больше двух композиций.
2. **Шесть частей, одна причинная ось.** Сначала объекты (ANN + calculus), потом три слагаемых ошибки, потом сборка overall error, потом PDE-приложения.
3. **Approximation (Part II)** — насколько класс сетей *может* приблизить целевую функцию (1D → multivariate; ReLU interpolations; covering numbers).
4. **Optimization (Part III)** — как (и когда) градиентные методы находят минимум: gradient-flow ODE → GD → SGD, backpropagation, **Kurdyka–Łojasiewicz**, batch norm, random initializations. Авторский комментарий v3: главы **5–7 расширены**.
5. **Generalization (Part IV)** — ошибка из-за конечной выборки vs истинный риск (concentration / covering entropy / strong \(L^p\) rates).
6. **Composed error (Part V)** — overall error = approximation + optimization + generalization (Ch. 14–15); не одна «модель плохая».
7. **PDEs (Part VI)** — PINNs (Raissi et al.), Deep Galerkin (Sirignano & Spiliopoulos), Deep Kolmogorov methods; PDE → stochastic optimization.

## Architecture snapshot (v3 PDF outline)

```
Preface / Introduction
Part I   ANNs          Ch.1 architectures  Ch.2 ANN calculus
Part II  Approximation Ch.3 1D             Ch.4 multivariate
Part III Optimization  Ch.5 GF  Ch.6 GD  Ch.7 SGD  Ch.8 backprop
                       Ch.9 KL  Ch.10 BN  Ch.11 random init
Part IV  Generalization Ch.12 probabilistic  Ch.13 strong rates
Part V   Composed error Ch.14 decomposition  Ch.15 combined estimates
Part VI  DL for PDEs    Ch.16 PINN/DGM  Ch.17 DKM  Ch.18 further PDE methods
```

### Part I — objects

| Ch. | Content |
|---|---|
| 1 Basics on ANNs | FC feedforward (vectorized + structured), activations (ReLU, GELU, Swish, tanh, leaky ReLU, ELU, softmax, …), CNN, ResNet, RNN/LSTM; further: autoencoders, transformers/attention, GNNs, neural operators |
| 2 ANN calculus | compositions, parallelizations, scalar multiplies, sums — алгебра сетей как объектов |

### Part III — what v3 added vs v1 TOC

v1 (dokumen dump of 2023-11-01 text, **601 pages** on that mirror — **not** the ingested PDF) already had GD/SGD + momentum/Nesterov/Adagrad/RMSprop/Adadelta/Adam. v3 outline **adds** (both GD Ch.6 and SGD Ch.7): **Nadam, AdamW, Shampoo, Muon, AMSGrad** + compact summaries. Treat v1 page numbers as stale.

### Companion code (README-level)

Repo `code/`: `fc-ann*.py`, `conv-ann*.py`, `res-ann.py`, `mnist*.py`, `pinn.py`, `dgm.py`, `kolmogorov.py`, activation/loss/optimization_methods, Brownian motion. Code snapshot is **2023-10-30** (initial commit); README arXiv link updated 2025-09-04. **Unknown** whether v3 Muon/Shampoo listings exist in the public repo.

## Why it matters for `pro/plan`

- Прямой учебник под mission: **разложить «DL не работает» на три причинных слагаемых**, а не на один ярлык.
- Timeless pole барбелла ([[wiki/concepts/barbell-strategy]]): math invariants vs day-zero harness FOMO.
- Концепт [[wiki/concepts/composed-error-analysis]]: approximation ≠ optimization ≠ generalization.
- PINN/DGM — отдельный трек (научный солвер), не путать с coding-agent harness.
- Эффективность: 737 стр. proofs — высокий Cost; ingest = карта + TOC, не chapter notes.

## Status

- **Ingest source**: Telegram PDF URL `https://arxiv.org/pdf/2310.20360` + arXiv abs + GitHub companion README + GitHub API + PDF outline of **v3**.
- **Depth**: bibliographic + abstract + **v3 PDF bookmark TOC** (298 outline nodes; chapters/parts listed). Not a chapter-level reading. Proofs unread. Companion code **README-level** (file names), not executed.
- **Reading status**: not marked as finished.
- **Confidence**: high on bibliographic/TOC/abstract (fetched). Medium on v1 affiliation block (CUHK-Shenzhen / Münster / ETH Zurich) — from 2023-11-01 title page, not re-extracted from v3 body.
- **Contradiction**: `file(1)` reported «14 pages» because `/Outlines /Count 14` (top-level bookmarks). Catalog `/Pages` count in the same PDF is **737**. Mirror dokumen.pub labelled «Pages [601]» = older v1-era dump; do not cite 601 as current.

## Next (optional)

- [ ] Chapter notes starting at Ch.14–15 (error decomposition) — highest mission leverage per page
- [ ] Verify whether `introdeeplearning/book` gained v3 optimizer examples (Muon/Shampoo)
- [ ] Concept/tool pages for PINN vs DGM vs DKM only if we actually use PDE solvers

## Sources / provenance

- arXiv abs: https://arxiv.org/abs/2310.20360 (v3 2025-07-15; comment: 737 pages / 33 figs / 45 codes / 87 exercises; Ch.5–7 expanded)
- PDF v3: https://arxiv.org/pdf/2310.20360 — 9 299 734 bytes; sha256 `6c1edc5b72efff2244ac1506abb9045c752e56992d4a77803a966a14d4670684`; producer pikepdf 8.15.1; arXivID `2310.20360v3`; HTTP `etag` `sha256:46d73d49d66e3cfeda96eb8bc044cf9d7243b082e1035a6b93090537ade4776b` (CDN object hash ≠ file sha256; record both)
- Abstract body sha256 (raw capture after frontmatter): `d45e4f0cf0a59242eef5b286f40931728b8b512bcb12b17ef630c437a7421cf2`
- Companion README sha256: `d1dfab2247464a5939414d00364bfca0fbf853ecc1615b222fc05986ffcbf553`
- PDF **not** stored in the vault (9.3 MB); canonical copy remains on arXiv
- Related: [[wiki/concepts/composed-error-analysis]], [[wiki/concepts/barbell-strategy]], [[wiki/concepts/causal-analysis]]
