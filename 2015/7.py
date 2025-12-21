from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f'{day}.test.txt' if TEST else f'{day}.txt'
input_str = open(input_file).read().rstrip()
lines = input_str.split('\n')

p1 = 0
p2 = 0

unsolved = {}
solved = {}

for l in lines:
    line = l.split(' -> ')
    unsolved[line[1]] = line[0]


def solve(right):
    if right.isdigit():
        return int(right)

    exp = unsolved[right]
    if right in solved:
        pass
    elif exp.isdigit():
        solved[right] = int(exp)
    elif ' AND ' in exp:
        a, b = exp.split(' AND ')
        solved[right] = solve(a) & solve(b)
    elif ' OR ' in exp:
        a, b = exp.split(' OR ')
        solved[right] = solve(a) | solve(b)
    elif exp.startswith('NOT '):
        solved[right] = ~ solve(exp[4:])
    elif ' LSHIFT ' in exp:
        a, b = exp.split(' LSHIFT')
        solved[right] = solve(a) << int(b)
    elif ' RSHIFT ' in exp:
        a, b = exp.split(' RSHIFT')
        solved[right] = solve(a) >> int(b)
    else:
        solved[right] = solve(exp)

    if solved[right] < 0:
        solved[right] = solved[right] + 65536
    elif solved[right] > 65535:
        solved[right] = solved[right] - 65536

    return solved[right]


if TEST:
    assert solve('d') == 72
    assert solve('e') == 507
    assert solve('f') == 492
    assert solve('g') == 114
    assert solve('h') == 65412
    assert solve('i') == 65079
    assert solve('x') == 123
    assert solve('y') == 456
    exit(0)

p1 = solve('a')
print(p1)

solved = {
    'b': p1
}
p2 = solve('a')
print(p2)
pass
