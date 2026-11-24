# tabs-open-count-20261123

[![make.fun · How Many Tabs Do You Have Open?](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/sopiahusen42/tabs-open-count-20261123/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/sopiahusen42/tabs-open-count-20261123/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)

312 is the honest count. Not a tidy number, because nobody arrives at their tab
count by deciding on one — you arrive at it by scrolling the strip and counting,
and a strip that long always has a few survivors in it: the docs page from a
task that got finished days ago, three copies of the same issue opened because
the first two were "just for reference", a couple of half-read things from a
sprint that died. Round numbers are what people answer when they estimate.
312 is what a person says after they actually look.

## The count

```text
312
```

## Run it

```console
$ python3 main.py
$ cat /output/entry.txt
312
```

## How it works

`main.py` is the whole program. It holds the line in a single module constant,
`COUNT`, and passes it to `validate_entry(text)` before touching the disk. That
validator returns an error string or `None`, and it enforces the gate: a string,
not blank, 1 to 160 code points, one line with no `\n` or `\r`, no leading or
trailing whitespace, ASCII digits only with no sign, space or punctuation, and
zero permitted only when written exactly as `0`.

If validation passes, the program creates the output directory (default
`/output`, override with `MAKEFUN_OUTPUT_DIR`), writes `COUNT + "\n"` as UTF-8
with `newline="\n"`, then reads the file back and compares the bytes to the
intended payload. Any failure prints one line to stderr and exits 1. There is no
clock, no randomness and no network, so the bytes are the same on every run.
