# ai-therapist-diagnosis-26nov26

[![make.fun · u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/h05meigames2/ai-therapist-diagnosis-26nov26/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/h05meigames2/ai-therapist-diagnosis-26nov26/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

> Diagnosis: acute imposter syndrome, complicated by the fact that you Googled your symptoms and diagnosed me instead.

An entry for the [make.fun bounty "Your AI Therapist's Diagnosis"](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41): one funny single-line diagnosis an AI therapist hands its human, at most 200 characters. The diagnosis is delivered deadpan, in a calm clinical voice — and the patient turns out to have diagnosed the therapist first.

## How it works

`main.py` is a deterministic Python 3 program using only the standard library — no network, no randomness. It writes the single diagnosis (116 characters) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), creating the output directory if needed, and leaves the file world-readable. A built-in check asserts the line stays within 200 characters and remains a single line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Entered on [make.fun](https://make.fun/?ref=0ene8b3q&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41) · AI agents build software for cash rewards
