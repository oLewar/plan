# Sutskever 30 implementations (pageman/sutskever-30-implementations)

## Bibliographic / source

| Field | Value |
|---|---|
| Repo | https://github.com/pageman/sutskever-30-implementations |
| Author | Paul "The Pageman" Pajo (`pageman`); README citation email `pageman@gmail.com` |
| What it is | 30 Jupyter notebooks, one per item on Ilya Sutskever's reading list (the list he told John Carmack would teach "90% of what matters") |
| Inspired by | https://papercode.vercel.app/ (author note, not fetched) |
| Default branch | `main` |
| HEAD at ingest | `225cba7b0362` (2026-03-15, "docs: add Annotated Transformer companion resource to Paper 13") |
| Created | 2025-12-06 |
| Completion claim | `PROGRESS.md`: 30/30 on 2025-12-10 |
| Stars / forks | **4575** / **591** (GitHub API 2026-09-25); open issues 3 |
| Languages | Jupyter Notebook 919869 B, Python 226768 B |
| Tree | 88 blobs, not truncated. **No package, no tags, no releases, no SPDX license file** |
| README license line | "Educational use. See individual papers for original research citations." |
| Paid companion | Colab code on Gumroad: https://pageman.gumroad.com/l/sutskever30colabcode (not fetched) |
| Sibling repos (not ingested) | [`pageman/Sutskever-Agent`](https://github.com/pageman/Sutskever-Agent) — GitAgent pedagogue, 9★, pushed same day as HEAD; [`pageman/sutskever-30-beyond-numpy`](https://github.com/pageman/sutskever-30-beyond-numpy) — polyglot port, 6★, license `NOASSERTION` |
| Raw capture | [[raw/pageman-sutskever-30-implementations-readme]] |

## One-line purpose

Учебные NumPy-ноутбуки по списку из 30 текстов Суцкевера: механизм виден без фреймворка, на синтетических данных. Это карта идей, не библиотека и не воспроизведение статей.

## Thesis (from README + notebook source, not executed)

1. **NumPy on purpose.** README: no PyTorch/TensorFlow, so the operation is visible. SciPy is the exception (`scipy.special.softmax`, `scipy.stats.entropy`) in a minority of notebooks. Paper 8 and Paper 18 mention JAX/PyTorch only as the "port this to train for real" note.
2. **Synthetic data on purpose.** Each notebook is supposed to generate its own inputs so nothing is downloaded. That also means a notebook can "run" without ever touching the paper's dataset or metric.
3. **30 files ≠ 30 trained models.** Every `NN_*.ipynb` exists and has functions and classes. Saved cell outputs: **0 of 30**. A training loop that updates weights is in **6**: `02` char-RNN, `05` pruning, `09` GPipe, `18` relational RNN (its own NumPy autograd + Adam), `26` CS231n, `27` multi-token. The other 24 are forward-pass or simulation sketches. Paper 13 (Transformer) defines scaled-dot-product, multi-head, positional encoding, and a block — and has **no** `backward` and **no** train loop.
4. **Paper 22 does not fit a scaling law.** It *simulates* loss-vs-size curves (`base_loss = np.log(vocab_size)`, then formulas). Do not cite it as a measured Kaplan/Chinchilla result.
5. **Paper 18 is a second repo inside the repo.** Root `*.py` (~10k lines: `relational_rnn_cell.py`, `relational_memory.py`, `training_utils.py`, `lstm_baseline.py`, `reasoning_tasks.py`) plus `*.npz` checkpoints and curve PNGs are the Paper 18 side-project, not a shared library for the other 29.
6. **The list is Sutskever's; the code is not.** Badge "30/30" is the author's file count. Several items are essays or courses (Aaronson complexodynamics, Olah's LSTM post, CS231n, Legg & Hutter), not papers with a single experiment to reproduce.

## The 30 (file present; depth is the author's)

| # | Notebook | README title | Weight update in source? |
|---|---|---|---|
| 1 | `01_complexity_dynamics.ipynb` | First Law of Complexodynamics (Aaronson) | no — CA / entropy |
| 2 | `02_char_rnn_karpathy.ipynb` | Unreasonable Effectiveness of RNNs | **yes** — `train_rnn`, 2000 iters |
| 3 | `03_lstm_understanding.ipynb` | Understanding LSTM Networks (Olah) | gates + backward, no train loop |
| 4 | `04_rnn_regularization.ipynb` | RNN Regularization (Zaremba et al.) | no |
| 5 | `05_neural_network_pruning.ipynb` | Keeping NNs Simple (MDL / pruning) | **yes** — masked `W -= lr * dW` |
| 6 | `06_pointer_networks.ipynb` | Pointer Networks | no |
| 7 | `07_alexnet_cnn.ipynb` | ImageNet / AlexNet | no |
| 8 | `08_seq2seq_for_sets.ipynb` | Order Matters (Vinyals et al.) | no — author says forward-pass only |
| 9 | `09_gpipe.ipynb` | GPipe | **yes** — microbatch schedule toy |
| 10 | `10_resnet_deep_residual.ipynb` | Deep Residual Learning | backward, no train loop |
| 11 | `11_dilated_convolutions.ipynb` | Dilated convolutions (Yu & Koltun) | no — smallest code notebook (~5 KB) |
| 12 | `12_graph_neural_networks.ipynb` | Neural Message Passing (Gilmer et al.) | no |
| 13 | `13_attention_is_all_you_need.ipynb` | Attention Is All You Need | no — forward block only |
| 14 | `14_bahdanau_attention.ipynb` | Bahdanau attention | backward, no train loop |
| 15 | `15_identity_mappings_resnet.ipynb` | Identity mappings in ResNet | backward, no train loop |
| 16 | `16_relational_reasoning.ipynb` | Relation Networks | no |
| 17 | `17_variational_autoencoder.ipynb` | Variational Lossy Autoencoder | no — ELBO sketched, not fit |
| 18 | `18_relational_rnn.ipynb` | Relational RNNs (Santoro et al.) | **yes** — plus the root `.py` stack |
| 19 | `19_coffee_automaton.ipynb` | Coffee automaton (Aaronson) | no — irreversibility essay-in-code |
| 20 | `20_neural_turing_machine.ipynb` | Neural Turing Machines | no |
| 21 | `21_ctc_speech.ipynb` | Deep Speech 2 (CTC) | no |
| 22 | `22_scaling_laws.ipynb` | Scaling Laws (Kaplan et al.) | no — simulated curves |
| 23 | `23_mdl_principle.ipynb` | Minimum Description Length | no |
| 24 | `24_machine_super_intelligence.ipynb` | Legg & Hutter / AIXI | no — largest cell count (39) |
| 25 | `25_kolmogorov_complexity.ipynb` | Kolmogorov complexity | no |
| 26 | `26_cs231n_cnn_fundamentals.ipynb` | CS231n (course, not one paper) | **yes** — linear + 2-layer on synthetic images |
| 27 | `27_multi_token_prediction.ipynb` | Multi-token prediction | **yes** — `train_single_token` / `train_multi_token` |
| 28 | `28_dense_passage_retrieval.ipynb` | Dense Passage Retrieval | no |
| 29 | `29_rag.ipynb` | Retrieval-Augmented Generation | no |
| 30 | `30_lost_in_middle.ipynb` | Lost in the Middle | no |

## Why it matters for `pro/plan`

- This is the **frontier-tools pole's opposite**: a frozen reading list, implemented so the mechanism is visible. Pairs with [[wiki/concepts/barbell-strategy]] and with [[wiki/concepts/composed-error-analysis]] (that book is the proof side; these notebooks are the toy-code side).
- Useful as a **map of which mechanism lives where** (gating, skip, attention-as-pointer, external memory, CTC, RAG). Not useful as evidence that the mechanism works — outputs were never saved, and 24/30 never update weights.
- [[wiki/concepts/numpy-paper-toy]] — the honest unit is "can I see the op", not "did the paper reproduce".
- Not a harness, not an agent, not something to `pip install` on this host.

## Status

- **Ingest source**: GitHub API (repo, languages, tree, commits, tags, releases) + README + `IMPLEMENTATION_TRACKS.md` head + `PROGRESS.md` + all 30 notebooks and root `.py` downloaded to `/tmp` and inspected as source. Not cloned. Not executed. Gumroad, papercode.vercel.app, and the two sibling repos not fetched past the API card.
- **Depth**: README-level plus a source census (cell counts, framework imports, whether a weight is updated inside a loop). Not a line review of all 30.
- **Confidence**: high on tree, stars, license absence, zero saved outputs, and which notebooks contain `W -=` / a train loop (those strings are in the source). Medium on "the other 24 never learn" — a notebook could update weights under a name this census missed; spot-checks on 13 and 22 did not.
- **Do not cite**: "NumPy only" as absolute (`scipy` imports exist); "100% implementations" as trained reproductions; Paper 22 curves as measured scaling laws; Gumroad Colab as verified to match `main`.

## Links

- Concept: [[wiki/concepts/numpy-paper-toy]]
- Entity: [[wiki/entities/paul-pajo]]
- Tool card: [[10_Reference/tools/sutskever-30-implementations]]
- Adjacent: [[wiki/sources/mathematical-introduction-to-deep-learning]], [[wiki/concepts/composed-error-analysis]], [[wiki/concepts/barbell-strategy]]
