"""Write Magda Salt-Hands' villain monologue to entry.txt.

Deterministic, stdlib only, no network. The monologue is a fixed string:
about 100 words, under 600 characters, spoken by a witch of the White
Flats who has spent three centuries salting the kingdom's fields, and
who tonight salts the mountain pass so the hero's army starves before
the gate. Her exhaustion lives in the pauses and deflections, never in
a word that names it.
"""

import os

MONOLOGUE = (
    "Come in. Mind the step — no, the other one. Sit. "
    "I was... salting the pass at dusk. Three hundred years, "
    "pinch by pinch, and the kingdom still sends boys with "
    "bright swords to ask why nothing grows. The fields. The roads. "
    "The wells. All mine, one pinch at a time. I heard your boots "
    "crunch salt past the ridge. Brave lads. Hungry lads, soon. "
    "Hold this jar a moment, will you? Nearly empty. Ah — there it "
    "is. You came to kill me, and I have already won. Walk on, "
    "hero. The gate is yours. The bread is mine."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
