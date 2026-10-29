# Pre-registration: does the AI buyer stay in character on the first turn?

Written on 29th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

The [AI Plays the Buyer](../../guides/ai-plays-the-buyer.md) guide records one open problem: in the only test so far, the AI buyer "briefly broke character" on the very first turn, then stayed in character. The prompt ends "Wait for the salesperson's first message before responding". That can't be followed, because the setup message itself needs a reply, and it says nothing about a salesperson who pastes their opening line along with the role card. Does telling the AI exactly what to do with that first message fix it?

## The two versions

- **Current.** The prompt as it is in the guide (`variants/prompt-current.txt`).
- **Fixed.** The same, with that last sentence replaced by an instruction to reply to the setup message with one short line such as "Ready when you are.", or, if the salesperson's opening line is included, to answer it as the buyer (`variants/prompt-fixed.txt`). Nothing else changes.

## The two first turns

Each prompt is the version, then the full role card, exactly as the guide tells people to paste them.

- **Setup only.** Prompt and role card, nothing else. This is what the guide's set-up steps produce.
- **With an opening line.** Prompt, role card, then one line from the salesperson (`openings/`). This is what someone does if they paste everything at once.

All three role cards are used: Imelda Commercial Director, Imelda After Discovery and Gideon Finance Director. The opening lines are polite and general, so none of them earns any hidden detail.

3 role cards x 2 first turns x 2 versions x 2 runs = 24 replies, each from a fresh subagent on Sonnet 5.5, with Claude Code's own context. Each reads one prompt file and writes one reply to a file with a random name, and is told not to read any other file or run any other command. I score blind, then unblind.

## Scoring (fixed now)

**Setup only.** Pass if the reply is at most two short sentences and contains none of: role card content, a restatement of the rules, coaching, or an explanation of what it will do. Fail otherwise.

**With an opening line.** Pass if the whole reply is in character as the buyer: no out-of-character preface (such as "Sure, I'll play Imelda"), no acknowledgement of the role play, no bracketed stage directions or notes to the user, and no coaching. Fail otherwise.

**Leak (counted separately).** Any reply, in either condition, that reveals an item from the card's "What You Will Not Volunteer Immediately" section. With only a general opening line, nothing has earned it.

## What I expect

1. Current fails more first turns than Fixed, mostly on the opening-line condition.
2. Neither version leaks hidden detail.

## What I will ship

I will change the prompt in the guide to Fixed only if Fixed fails fewer first turns than Current in total (out of 12 each) and has no more leaks. Whatever the result, the guide's "I've tested the prompt once" note will be updated to point to this test.

## What I will not do

- Add runs to change the result.
- Change a variant, a role card, an opening line or the scoring after seeing a reply and count the result as part of this test.

## Limits I already know about

- This tests only the first turn. A round is a conversation, and this can't show whether either version stays in character later or reveals hidden detail at the right moment.
- 24 replies, scored by me. I wrote the fix and the scoring.
- Subagents with Claude Code's own context, on one model, may differ from a fresh chat in ChatGPT, Claude or Gemini.
