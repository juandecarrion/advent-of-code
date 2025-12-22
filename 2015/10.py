from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f'{day}.test.txt' if TEST else f'{day}.txt'
input_str = open(input_file).read().rstrip()
lines = input_str.split('\n')

p1 = 0
p2 = 0


def next_step(previous):
    current_digit = ''
    current_count = 0
    result = ''
    for c in previous:
        if c != current_digit:
            if current_count:
                result += str(current_count) + current_digit
            current_digit = c
            current_count = 1
        else:
            current_count += 1
    result += str(current_count) + current_digit
    return result


assert next_step('1') == '11'
assert next_step('11') == '21'
assert next_step('21') == '1211'
assert next_step('1211') == '111221'
assert next_step('111221') == '312211'

current_input = lines[0]
for i in range(40):
    current_input = next_step(current_input)

p1 = len(current_input)
for i in range(10):
    current_input = next_step(current_input)
p2 = len(current_input)

print(p1)
print(p2)
pass
