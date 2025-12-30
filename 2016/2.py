from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

keypad_lines = """
1 2 3
4 5 6
7 8 9
""".strip().split("\n")

keypad = []
for kl in keypad_lines:
    keypad.append(kl.split())

p1 = ""
x = 1
y = 1
for l in lines:
    for c in l:
        match c:
            case "U":
                x -= 1 if x > 0 else 0
            case "D":
                x += +1 if x < 2 else 0
            case "L":
                y -= 1 if y > 0 else 0
            case "R":
                y += 1 if y < 2 else 0
    p1 += keypad[x][y]


keypad2 = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]
x = 2
y = 0
p2 = ""
for l in lines:
    for c in l:
        match c:
            case "U":
                x -= 1 if x > 0 and keypad2[x - 1][y] != " " else 0
            case "D":
                x += +1 if x < 4 and keypad2[x + 1][y] != " " else 0
            case "L":
                y -= 1 if y > 0 and keypad2[x][y - 1] != " " else 0
            case "R":
                y += 1 if y < 4 and keypad2[x][y + 1] != " " else 0
    p2 += keypad2[x][y]

print(p1)
print(p2)
pass
