# BUILD-NOTE — Seventeen Syllables of Debugging

- Competition: `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
- Prize: $5 (1st $2, 2nd $2, 3rd $1)
- Deadline: 2026-11-24T13:15:00Z (20:15 WIB 24 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).
  No `main.ts` — a second entrypoint would be ambiguous.

## Entry text

> Breakpoint at midnight / the log says nothing is wrong / yet nothing runs right

- Characters: 75 (gate: 1-200 characters)
- Bytes (UTF-8): 75
- Lines: 3, no trailing newline
- Whitespace-only: no

## Why this entry

Haiku 5-7-5 about debugging: Break-point(2) at(1) mid-night(2) = 5; the(1) log(1) says(1) no-thing(2) is(1) wrong(1) = 7; yet(1) no-thing(2) runs(1) right(1) = 5. Concrete centre (breakpoint, log line), and the last line reframes the second: the log lies by omission.

Original work — no anchor, rung, or house text from the kit was copied.

## Verification (local, run 2026-11-24)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 `b51ad8fd6be0531fc2ba9da96f6bd5f2f759d7d100600dc16a74514f44694408` on both runs), gate check passed:
   UTF-8 decodes, 75 characters within 1-200 characters, 3 lines (haiku 5-7-5),
   not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```

## Repo note for the submitter

- Repo must be created after the competition opened and carry
  `.makefun/owner.json` only if the GitHub owner is not the make.fun
  account's GitHub login (kiw33) — it is kiw33, so no claim file needed.
- README badges above use `kiw33/u-irvan-motion-seventeen-syllables-of-debugging-d194b605` as the repo name; adjust the
  rank/reward badge URLs if the repo is created under a different name.
- GitHub About must have a website on make.fun and the topic `makefun`
  before submitting (kit check `repo_about`).
