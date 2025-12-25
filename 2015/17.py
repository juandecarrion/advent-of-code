import itertools
import sys
from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

TOTAL = 25 if TEST else 150

containers = []
for line in lines:
    containers.append(int(line))


min_num_containers = sys.maxsize
for L in range(len(containers) + 1):
    for subset in itertools.combinations(containers, L):
        if sum(subset) == TOTAL:
            p1 += 1
            min_num_containers = min(min_num_containers, len(subset))


for L in range(len(containers) + 1):
    for subset in itertools.combinations(containers, L):
        if sum(subset) == TOTAL and len(subset) == min_num_containers:
            p2 += 1

print(p1)
print(p2)
pass
