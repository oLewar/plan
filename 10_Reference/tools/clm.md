# CLM

Local **System One** ranker: frozen Qwen3-8B encoder plus two small contrastive heads. Speaks the same `POST /v1/systemone` wire as TypeSafe Jev (`noul` / `choice` / `score`). Apache-2.0. Reference only.

- Full wiki source: [[wiki/sources/clm]]
- Entity: [[wiki/entities/contrastive-lm]]
- Concept: [[wiki/concepts/contrastive-action-ranker]]
- GitHub: https://github.com/Contrastive-LM/CLM
- Blog: https://contrastive-lm.notion.site
- Weights: https://huggingface.co/Contrastive-LM/CLM-v0.1-8B
- PyPI name: `contrastive-lm` **0.1.0** (no git tags, 2026-09-25)
- Stars: **947** (GitHub API 2026-09-25)

## Commands (README; not run here)

```bash
pip install contrastive-lm
vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b --runner pooling --max-model-len 2048 --port 8090
clm-serve
```

Playground at `http://127.0.0.1:8700/`. API only: `clm-serve --no-ui`. Needs a GPU for the encoder (README: 24 GB with the 2048 cap; 4090 in their playground note). Do not install on this host without an explicit ask.

## Operating constraints

- Ranker, not a generative loop. It scores candidates you pass in.
- `CLM_API_KEY` optional. `--cors` is off by default so a key is not sent to arbitrary origins.
- T-Rex survival in the shipped JSON is with a planner shield on. CLM agrees with the planner ~66%; Jev ~99%. Do not quote 5/5 as the model's score.
- README 9× / DeepSWE 81.6% / TB2.1 87.6% are author claims (held-out 38 and 30). Not reproduced.

## Mental model

Embed state and each action, softmax, execute the argmax yourself. Contrast hosted Jev ([[wiki/concepts/indexed-action-space]]), offline harness search ([[wiki/concepts/regularized-harness-search]]).
