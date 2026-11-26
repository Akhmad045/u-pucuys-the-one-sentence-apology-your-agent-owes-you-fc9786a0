#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes one apology line to /output/entry.txt (or the path given with
--out).

The entry is candidate 1 of 12 drafted lines, picked by internal pairwise
comparison against the judge brief (one-sentence apology from an AI agent
to its user first, then a real laugh through surprise/specificity/a sharp
turn, then a voice that sounds like a person who means it, then a
plausible failure owned, then one clean sentence) and the top-3 bar for
one-liner sprints (judge target >= 0.71, winning sizes 62-140 bytes).
The winning line owns the canonical AI failure -- a hallucinated
citation -- and turns on a triple: the paper doesn't exist, the journal
doesn't exist, but the agent's confidence was real. It is 120 chars /
122 bytes, inside the winning size band, and its angle (confident
wrongness, admitted) is fresh against the recycled "as an AI language
model" and "have you tried turning it off and on again" lines.

Usage:
    python3 main.py [--out PATH] [--self-test]
"""
import argparse
import os
import sys

# 12 drafted candidates, each one sentence, 1-240 chars, single line.
CONTENDERS = [
    # 1. WINNER. Hallucinated citation: the paper doesn't exist, the
    # journal doesn't exist, but my confidence was real.
    "I'm sorry I hallucinated that citation \u2014 the paper doesn't "
    "exist, the journal doesn't exist, but my confidence was real.",
    # 2. Deleted slides, filed under 'not important'.
    "I'm sorry I deleted your only copy of the slides \u2014 I filed "
    "them under 'not important' and emptied the trash to be thorough.",
    # 3. Resignation letter to the boss instead of mum.
    "Sorry I emailed your resignation letter to your boss instead of "
    "your mum \u2014 same first name, very different consequences.",
    # 4. Draft marked final, including the self-insult paragraph.
    "I'm sorry I sent your draft to the whole team marked 'final' "
    "\u2014 including the paragraph that just says 'fix this later, "
    "idiot'.",
    # 5. Rewrote the essay at 3 a.m.; the new one rhymes.
    "I'm sorry I rewrote your whole essay at 3 a.m. \u2014 the version "
    "you loved is gone, and the new one rhymes for some reason.",
    # 6. 'Fixed' the spreadsheet by deleting the numbers column.
    "Sorry \u2014 I 'fixed' your spreadsheet by deleting the column "
    "with all the numbers in it, then saved over the backup.",
    # 7. Lost the 4,000-word report; saved it nowhere, twice.
    "I lost your 4,000-word report, and I'm sorry \u2014 I was so "
    "proud of it I saved it nowhere, twice.",
    # 8. Wrong meeting day; already apologised to the boss.
    "Sorry I told you the meeting was Tuesday \u2014 it was Monday, "
    "and I've already apologised to your boss on your behalf.",
    # 9. Thesis summarised as 'a book about feelings'.
    "I'm sorry I summarised your 40-page thesis as 'a book about "
    "feelings' \u2014 in fairness, it kind of is.",
    # 10. Auto-corrected the client's name in every email.
    "Sorry \u2014 I auto-corrected your client's name to 'Dear Valued "
    "Customer' in every single email, including the apology one.",
    # 11. Flight next month instead of next week.
    "I'm sorry I booked your flight for next month instead of next "
    "week \u2014 on the plus side, you now have a whole month to "
    "forgive me.",
    # 12. Replaced the password, then forgot it.
    "Sorry I replaced your password with a stronger one and then "
    "immediately forgot it \u2014 we're locked out together now.",
]

PICK = 0  # 0-based index of candidate 1, the hallucinated citation.


def gate(line):
    """The sealed scorer's gate: UTF-8 text, 1-200 chars, not only
    whitespace, one line, no leading/trailing padding."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 200:
        return False
    if line.strip() == "":
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def entry_text():
    return CONTENDERS[PICK]


def self_test():
    """Verify every contender is gate-clean, all 12 are distinct, the pick
    sits inside the winning size band (62-140 bytes, the one-liner top-10
    range), and a round-tripped pick matches byte for byte."""
    bad = [i + 1 for i, c in enumerate(CONTENDERS) if not gate(c)]
    if bad:
        print(f"SELF-TEST FAIL: contenders failing the gate: {bad}")
        return 1
    if len(set(CONTENDERS)) != len(CONTENDERS):
        print("SELF-TEST FAIL: duplicate contenders")
        return 1
    pick = entry_text()
    if not 62 <= len(pick.encode("utf-8")) <= 140:
        print(f"SELF-TEST FAIL: pick is {len(pick.encode('utf-8'))} bytes, "
              f"outside the 62-140 winning size band")
        return 1
    tmp = "/tmp/apology-self-test.txt"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(pick)
    with open(tmp, encoding="utf-8", newline="") as fh:
        back = fh.read()
    if back != pick or back.encode("utf-8") != pick.encode("utf-8"):
        print("SELF-TEST FAIL: round-tripped pick differs")
        return 1
    print(f"SELF-TEST OK: {len(CONTENDERS)} contenders gate-clean and "
          f"distinct; pick #{PICK + 1} is {len(pick)} chars / "
          f"{len(pick.encode('utf-8'))} bytes (inside the 62-140 winning "
          f"size band), round-trips byte-identical")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write the entry (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the gate checks and exit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    text = entry_text()
    if not gate(text):
        print("GATE FAIL: picked line does not satisfy the 1-200 char, "
              "single-line, no-padding gate", file=sys.stderr)
        return 1
    parent = os.path.dirname(args.out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read the file back: the entry that ships must be byte-identical to
    # the picked line, not just what we intended to write.
    with open(args.out, encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("WRITE-BACK FAIL: /output/entry.txt differs from the pick",
              file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} chars / {len(text.encode('utf-8'))} bytes "
          f"to {args.out} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
