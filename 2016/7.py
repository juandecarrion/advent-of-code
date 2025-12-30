from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

"""
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""


def has_abba(ip_fragment):
    for i in range(1, len(ip_fragment) - 2):
        if (
            ip_fragment[i] == ip_fragment[i + 1]
            and ip_fragment[i - 1] == ip_fragment[i + 2]
            and ip_fragment[i - 1] != ip_fragment[i]
        ):
            return True
    return False


def support_tls(ip):
    ip = ip.replace("[", "]")
    i = 0
    outer_has_abba = False
    for fragment in ip.split("]"):
        if i % 2:
            if has_abba(fragment):
                return False
        else:
            if has_abba(fragment):
                outer_has_abba = True
        i += 1
    return outer_has_abba


def get_abas(ip_fragment):
    abas = []
    for i in range(1, len(ip_fragment) - 1):
        if (
            ip_fragment[i - 1] == ip_fragment[i + 1]
            and ip_fragment[i - 1] != ip_fragment[i]
        ):
            abas.append(ip_fragment[i - 1 : i + 2])
    return abas


def support_ssl(ip):
    ip = ip.replace("[", "]")
    i = 0
    abas = []
    babs = []
    for fragment in ip.split("]"):
        if i % 2:  # inner
            fragment_abas = get_abas(fragment)
            babs += fragment_abas
        else:  # outer
            fragment_abas = get_abas(fragment)
            abas += fragment_abas
        i += 1
    for aba in abas:
        for bab in babs:
            if aba[0] == bab[1] and aba[1] == bab[0]:
                return True
    return False


for line in lines:
    if support_tls(line):
        p1 += 1
    if support_ssl(line):
        p2 += 1
    if TEST:
        print(line, support_tls(line))
        print(line, support_ssl(line))

print(p1)
print(p2)
pass
