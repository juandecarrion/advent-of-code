from pathlib import Path

TEST = True

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
guests = []
for line in lines:
    words = line.rstrip(".").split()
    if words[0] not in guests:
        guests.append(words[0])
    if words[10] not in guests:
        guests.append(words[10])


print(p1)
print(p2)
pass
