import itertools
from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f'{day}.test.txt' if TEST else f'{day}.txt'
input_str = open(input_file).read().rstrip()
lines = input_str.split('\n')

p1 = 0
p2 = 0


def memory_len(line):
    if line.startswith('"'):
        line = line[1:]
    if line.endswith('"'):
        line = line[:-1]
    result = len(line.encode("utf-8").decode('unicode-escape'))
    return result


line_count = []
c = 0
for character in itertools.chain.from_iterable(open(input_file)):
    if character == '\n':
        line_count.append(c)
        c = 0
    else:
        c += 1

line_count2 = []
c = 0
for character in itertools.chain.from_iterable(open(input_file)):
    if character == '\n':
        line_count2.append(c + 2)
        c = 0
    else:
        c += 1
        if character in ['\\', '\"']:
            c += 1

i = 0
for l in lines:
    if not l:
        continue
    p1 += line_count[i] - memory_len(l)
    p2 += line_count2[i] - line_count[i]
    i += 1

if TEST:
    assert memory_len(lines[0]) == 0
    assert memory_len(lines[1]) == 3
    assert memory_len(lines[2]) == 7
    assert memory_len(lines[3]) == 1

    assert p1 == 12
    assert p2 == 19

print(p1)
print(p2)
pass
