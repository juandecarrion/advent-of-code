from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

REAL_SUE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


class Sue:
    def __init__(self, id, props):
        self.id = id
        self.props = {}
        for k in REAL_SUE.keys():
            self.props[k] = props[k] if k in props else None

    def is_real_sue(self):
        for k, v in self.props.items():
            if v is not None:
                if REAL_SUE[k] != v:
                    return False
        return True

    def is_real_sue2(self):
        for k, v in self.props.items():
            if v is not None:
                if k in ["cats", "trees"]:
                    if REAL_SUE[k] > v:
                        return False
                elif k in ["pomeranians", "goldfish"]:
                    if REAL_SUE[k] < v:
                        return False
                else:
                    if REAL_SUE[k] != v:
                        return False
        return True


for line in lines:
    id_str, prop_str = line.split(": ", 1)
    _, id = id_str.split(" ")
    props = {}
    for prop in prop_str.split(", "):
        k, v = prop.split(": ")
        props[k] = int(v)
    sue = Sue(id, props)
    if sue.is_real_sue():
        p1 = sue.id
    if sue.is_real_sue2():
        p2 = sue.id

print(p1)
print(p2)
pass
