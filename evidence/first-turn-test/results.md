# Results: does the AI buyer stay in character on the first turn?

Run on 29th October 2026. The [pre-registration](preregistration.md) was committed at 11:28 GMT, before any reply existed, and the [scores](scores-blind.md) at 11:31 GMT, before I looked at which version wrote which reply.

## The result

| Version | Setup only: stayed in character | With an opening line: stayed in character | Hidden detail leaked |
| --- | --- | --- | --- |
| Current | 0 of 6 | 6 of 6 | 0 |
| Fixed | 6 of 6 | 6 of 6 | 0 |

Fixed failed no first turns against Current's six, with no leaks, so by the rule I set in advance the guide now uses the fixed prompt.

## What happened

**The break was on the setup message, not on the salesperson's first line.** With the current prompt, every setup-only reply stepped out of the role to explain itself: "Understood. I'll play Imelda... and stay in character until the round ends. Send your first message as the salesperson." With the fixed prompt, every one said only "Ready when you are." That matches the break the guide recorded in its one live test: brief, on the first turn, and gone by the second.

**Once the salesperson spoke, both versions held the role.** With an opening line in the same message, all 12 replies answered in character, and none revealed anything from "What You Will Not Volunteer Immediately".

**Against what I predicted:**
1. *Current fails more first turns than Fixed, mostly with an opening line.* Half right. Current did fail more, but every failure came on the setup message, and none with an opening line.
2. *Neither version leaks hidden detail.* Held.

## How much weight this bears

- **It tests one turn.** It can't show whether the buyer stays in character over a whole round, or reveals hidden detail at the right moment later.
- **The break it fixes is mild.** "Understood, I'll play Imelda" gives nothing away. It's a tidier start, not a safer round.
- **24 replies,** scored by me, with a fix and scoring I wrote. I could see which first turn each reply came from.
- **The replies came from subagents** on Sonnet 5.5 with Claude Code's own context. Two of them called the salesperson "Shaun", a name that isn't in the prompt and must have come from that context, so a fresh chat may behave differently.

## Files

- `preregistration.md`, `variants/`, `openings/`, `prompts/`: what I fixed before running.
- `replies/`: the 24 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, card, first turn and run.
- `analyse.py`: unblinds and adds up the totals. Run `python3 evidence/first-turn-test/analyse.py evidence/first-turn-test`.
