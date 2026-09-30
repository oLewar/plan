# UniMate

Motion model for many skeleton topologies. **Reference only. Not installed. Checkpoints and dataset not downloaded.**

| | |
|---|---|
| Repo | https://github.com/Friedrich-M/UniMate |
| Page | https://linzhanmou.com/unimate/ |
| Paper | https://arxiv.org/abs/2609.05415 |
| Code license | MIT. Data is not: Mixamo terms, per-object Objaverse, Truebones commercial (motions not in the download) |
| Train | `accelerate launch -m unimate.training.train --config configs/uniml3d_60frames_graph_adaln.json` |
| Sample | `python -m unimate.inference.sample --exp_dir <run>` — needs `dataset/features/<dataset>/` beside the checkpoint |
| Tags | none |

Wiki: [[wiki/sources/unimate]] · [[wiki/concepts/pinned-flow-sampling]]

In-betweening, joint editing, and expansion are one Euler sampler that overwrites the pinned slice every step. They require flow matching; they do not use the dopri5 solver that plain sampling uses. Preview checkpoints are not the final ones, and released captions need not match the paper.
