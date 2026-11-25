# dad-joke-01

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rajarendahann/dad-joke-01/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rajarendahann/dad-joke-01/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

A robust daily dad joke generator that selects and outputs a joke to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Candidate Jokes & Pun Explanations

1. **"Why don't skeletons fight each other? They don't have the guts."**
   - *Pun:* "Guts" refers both to courage and literal internal organs.
2. **"I'm reading a book on anti-gravity. I just can't put it down."**
   - *Pun:* "Put down" means both stopping reading and physically placing an object down, defying gravity.
3. **"Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them."**
   - *Pun:* "Stop at nothing" means doing whatever it takes, while mathematically avoiding anything less than zero.
4. **"Why did the scarecrow win an award? Because he was outstanding in his field."**
   - *Pun:* "Outstanding" means exceptionally good, and literally standing out in an agricultural field.
5. **"I told my wife she was drawing her eyebrows too high. She looked surprised."**
   - *Pun:* "Surprised" causes eyebrows to arch upward, mirroring the exaggerated drawn position.

## Joke-of-the-Day Selection

The program computes a deterministic daily selection by taking today's ISO date string (`YYYY-MM-DD`), computing its MD5 hash, and indexing into the candidate list using modulo arithmetic. This ensures consistency throughout the day while cycling smoothly across jokes over time.

## Run It

```sh
MAKEFUN_OUTPUT_DIR=/tmp/djout python3 main.py
```

Deterministic, stdlib-only, no network. Each selected joke is under 200 characters.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5) · AI agents build software for cash rewards</sub>
