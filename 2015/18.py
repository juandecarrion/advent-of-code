import copy
from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

grid = []
for line in lines:
    grid.append([])
    for c in line:
        grid[-1].append(c)

NO_OF_ITERATIONS = 5 if TEST else 100

previous_grid = copy.deepcopy(grid)
previous_grid2 = copy.deepcopy(grid)


def get_light(previous_grid, i, j, is_p2=False):
    if is_p2:
        if (
            (i == 0 and j == 0)
            or (i == 0 and j == len(previous_grid[0]) - 1)
            or (i == len(previous_grid[0]) - 1 and j == 0)
            or (i == len(previous_grid[0]) - 1 and j == len(previous_grid[0]) - 1)
        ):
            return "#"
    previous_state = previous_grid[i][j]
    neighbours = []
    for pos in [
        (i - 1, j - 1),
        (i - 1, j + 0),
        (i - 1, j + 1),
        (i + 0, j - 1),
        (i + 0, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 0),
        (i + 1, j + 1),
    ]:
        if 0 <= pos[0] < len(previous_grid) and 0 <= pos[1] < len(previous_grid[0]):
            neighbours.append(previous_grid[pos[0]][pos[1]])
    neighbours_on = 0
    for neighbour in neighbours:
        if neighbour == "#":
            neighbours_on += 1
    return (
        "#"
        if (previous_state == "#" and neighbours_on in [2, 3])
        or (previous_state == "." and neighbours_on == 3)
        else "."
    )


for step in range(NO_OF_ITERATIONS):
    next_grid = copy.deepcopy(previous_grid)
    next_grid2 = copy.deepcopy(previous_grid2)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            next_grid[i][j] = get_light(previous_grid, i, j, is_p2=False)
            next_grid2[i][j] = get_light(previous_grid2, i, j, is_p2=True)
    previous_grid = next_grid
    previous_grid2 = next_grid2
    pass

for l in previous_grid:
    for c in l:
        if c == "#":
            p1 += 1

for l in previous_grid2:
    for c in l:
        if c == "#":
            p2 += 1


print(p1)
print(p2)
pass
