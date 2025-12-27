from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0


def base_calc_presents(house_number):
    i = 1
    factors = set()
    while i**2 <= house_number:
        if house_number % i == 0:
            factors.add(i)
            factors.add(house_number / i)
        i += 1
    return factors


def calc_presents(house_number):
    result = sum(base_calc_presents(house_number)) * 10
    return result


def calc_presents2(house_number):
    result = 0
    for i in base_calc_presents(house_number):
        if house_number < i + i * 50:
            result += i
    result *= 11
    return result


if TEST:
    assert calc_presents(2) == 30
    assert calc_presents(3) == 40  #   1 + 3
    assert calc_presents(4) == 70  #   1 + 4   + 2
    assert calc_presents(5) == 60  #   1 + 5
    assert calc_presents(6) == 120  #  1 + 6   + 3 + 2
    assert calc_presents(7) == 80  #   1 + 7
    assert calc_presents(8) == 150  #  1 + 8   + 4 + 2
    assert calc_presents(9) == 130  #  1 + 9   + 3
    assert calc_presents(10) == 180  # 1 + 10  + 5 + 2
    assert calc_presents(11) == 120  # 1 + 11
    assert calc_presents(12) == 280  # 1 + 12  + 6 + 4 + 3 + 2
    assert calc_presents(13) == 140  # 1 + 13


limit = int(lines[0])
p1 = 2
max_result = calc_presents(p1)
while limit > max_result:
    p1 += 1
    result = calc_presents(p1)
    if result > max_result:
        max_result = result

p2 = 2
max_result = calc_presents(p2)
while limit > max_result:
    p2 += 1
    result = calc_presents2(p2)
    if result > max_result:
        max_result = result

print(p1)
print(p2)
pass
