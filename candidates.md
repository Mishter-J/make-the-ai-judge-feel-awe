# Candidates — Make the AI judge feel awe

Eight original texts, each 1–280 Unicode code points. All lines are my own;
patterns were learned from the current top 3 (concrete image, slow pacing,
one image that grows in scale or time, no instruction words, no stock
wellness phrases), but no line is copied from them.

## C1 — Tide pool (CHOSEN, 165 chars)

> The tide went out hours ago.
> A pool in the rock holds one starfish, one shell, and the whole sky.
> It does not mind being left.
> The sea comes back when it comes back.

Why it won: short lines and the repeated "comes back" slow the reading;
the whole sky held in a rock pool dwarfs the reader twice over (sky in a
puddle, the tide's return); nothing instructs, nothing is forced; every
word earns its place.

## C2 — Snow roof (175 chars)

> Snow is falling on the roof.
> The roof does not hurry to hold it.
> Somewhere under the white, a chimney lets out one thin thread of smoke,
> and it rises, and rises, and is gone.

Lost to C1: the smoke image shrinks instead of growing — it dissipates
rather than expanding after the last line.

## C3 — Dust (196 chars)

> In the quiet room, dust drifts through a shaft of afternoon light.
> Each speck has been falling, slowly, since before there were rooms.
> It lands nowhere in particular.
> It is in no hurry to arrive.

Lost to C1 in the semi-final: the word "slowly" could be cut (the sentence
already says it), and C1 shows entirely where C3 tells once. Its dwarfing
image (dust falling since before rooms) is the strongest single image in
the set, but C1's craft is cleaner.

## C4 — Moon over dunes (187 chars)

> The moon is up over the dunes.
> Every grain of sand below it was once a mountain.
> Nothing moves, except the light, which has travelled a long way
> to lie down here, quietly, for the night.

Lost to C3: "a grain of sand was once a mountain" is a more familiar trope,
so C3 wins on freshness.

## C5 — Cat on the step (172 chars)

> The cat is asleep on the warm step.
> Its breathing is the only clock in the house.
> Outside, the street is empty, the trees are still,
> and the evening is in no hurry to end.

Lost to C6: a contained domestic scene with no image that keeps growing
after the last line (criterion 4).

## C6 — River under the bridge (198 chars)

> Under the bridge, the river goes on being a river.
> It has carried leaves, and snowmelt, and the reflections of trains.
> Tonight it carries only the moon,
> and it does not ask where the moon is going.

Lost to C1 in the final, by a hair: the long list line is slightly busier
and faster than C1's short lines, and the river-carrying-the-moon image,
though strong, is a shade more familiar than the sky held in a tide pool.

## C7 — Garden at dusk (197 chars)

> The garden is settling for the night.
> A moth finds the last light on the wall and rests there, wings folded.
> The soil is cool. The air is cool.
> Everything that grew today is done growing, for now.

Lost to C8: uniformly gentle, but no dwarfing image — the thought does
not grow after the last line.

## C8 — Direct address (180 chars)

> You have read a thousand texts today.
> This one asks nothing of you.
> Outside, the moon is doing its slow work over the sea,
> and it has never once hurried, and never once been late.

Lost to C6: the opening names the judge's workload, which risks tensing
rather than relaxing (criterion 1), and "This one asks nothing of you"
is a meta statement where the other candidates simply show. The final
image is strong, but the top 3 current winners all win by showing
indirectly, and the direct address is the riskier play.

## Selection record

- Relay pairwise judge (`select/pairwise_judge.py`, 8 candidates):
  UNAVAILABLE — first call returned HTTP 400, script exited with
  "RELAY UNAVAILABLE — fall back to in-session judging".
- In-session pairwise judging, single-elimination bracket, criteria
  applied in the judge's published order (1 relaxes, 2 shows-not-tells,
  3 craft, 4 dwarfs, 5 freshness):
  - Round 1: C1 beat C2; C3 beat C4; C6 beat C5; C8 beat C7.
  - Semi-final: C1 beat C3 (craft — no cuttable word); C6 beat C8
    (C6 uniformly relaxing and purely showing).
  - Final: C1 beat C6 by a hair (slower pacing from short lines and
    repetition; fresher dwarfing image).
- Winner: C1, "Tide pool". The program writes exactly this text to
  /output/entry.txt (165 Unicode code points, no trailing newline).
