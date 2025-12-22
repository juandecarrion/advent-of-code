from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f'{day}.test.txt' if TEST else f'{day}.txt'
input_str = open(input_file).read().rstrip()
lines = input_str.split('\n')

p1 = 0
p2 = 0


def is_valid(password):
    first_cond = False
    for first, second, third in zip(password, password[1:], password[2:]):
        if ord(first) + 2 == ord(second) + 1 == ord(third):
            first_cond = True

    if 'i' in password or 'o' in password or 'l' in password:
        return False

    third_cond = 0
    for i, (first, second) in enumerate(zip(password, password[1:])):
        if first == second:
            for third, fourth in zip(password[i + 2:], password[i + 3:]):
                if third == fourth:
                    third_cond = True
                    break
            break

    return first_cond and third_cond


assert is_valid('hijklmmn') == False
assert is_valid('abbceffg') == False
assert is_valid('abbcegjk') == False
assert is_valid('abcdefhh') == False

assert is_valid('abcdffaa') == True
assert is_valid('ghjaabcc') == True

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def next_char(char):
    if char == 'z':
        return 'a'
    pos = ALPHABET.find(char)
    if pos == -1:
        raise ValueError('Invalid character')
    return ALPHABET[pos + 1]


def next_valid_password(password):
    as_list = list(password)
    while True:
        as_list[-1] = next_char(as_list[-1])
        if as_list[-1] == 'a':
            as_list[-2] = next_char(as_list[-2])
            if as_list[-2] == 'a':
                as_list[-3] = next_char(as_list[-3])
                if as_list[-3] == 'a':
                    as_list[-4] = next_char(as_list[-4])
                    if as_list[-4] == 'a':
                        as_list[-5] = next_char(as_list[-5])
                        if as_list[-5] == 'a':
                            as_list[-6] = next_char(as_list[-6])
                            if as_list[-6] == 'a':
                                as_list[-7] = next_char(as_list[-7])
        if is_valid(''.join(as_list)):
            break
    password = ''.join(as_list)
    return password


assert next_valid_password('abcdefgh') == 'abcdffaa'
assert next_valid_password('ghijklmn') == 'ghjaabcc'

p1 = next_valid_password(lines[0])
p2 = next_valid_password(p1)

print(p1)
print(p2)
pass
