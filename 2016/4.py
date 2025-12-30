from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

names = []
sector_ids = []
checksums = []

for line in lines:
    line_split = line.split("-")
    name = line_split[:-1]
    name = "-".join(name)
    sector_id, checksum = line_split[-1].split("[")
    sector_id = int(sector_id)
    checksum = checksum.strip("[]")
    names.append(name)
    sector_ids.append(sector_id)
    checksums.append(checksum)


def calc_checksum(name):
    name = name.replace("-", "")
    count = {}
    for c in name:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    count_pairs = list(count.items())
    count_pairs.sort(key=lambda x: x[1] * 100 - ord(x[0]), reverse=True)
    result = ""
    for i in range(5):
        result += str(count_pairs[i][0])
    return result


for i in range(0, len(names)):
    checksum = calc_checksum(names[i])
    if checksum == checksums[i]:
        p1 += sector_ids[i]


def decrypt(encrypted_str, sector_id):
    sector_id = sector_id % 26
    decrypted_str = ""
    for c in encrypted_str:
        if c == "-":
            decrypted_str += " "
        else:
            decrypted_char = ord(c) + sector_id
            if decrypted_char > ord("z"):
                decrypted_char -= 26
            decrypted_str += chr(decrypted_char)
    return decrypted_str


assert decrypt("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name"

for i in range(len(names)):
    if decrypt(names[i], sector_ids[i]) == "northpole object storage":
        p2 += sector_ids[i]


print(p1)
print(p2)
pass
