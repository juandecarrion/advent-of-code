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


def solve(no_of_groups):
    total_weight = sum(packages)
    weight_per_group = total_weight // no_of_groups

    ITERATION_FACTOR = 2**19
    options = set()
    for i in range(1, len(packages)):
        for _ in range(ITERATION_FACTOR):
            random.shuffle(packages)
            first_group = packages[:i]
            if sum(first_group) == weight_per_group:
                rest = packages[i:]
                for _ in range(ITERATION_FACTOR):
                    matches = False
                    random.shuffle(rest)
                    if no_of_groups == 3:
                        for j in range(1, len(rest) - 1):
                            second_group = rest[:j]
                            third_group = rest[j:]
                            if (
                                sum(second_group)
                                == sum(third_group)
                                == weight_per_group
                            ):
                                for group in [first_group, second_group, third_group]:
                                    if len(group) == i:
                                        options.add(tuple(sorted(group)))
                                matches = True
                    else:
                        for j in range(1, len(rest) - 2):
                            for k in range(j + 1, len(rest) - 1):
                                second_group = rest[:j]
                                third_group = rest[j:k]
                                fourth_group = rest[k:]
                                if (
                                    sum(second_group)
                                    == sum(third_group)
                                    == sum(fourth_group)
                                    == weight_per_group
                                ):
                                    for group in [
                                        first_group,
                                        second_group,
                                        third_group,
                                        fourth_group,
                                    ]:
                                        if len(group) == i:
                                            options.add(tuple(sorted(group)))
                                    matches = True
                    if matches:
                        break
        if options:
            break

    result = sys.maxsize
    for option in options:
        entanglement = reduce(mul, option)
        result = min(result, entanglement)

    return result


p1 = solve(no_of_groups=3)
p2 = solve(no_of_groups=4)

print(p1)
print(p2)
pass
