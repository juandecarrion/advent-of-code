from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

screen = []
width, height = (50, 6) if not TEST else (7, 3)

grid = []
for i in range(height):
    grid.append(["."] * width)


if TEST:
    test_steps = [
        """
    ###....
    ###....
    .......
    """,
        """
    #.#....
    ###....
    .#.....
    """,
        """
    ....#.#
    ###....
    .#.....
    """,
        """
    .#..#.#
    #.#....
    .#.....
    """,
    ]

    for i, test_step in enumerate(test_steps):
        test_step = test_step.strip().split("\n")
        test_steps[i] = [list(x.strip()) for x in test_step]
        pass

for i, line in enumerate(lines):
    instruction = line.split(" ")
    match instruction[0]:
        case "rect":
            axb = instruction[1]
            a, b = axb.split("x")
            a = int(a)
            b = int(b)
            for y in range(b):
                for x in range(a):
                    grid[y][x] = "#"
        case "rotate":
            index = int(instruction[2].split("=")[1])
            pixels = int(instruction[-1])
            if instruction[1] == "column":
                previous_values = []
                for y in range(height):
                    previous_values.append(grid[y][index])
                for y in range(height):
                    grid[y][index] = previous_values[(y - pixels) % height]
            if instruction[1] == "row":
                previous_values = []
                for x in range(width):
                    previous_values.append(grid[index][x])
                for x in range(width):
                    grid[index][x] = previous_values[(x - pixels) % width]
    if TEST:
        print(i)
        assert grid == test_steps[i]

for row in grid:
    for char in row:
        p1 += 1 if char == "#" else 0


print(p1)
for row in grid:
    print("".join(row).replace(".", " "))
pass
