import random
import sys
from functools import reduce
from operator import mul
from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0


packages = []
for line in lines:
    packages.append(int(line))

total_weight = sum(packages)
weight_per_group = total_weight // 3

ITERATION_FACTOR = 2**20
options = set()
for i in range(1, 7):
    for _ in range(ITERATION_FACTOR):
        random.shuffle(packages)
        first_group = packages[:i]
        if sum(first_group) == weight_per_group:
            rest = packages[i:]
            for _ in range(ITERATION_FACTOR):
                random.shuffle(rest)
                for j in range(1, len(rest) - 1):
                    second_group = sum(rest[:j])
                    third_group = sum(rest[j:])
                    if second_group == third_group == weight_per_group:
                        options.add(tuple(sorted(first_group)))
    if options:
        break

p1 = sys.maxsize
# p1 = 270894973147
# p1 = 102937852963
# p1 = 48585083935
# p1 = 30367698987
# p1 = 29728298883
# p1 = 10542541903
# p1 = 10439961859
# p1 = 10439961859
for option in options:
    entanglement = reduce(mul, option)
    if entanglement <= p1:
        print(len(option), entanglement, option)
        p1 = min(p1, entanglement)

print(p1)
print(p2)
pass
