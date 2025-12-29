from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0


def solve(a=0):
    register = {
        "a": a,
        "b": 0,
    }

    i = 0
    offset = 1
    while i < len(lines):
        line = lines[i]
        split_str = line.split(maxsplit=1)
        instruction = split_str[0]
        r = split_str[1]
        if "," in r:
            r, offset = r.split(", ")
            offset = int(offset) - 1
        if instruction == "jmp":
            offset = int(split_str[1]) - 1
        match instruction:
            case "hlf":
                register[r] //= 2
            case "tpl":
                register[r] *= 3
            case "inc":
                register[r] += 1
            case "jmp":
                i += offset
            case "jie":
                if (register[r] % 2) == 0:
                    i += offset
            case "jio":
                if register[r] == 1:
                    i += offset
            case _:
                raise NotImplementedError()
        i += 1

    return register


register = solve()
if TEST:
    assert register["a"] == 2


p1 = register["b"]

register = solve(a=1)
p2 = register["b"]

print(p1)
print(p2)
pass
