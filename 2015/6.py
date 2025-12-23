from pathlib import Path

day = Path(__file__).stem
input_file = f"{day}.txt"
input_str = open(input_file).read()
lines = input_str.split("\n")

p1 = 0
p2 = 0

grid = {}
for i in range(1000):
    for j in range(1000):
        grid[(i, j)] = False

grid2 = {}
for i in range(1000):
    for j in range(1000):
        grid2[(i, j)] = 0

for l in lines:
    if not l:
        continue
    if l.startswith("turn"):
        l = l[len("turn ") :]
    l = l.replace(",", " ")
    a, b, c, d, e, f = l.split()
    b = int(b)
    c = int(c)
    e = int(e)
    f = int(f)

    if b < e:
        min_x = b
        max_x = e
    else:
        min_x = e
        max_x = b

    if c < f:
        min_y = c
        max_y = f
    else:
        min_y = f
        max_y = c

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if a == "toggle":
                grid[(y, x)] = not grid[(y, x)]
                grid2[(y, x)] += 2
            elif a == "on":
                grid[(y, x)] = True
                grid2[(y, x)] += 1
            else:
                grid[(y, x)] = False
                if grid2[(y, x)] > 0:
                    grid2[(y, x)] -= 1

for v in grid.values():
    if v:
        p1 += 1

for v in grid2.values():
    p2 += v

print(p1)
print(p2)
pass
