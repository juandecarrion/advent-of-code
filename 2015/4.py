import hashlib
from pathlib import Path

day = Path(__file__).stem
input_file = f"{day}.txt"
input_str = open(input_file).read()
lines = input_str.split("\n")

p1 = 0
p2 = 0

secret = input_str.strip()

for i in range(1000 * 1000 * 1000):
    md5 = hashlib.md5((secret + str(i)).encode()).hexdigest()
    if md5[:5] == "00000":
        p1 = i
        break

for i in range(1000 * 1000 * 1000):
    md5 = hashlib.md5((secret + str(i)).encode()).hexdigest()
    if md5[:6] == "000000":
        p2 = i
        break

print(p1)
print(p2)
pass
