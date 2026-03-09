"""convert piqa-dan.json to piqa-dan.tsv with the columns prompt, solution0, solution1, label

currently almost all labels are 0 (i.e. solution0), but we will shuffle them in this file and change the labels accordingly
"""

import json
import random
from pathlib import Path

with Path("piqa-dan.json").open() as f:
    data = json.load(f)

# shuffle the solutions and change the labels accordingly
for example in data:
    # sample if true should be 0 or 1
    solution0_should_be_correct = random.random() < 0.5
    solution0_is_correct = example["label"] == 0
    if solution0_should_be_correct != solution0_is_correct:
        # swap the solutions
        example["solution0"], example["solution1"] = (
            example["solution1"],
            example["solution0"],
        )
        # change the label
        example["label"] = 1 - example["label"]


with Path("piqa-dan.tsv").open("w") as f:
    f.write("prompt\tsolution0\tsolution1\tlabel\n")
    for example in data:
        f.write(
            f"{example['prompt']}\t{example['solution0']}\t{example['solution1']}\t{example['label']}\n"
        )
