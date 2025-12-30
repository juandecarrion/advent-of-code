import hashlib
from pathlib import Path

TEST = True
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = ""
p2 = "????????"

i = 0
while True:
    i += 1
    to_hash = input_str + str(i)
    hash_str = hashlib.md5(to_hash.encode()).hexdigest()
    if hash_str.startswith("00000"):
        if len(p1) < 8:
            p1 += hash_str[5]
        if hash_str[5].isdigit():
            index = int(hash_str[5])
            if 0 <= index <= 7 and p2[index] == "?":
                p2 = p2[:index] + hash_str[6] + p2[index + 1 :]
    if len(p1) >= 8 and "?" not in p2:
        break

print(p1)
print(p2)
pass
