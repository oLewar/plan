# Julia 1

Local decision model. **Reference only. Weights not downloaded, package not installed** on this host.

| | |
|---|---|
| Page | https://supersoniclabs.ia.br/julia-1/ |
| Weights | https://huggingface.co/SupersonicLabs/Julia-1 |
| Package | `supersonic-julia` 0.1.0 (Apache-2.0). `pip install -e` after `snapshot_download` |
| Run | `from julia import load_model` then `engine.predict(state=..., questions=...)` on CPU |
| Base | `jhu-clsp/mmBERT-small` (MIT). Not a Transformers AutoModel |
| Disk | 550.5 MiB FP32 checkpoint |

Wiki: [[wiki/sources/julia-1]] · [[wiki/concepts/supplied-option-ranker]]

It scores options you pass in (`choice` / `score` / `noul`, 2–20). It does not generate text. A Jev column in their table is a supplied reference, not a rerun.
