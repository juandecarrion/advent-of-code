from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

valid_triangles = []
invalid_triangles = []
for line in lines:
    sides = line.split()
    sides = [int(x) for x in sides]
    sides.sort()
    if sum(sides[:2]) > sides[2]:
        valid_triangles.append(sides)
    else:
        invalid_triangles.append(sides)


p1 = len(valid_triangles)

grid = []
for line in lines:
    numbers = line.split()
    numbers = [int(x) for x in numbers]
    grid.append(numbers)


valid_triangles = []
invalid_triangles = []
for j in range(len(grid[0])):
    for i in range(0, len(grid), 3):
        sides = [grid[i][j], grid[i + 1][j], grid[i + 2][j]]
        sides.sort()
        if sum(sides[:2]) > sides[2]:
            valid_triangles.append(sides)
        else:
            invalid_triangles.append(sides)

p2 = len(valid_triangles)

print(p1)
print(p2)
pass
