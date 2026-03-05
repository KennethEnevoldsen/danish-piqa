import json
from pathlib import Path

with Path("piqa-dan.json").open() as f:
    data = json.load(f)

for i, example in enumerate(data):
    example["id"] = i
    text = f"{example['prompt']} {example['solution0']} "
    example["n_words"] = len(text.split())

with Path("piqa-dan.json").open("w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"we have a total of {len(data)} examples")
print(
    f"we have a average length of {sum(example['n_words'] for example in data) / len(data):.2f} words per example"
)
