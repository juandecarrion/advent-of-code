from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


def turn_right(direction):
    match direction:
        case (1, 0):
            return 0, 1
        case (0, 1):
            return -1, 0
        case (-1, 0):
            return 0, -1
        case (0, -1):
            return 1, 0
    raise NotImplementedError()


def turn_left(direction):
    match direction:
        case (1, 0):
            return 0, -1
        case (0, -1):
            return -1, 0
        case (-1, 0):
            return 0, 1
        case (0, 1):
            return 1, 0
    raise NotImplementedError()


def calc_taxicab(instructions):
    direction = (1, 0)
    pos = (0, 0)
    for instruction in instructions.split(", "):
        turn, dist = instruction[0], int(instruction[1:])
        direction = turn_right(direction) if turn == "R" else turn_left(direction)
        pos = pos[0] + direction[0] * dist, pos[1] + direction[1] * dist
    return abs(pos[0]) + abs(pos[1])


def calc_taxicab2(instructions):
    direction = (1, 0)
    pos = (0, 0)
    visited_pos = [pos]
    for instruction in instructions.split(", "):
        turn, dist = instruction[0], int(instruction[1:])
        direction = turn_right(direction) if turn == "R" else turn_left(direction)
        for _ in range(dist):
            pos = pos[0] + direction[0] * 1, pos[1] + direction[1] * 1
            if pos in visited_pos:
                return abs(pos[0]) + abs(pos[1])
            visited_pos.append(pos)

    raise Exception("Solution not found")


def check_taxicab(instructions, expected):
    result = calc_taxicab(instructions)
    assert result == expected


for tc in [
    ("R2, L3", 5),
    ("R2, R2, R2", 2),
    ("R5, L5, R5, R3", 12),
]:
    check_taxicab(tc[0], tc[1])

p1 = 0
p2 = 0

p1 += calc_taxicab(lines[0])
p2 += calc_taxicab2(lines[0])


print(p1)
print(p2)
pass
