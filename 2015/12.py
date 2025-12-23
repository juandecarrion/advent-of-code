import re
from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f'{day}.test.txt' if TEST else f'{day}.txt'
input_str = open(input_file).read().rstrip()
lines = input_str.split('\n')

p1 = 0
p2 = 0


def sum_of_numbers(str):
    sum = 0
    new_str = ''
    for c in str:
        new_str += c if c.isdigit() or c == '-' else ' '

    numbers = new_str.split()
    for number in numbers:
        sum += int(number)
    return sum


assert sum_of_numbers('[1,2,3]') == 6
assert sum_of_numbers('{"a":2,"b":4}') == 6
assert sum_of_numbers('[[[3]]]') == 3
assert sum_of_numbers('{"a":{"b":4},"c":-1}') == 3
assert sum_of_numbers('{"a":[-1,1]}') == 0
assert sum_of_numbers('[-1,{"a":1}]') == 0
assert sum_of_numbers('[]') == 0
assert sum_of_numbers('{}') == 0

for line in lines:
    p1 += sum_of_numbers(line)

# \{[^{}]+\:\"red\"[^{}]+\}
to_remove = re.compile(r"\{[^{}]+\:\"red\"[^{}]+\}")

for line in lines:
    p2 += sum_of_numbers(to_remove.sub('', line))

print(p1)
print(p2)
pass
