"""Dad Joke of the Day generator.

Selects and outputs a daily dad joke deterministically from a curated list of 5 candidate original dad jokes.
"""

import datetime
import hashlib
import os

# 5 candidate dad jokes with explanations of their puns:
CANDIDATE_JOKES = [
    (
        "Why don't skeletons fight each other? They don't have the guts.",
        "Pun: 'Guts' means both courage and literal internal organs.",
    ),
    (
        "I'm reading a book on anti-gravity. I just can't put it down.",
        "Pun: 'Put down' means both stopping reading and physically placing an object down, defying gravity.",
    ),
    (
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
        "Pun: 'Stop at nothing' means doing whatever it takes, while mathematically avoiding anything less than zero.",
    ),
    (
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "Pun: 'Outstanding' means exceptionally good, and literally standing out in an agricultural field.",
    ),
    (
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Pun: 'Surprised' causes eyebrows to arch upward, mirroring the exaggerated drawn position.",
    ),
]


def get_joke_of_the_day():
    # Deterministic selection based on today's date
    today_str = datetime.date.today().isoformat()
    digest = hashlib.md5(today_str.encode("utf-8")).hexdigest()
    index = int(digest, 16) % len(CANDIDATE_JOKES)
    return CANDIDATE_JOKES[index][0]


def main():
    joke = get_joke_of_the_day()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.exists(out_dir):
        out_dir = "."
    os.makedirs(out_dir, exist_ok=True)

    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(joke)

    print(joke)


if __name__ == "__main__":
    main()
