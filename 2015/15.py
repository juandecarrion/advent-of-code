from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

ingredients = []
a = []
for line in lines:
    words = line.replace(",", "").split()

    ingredient = words[0].rstrip(":")
    capacity = int(words[2])
    durability = int(words[4])
    flavor = int(words[6])
    texture = int(words[8])
    calories = int(words[10])

    ingredients.append(ingredient)
    a.append([capacity, durability, flavor, texture, calories])

ingredient_count = len(a)

# x1 + x2 + x3 + x4 = 100
# x1 >= 1; x2 >= 1; x3 >= 1; x4 >= 1;
# maximize(
#   (a1 * x1 + a2 * x2 + a3 * x3 + a4 * x4) *
#   (b1 * x1 + b2 * x2 + b3 * x3 + b4 * x4) *
#   (c1 * c1 + c2 * x2 + c3 * x3 + c4 * x4) *
#   (d1 * x1 + d2 * x2 + d3 * d3 + d4 * x4)
# )


def objective(x):
    result = 1
    for j in range(len(a[0]) - 1):
        inter = 0
        for i in range(len(a)):
            inter += a[i][j] * x[i]
        result *= inter if inter > 0 else 0
    return result


if TEST:
    assert objective([44, 56]) == 62842880


def solve(is_p2=False):
    result = 0
    if TEST:
        for i in range(1, 100):
            l = 100 - i
            calories = a[0][-1] * i + a[1][-1] * l
            if not is_p2 or calories == 500:
                o = objective([i, l])
                if o >= result:
                    result = o
    else:
        for i in range(1, 100):
            for j in range(1, 100 - i):
                for k in range(1, 100 - i - j):
                    l = 100 - i - j - k
                    calories = a[0][-1] * i + a[1][-1] * j + a[2][-1] * k + a[3][-1] * l
                    if not is_p2 or calories == 500:
                        o = objective([i, j, k, l])
                        if o >= result:
                            result = o
    return result


p1 = solve(is_p2=False)
p2 = solve(is_p2=True)

print(p1)
print(p2)
pass
