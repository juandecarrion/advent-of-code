import itertools
import sys
from pathlib import Path
import numpy as np

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

# It could be faster with something like this: https://medium.com/@codingguy/traveling-salesman-problem-a-speed-battle-between-python-and-go-93ea447669d6

i = 0
cities = {}
for line in lines:
    orig, _, dest, _, dist = line.split()
    if orig not in cities:
        cities[orig] = i
        i += 1
    if dest not in cities:
        cities[dest] = i
        i += 1

city_count = len(cities)

dist_a = np.zeros((city_count, city_count))
for line in lines:
    orig, _, dest, _, dist = line.split()
    orig = cities[orig]
    dest = cities[dest]
    dist = int(dist)
    dist_a[orig][dest] = dist
    dist_a[dest][orig] = dist

possible_ways = list(itertools.permutations(cities.values()))

p1 = sys.maxsize
for way in possible_ways:
    way_dist = 0
    for previous, current in zip(way, way[1:]):
        way_dist += dist_a[previous][current]
    p1 = min(way_dist, p1)
    p2 = max(way_dist, p2)

print(p1)
print(p2)
pass
