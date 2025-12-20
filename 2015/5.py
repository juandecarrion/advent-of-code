from pathlib import Path

day = Path(__file__).stem
input_file = f'{day}.txt'
input_str = open(input_file).read()
lines = input_str.split('\n')

p1 = 0
p2 = 0


def is_nice(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    contains_pair = False
    contains_forbidden = False

    for i in range(len(line) - 1):
        c = line[i]

        if c in vowels:
            vowel_count += 1

        if line[i] == line[i + 1]:
            contains_pair = True

        if line[i:i + 2] in ['ab', 'cd', 'pq', 'xy']:
            contains_forbidden = True

    if line[-1:] in vowels:
        vowel_count += 1

    return vowel_count >= 3 and contains_pair and not contains_forbidden


assert is_nice('ugknbfddgicrmopn')
assert is_nice('aaa')
assert is_nice('jchzalrnumimnmhp') is False
assert is_nice('haegwjzuvuyypxyu') is False
assert is_nice('dvszwmarrgswjxmb') is False
assert is_nice('') is False


def is_nice2(line):
    repeated_pair = False
    sandwich = False

    for i in range(len(line) - 1):
        pair = line[i:i + 2]
        rest = line[i + 2:]
        if pair in rest:
            repeated_pair = True
        if i + 2 < len(line) and line[i] == line[i + 2]:
            sandwich = True

    return repeated_pair and sandwich


assert is_nice2('qjhvhtzxzqqjkmpb') is True
assert is_nice2('xxyxx') is True
assert is_nice2('uurcxstgmygtbstg') is False
assert is_nice2('ieodomkazucvgmuy') is False
assert is_nice2('qjhvdtaxzqqjkmpb') is False

for l in lines:
    if is_nice(l):
        p1 += 1
    if is_nice2(l):
        p2 += 1

print(p1)
print(p2)
pass
