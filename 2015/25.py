import re
from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

code_row, code_column = re.findall(r"\d+", lines[0])
code_pos = (int(code_row), int(code_column))


def get_next_pos(pos):
    x, y = pos
    return (x - 1, y + 1) if x > 1 else (y + 1, 1)


def test_get_next_pos(pos, next_pos):
    assert get_next_pos(pos) == next_pos


"""
   | 1   2   3   4   5   6  
---+---+---+---+---+---+---+
 1 |  1   3   6  10  15  21
 2 |  2   5   9  14  20
 3 |  4   8  13  19
 4 |  7  12  18
 5 | 11  17
 6 | 16
"""

if TEST:
    test_get_next_pos((1, 1), (2, 1))
    test_get_next_pos((2, 1), (1, 2))
    test_get_next_pos((1, 2), (3, 1))
    test_get_next_pos((3, 1), (2, 2))
    test_get_next_pos((2, 2), (1, 3))
    test_get_next_pos((1, 3), (4, 1))
    test_get_next_pos((4, 1), (3, 2))
    test_get_next_pos((3, 2), (2, 3))
    test_get_next_pos((2, 3), (1, 4))


def get_next_value(value):
    result = value * 252533
    result = result % 33554393
    return result


def test_get_next_val(value, next_value):
    assert get_next_value(value) == next_value


"""
   |    1         2         3         4         5         6
---+---------+---------+---------+---------+---------+---------+
 1 | 20151125  18749137  17289845  30943339  10071777  33511524
 2 | 31916031  21629792  16929656   7726640  15514188   4041754
 3 | 16080970   8057251   1601130   7981243  11661866  16474243
 4 | 24592653  32451966  21345942   9380097  10600672  31527494
 5 |    77061  17552253  28094349   6899651   9250759  31663883
 6 | 33071741   6796745  25397450  24659492   1534922  27995004
"""


if TEST:
    test_get_next_val(20151125, 31916031)
    test_get_next_val(31916031, 18749137)
    test_get_next_val(18749137, 16080970)
    test_get_next_val(16080970, 21629792)
    test_get_next_val(21629792, 17289845)
    test_get_next_val(17289845, 24592653)


pos = (1, 1)
value = 20151125
while True:
    pos = get_next_pos(pos)
    value = get_next_value(value)
    if pos == code_pos:
        p1 = value
        break


print(p1)
print(p2)
pass
