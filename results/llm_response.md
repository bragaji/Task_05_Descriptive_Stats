## “How many games did the team play?”
22 games
(16 wins, 6 losses)

## “Who contributed most to team success based on scoring + caused turnovers?”
| Player           | Goals | CT | Total Contribution |
| ---------------- | ----- | -- | ------------------ |
| **Emma Tyrrell** | 70    | 7  | **77** ✅           |
| Olivia Adamson   | 58    | 7  | 65                 |
| Emma Ward        | 44    | 3  | 47                 |
| Natalie Smith    | 44    | 8  | 52                 |

Conclusion: Emma Tyrrell contributed the most based on combined scoring and defensive impact.

## “Should the team focus on offense or defense to win 2 more games next season?”

Offense:
Goals scored: 335 (15.2/game)

Shot %: 46.8%

Assists: 150

Top scorers (Tyrrell, Adamson, Ward) are highly efficient.

Defense:
Goals allowed: 213 (9.7/game)

Caused Turnovers: 210

Save %: .418 (below opponent save rate)

Opponent goals in losses: avg ~13–15

Recommendation:
To convert close losses (e.g., 8–9 vs Maryland, 10–11 vs Boston College) into wins, improving goalie performance and defensive coverage would yield the biggest impact. So, focus on defense.

## “Who is the most improved player?”

While there is no direct past-season comparison, based on usage stats and contributions:

Natalie Smith had:

44 Goals (3rd best scorer)

24 CT (among top 3 defenders)

36 Draw Controls

She appears to be a two-way impact player, possibly stepping into a much larger role.

## “Which player had the highest goal-to-shot ratio?”
| Player         | Goals | Shots | G/S Ratio   |
| -------------- | ----- | ----- | ----------- |
| **Emma Ward**  | 44    | 90    | **0.489** ✅ |
| Emma Tyrrell   | 70    | 135   | 0.518       |
| Olivia Adamson | 58    | 109   | 0.532       |
| Natalie Smith  |       |       |             |






##################################### Advance Questions Responses ################################################

1) Did location impact win probability?

Records by venue: Home 9–2, Away 5–2, Neutral 2–2.
Empirical win rates:

Home: 9/11 = 81.8%

Away: 5/7 = 71.4%

Neutral: 2/4 = 50.0%
Overall: 16/22 = 72.7%.

Takeaway: Playing at home increased win probability by ~+10 percentage points vs away (81.8% vs 71.4%), and ~+31 points vs neutral. That’s a material home-ice (home-turf) effect in this sample. (We can’t test statistical significance without game-by-game expected values, but the gap is sizable.)

2) Offense or defense to add 2 more wins next season?

What the team already does well:

Scoring: 15.23 goals/game on .468 shooting — strong.

Possession start: Massive edge on draw controls (384–234, +150).

Turnovers/CTs: +40 in caused turnovers (210–170).
Where there’s headroom:

Clears: SU .910 vs opponents .932 — trailing here gives opponents extra possessions.

Ground balls: SU 327 vs opponents 351 (–24).

Goalie save%: SU .418 vs opponents .357 (note: the opponent figure is how their goalies fared vs SU shooters; SU’s .418 is good, but closing out top teams may need a bump).

Close-loss pattern: Three one-goal losses (Maryland 8–9, Stony Brook 12–13, BC 10–11) plus two multi-goal defeats to BC in postseason (7–10, 8–15). Marginal defensive tightening (clears/GBs/save%) is more likely to flip those one-goal results than trying to squeeze more efficiency from an already elite offense. Recommendation: Emphasize defense/possession protection (clear efficiency, ground-ball wins, incremental save% improvement). That path most plausibly adds ~2 wins.

3) Which player contributed most to wins (offense + defense)?

Data we have: Goals, assists, ground balls (GB), caused turnovers (CT), draw controls (DC). No direct on/off or possession value, so I’ll define a simple two-way contribution index:

Two-Way Index = Points (G+A) + [GB + CT + 0.7×DC]
Rationale: a point ≈ direct scoring; GB/CT add possessions or remove opponent chances; DC is a possession start (very valuable), weighted at 0.7 so it doesn’t swamp pure scoring.

Top candidates (from the stat table):

Kate Mashewske (FO specialist): 0 pts; DC 234, GB 1, CT 1 ⇒ Defense block = 1 + 1 + 0.7×234 = 165.8 ⇒ 165.8 total.

Emma Tyrrell: 92 pts; GB 21, CT 7, DC 6 ⇒ 92 + (21 + 7 + 0.7×6=32.2) = 124.2.

Olivia Adamson: 83 pts; GB 12, CT 7, DC 6 ⇒ 83 + 23.2 = 106.2.

Natalie Smith: 54 pts; GB 11, CT 8, DC 36 ⇒ 54 + (11+8+25.2=44.2) = 98.2.

Emma Ward: 81 pts; GB 10, CT 3, DC 0 ⇒ 94.0.

Answer: By any possession-valuing metric, Kate Mashewske contributed the most to wins via an enormous draw-control advantage (234 DC). If you only count points, Emma Tyrrell leads (92). Given how DCs drive possession and therefore win probability, Kate is #1 overall in impact in this framework.

4) Most improved player (first half → second half)?

We need per-game splits by player to measure improvement (e.g., first 11 vs last 11: points/game, DCs/game, GBs/CTs/game, shooting%). The uploaded PDF has season totals only, not game-by-game logs. Therefore, we cannot identify the most-improved player from this file alone.

How I would measure it (if we had game logs):

Define Improvement Score = (2nd-half rate – 1st-half rate) for: Points/game, Usage (shots), Efficiency (shot%/FP%), and Defensive rate (GB+CT+0.7×DC per game).

Normalize to z-scores and sum for a composite, weighting efficiency higher to avoid pure-volume artifacts.

5) Projection if defense improves by 15%, offense same

Assumption: “Defense +15%” = 15% fewer goals allowed per game. Current GA/G = 9.68 ⇒ improved GA/G = 9.68 × (1–0.15) = 8.23. Offense stays at GF/G = 15.23. Use a standard Pythagorean expectation (exponent ≈ 2) to translate scoring to win%:

Current: Win% ≈ 15.23² / (15.23² + 9.68²) ≈ 0.71 (matches 16–6 ~72.7%).

With improved defense: Win% ≈ 15.23² / (15.23² + 8.23²) ≈ 0.77 ⇒ over 22 games ≈ 17–5.

Close-game adjustment: There were three one-goal losses. A 15% defensive reduction plausibly flips 1–2 of those. That yields a realistic range of 17–5 to 18–4, depending on schedule strength and end-game variance.
