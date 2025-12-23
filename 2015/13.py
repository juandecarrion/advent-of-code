import itertools
from pathlib import Path

import numpy as np

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


def solve(add_me=False):
    guests = []
    for line in lines:
        words = line.rstrip(".").split()
        if words[0] not in guests:
            guests.append(words[0])
        if words[10] not in guests:
            guests.append(words[10])
    if add_me:
        guests.append("me")

    a = np.zeros((len(guests), len(guests)))

    for line in lines:
        words = line.rstrip(".").split()
        guest_i = guests.index(words[0])
        guest_j = guests.index(words[10])
        hu = int(words[3])
        if words[2] == "lose":
            hu *= -1
        a[guest_i][guest_j] = hu

    arrangements = list(itertools.permutations(range(len(guests))))

    result = 0
    for arrangement in arrangements:
        left_arrangement = arrangement[1:] + (arrangement[0],)
        right_arrangement = (arrangement[-1],) + arrangement[:-1]
        happiness = 0
        for left, center, right in zip(
            left_arrangement, arrangement, right_arrangement
        ):
            happiness += a[center][left]
            happiness += a[center][right]
        result = int(max(result, happiness))

    return result


p1 = solve(add_me=False)
p2 = solve(add_me=True)

print(p1)
print(p2)
pass
