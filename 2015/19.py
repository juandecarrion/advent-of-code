import random
from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

is_replacement = True
replacements = []
medicine_molecule = ""
for line in lines:
    if not line:
        is_replacement = False
        continue
    if is_replacement:
        k, v = line.split(" => ")
        replacements.append((k, v))
    else:
        medicine_molecule = line


unique_replacements = set()
for i in range(len(medicine_molecule)):
    for k, v in replacements:
        len_k = len(k)
        if medicine_molecule[i : i + len_k] == k:
            unique_replacements.add(
                medicine_molecule[:i] + v + medicine_molecule[i + len_k :]
            )


# replacements = sorted(replacements, key=lambda x: len(x[1]), reverse=True)


def find_path(current_molecule, end, steps=0):
    random.shuffle(replacements)
    previous_molecule = ""
    while previous_molecule != current_molecule:
        previous_molecule = current_molecule
        for k, v in replacements:
            while v in current_molecule:
                steps += current_molecule.count(v)
                current_molecule = current_molecule.replace(v, k)
    if current_molecule == end:
        return steps
    else:
        return 0


p1 = len(unique_replacements)


end = "e"
while not p2:
    p2 = find_path(medicine_molecule, end, steps=0)

print(p1)
print(p2)
pass
