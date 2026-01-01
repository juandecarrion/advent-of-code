from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")

p1 = 0
p2 = 0

container = {
    "bot": {},
    "output": {},
}

# Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.

"""
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""


compares = {}

for line in lines:
    split_line = line.split(" ")
    if split_line[0] == "value":
        value = int(split_line[1])
        bot = int(split_line[5])
        if bot in container["bot"]:
            container["bot"][bot].append(value)
        else:
            container["bot"][bot] = [value]

instructions = {}
for line in lines:
    split_line = line.split(" ")
    if split_line[0] == "bot":
        from_bot = int(split_line[1])
        low_type = split_line[5]
        low_index = int(split_line[6])
        high_type = split_line[10]
        high_index = int(split_line[11])

        if from_bot in instructions:
            raise Exception("It shouldn't happen")
        instructions[from_bot] = {
            "low": {
                "type": split_line[5],
                "index": int(split_line[6]),
            },
            "high": {
                "type": split_line[10],
                "index": int(split_line[11]),
            },
        }


while True:
    from_bot = None
    for k, v in container["bot"].items():
        if len(v) == 2:
            from_bot = k
            break
    if from_bot is None:
        break
    from_values = container["bot"][from_bot]
    instruction = instructions[from_bot]

    from_values = container["bot"][from_bot]
    from_values = sorted(from_values)
    values = {
        "low": from_values.pop(0),
        "high": from_values.pop(-1),
    }
    container["bot"][from_bot] = from_values

    for k, v in instruction.items():
        if v["index"] in container[v["type"]]:
            container[v["type"]][v["index"]].append(values[k])
        else:
            container[v["type"]][v["index"]] = [values[k]]

    compares[(values["high"], values["low"])] = from_bot


p1 = compares[(61, 17)]

product = container["output"][0] + container["output"][1] + container["output"][2]
p2 = 1
for i in product:
    p2 *= i

print(p1)
print(p2)
pass
