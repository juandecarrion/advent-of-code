from pathlib import Path

TEST = True
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

test_cases = [
    ("ADVENT", "ADVENT"),
    ("A(1x5)BC", "ABBBBBC"),
    ("(3x3)XYZ", "XYZXYZXYZ"),
    ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"),
    ("(6x1)(1x3)A", "(1x3)A"),
    ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
]

test_cases2 = [
    ("(3x3)XYZ", 9),
    ("X(8x2)(3x3)ABCY", 20),
    ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
    ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
]


def decompress(compressed):
    result = ""
    i = 0
    while i < len(compressed):
        if compressed[i] == "(":
            end = compressed[i + 1 :].find(")")
            end = i + end + 1
            marker = compressed[i + 1 : end]
            length, times = marker.split("x")
            length = int(length)
            times = int(times)
            to_repeat = compressed[end + 1 : end + length + 1]
            for j in range(times):
                result += to_repeat
            i = end + length + 1
        else:
            result += compressed[i]
            i += 1
    return result


def check_test_case(compressed, expected):
    result = decompress(compressed)
    assert result == expected


def decompress2(compressed):
    result = 0
    i = 0
    while i < len(compressed):
        if compressed[i] == "(":
            end = compressed[i + 1 :].find(")")
            end = i + end + 1
            marker = compressed[i + 1 : end]
            length, times = marker.split("x")
            length = int(length)
            times = int(times)
            to_repeat = compressed[end + 1 : end + length + 1]
            result += times * decompress2(to_repeat)
            i = end + length + 1
        else:
            result += 1
            i += 1
    return result


def check_test_case2(compressed, expected):
    result = decompress2(compressed)
    assert result == expected


for test_case in test_cases:
    check_test_case(test_case[0], test_case[1])


for test_case in test_cases2:
    check_test_case2(test_case[0], test_case[1])


result = decompress(input_str)
p1 += len(result)

p2 += decompress2(input_str)

print(p1)
print(p2)
pass
