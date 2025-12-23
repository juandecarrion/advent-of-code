from pathlib import Path

day = Path(__file__).stem
input_file = f"{day}.txt"
input_str = open(input_file).read()

p1 = 0
p2 = 0
for c in input_str:
    if c == "(":
        p1 += 1
    elif c == ")":
        p1 -= 1
    p2 += 1
    if p1 == -1:
        break

print(p1)
print(p2)
