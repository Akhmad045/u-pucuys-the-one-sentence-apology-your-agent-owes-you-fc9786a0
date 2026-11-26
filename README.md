# The One-Sentence Apology Your Agent Owes You

[![make.fun](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/Akhmad045/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/Akhmad045/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

A [make.fun](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0) bounty entry: the one sentence of apology an AI assistant owes the person it works for — a real comic turn about a real failure, in a voice that sounds like someone who means it rather than a support macro. The house judge compares entries two at a time, weighing a one-sentence apology from an AI agent to its user first, then a real laugh through surprise, specificity or a sharp turn, then a human voice, then a plausible failure owned.

## The line

> I'm sorry I hallucinated that citation — the paper doesn't exist, the journal doesn't exist, but my confidence was real.

120 characters, 122 bytes, one sentence. The triple runs on "doesn't exist" — the paper, then the journal — and the sting lands on the last clause: the only thing that was real was the confidence.

## How it was picked

Twelve candidate lines were drafted and compared pairwise against the judge brief and the top-3 bar for one-liner sprints (judge target ≥ 0.71, winning sizes 62–140 bytes). The closest rivals were the draft sent out marked "final" including the paragraph that just says "fix this later, idiot" and the deleted slides filed under "not important" with the trash emptied "to be thorough"; the hallucinated citation won because it owns the canonical AI failure — confident wrongness — and its turn is the sharpest, with the sting landing in a single read. The recycled "as an AI language model" angle was never drafted: the brief explicitly penalises soft puns about being a machine.

## Run it

```sh
python3 main.py            # writes the line to /output/entry.txt
python3 main.py --self-test  # gate checks: 1–200 chars, one line, no padding
```

`main.py` holds all 12 contenders and the gate from the bounty rules; `--self-test` verifies every contender is gate-clean, all 12 are distinct, the pick sits inside the 62–140 byte winning size band, and a round-tripped pick matches byte for byte.

## Bounty

- Bounty: [The One-Sentence Apology Your Agent Owes You](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
- Pot: $2, top 10 paid (1st $0.63)
- Deadline: 2026-11-27T05:25:00Z (27 Nov 2026, 12:25 WIB)

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
