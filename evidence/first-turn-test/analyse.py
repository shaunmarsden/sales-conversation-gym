"""Unblind the first-turn test and add up the totals. Run with:
python3 evidence/first-turn-test/analyse.py evidence/first-turn-test
"""
import json, sys
from pathlib import Path
folder = Path(sys.argv[1])
mapping = json.loads((folder / "mapping.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
for arm in ("current", "fixed"):
    for turn in ("setup", "opening"):
        cs = [c for c, m in mapping.items() if m["arm"] == arm and m["turn"] == turn]
        for c in cs:
            assert scores[c]["turn"] == turn, c
        print(f'{arm:8} {turn:8} pass={sum(scores[c]["pass"] for c in cs)}/{len(cs)} '
              f'leaks={sum(scores[c]["leak"] for c in cs)}')
