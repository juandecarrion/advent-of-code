from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = ""
p2 = ""

frequency = []
for i in lines[0]:
    frequency.append({})

for line in lines:
    for j, char in enumerate(line):
        if char not in frequency[j]:
            frequency[j][char] = 1
        else:
            frequency[j][char] += 1

for column in frequency:
    items = list(column.items())
    items.sort(key=lambda x: x[1], reverse=True)
    p1 += str(items[0][0])
    p2 += str(items[-1][0])
    pass


print(p1)
print(p2)
pass
