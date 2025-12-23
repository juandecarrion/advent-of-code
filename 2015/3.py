from pathlib import Path

day = Path(__file__).stem
input_file = f"{day}.txt"
input_str = open(input_file).read()
lines = input_str.split("\n")

p1 = 0
p2 = 0
houses = {}
p2_houses = {}

loc = (0, 0)
santa_loc = (0, 0)
robo_loc = (0, 0)

houses[loc] = 1
p2_houses[santa_loc] = 2

santa_turn = True
for c in input_str:
    if c == "^":
        loc = (loc[0] + 1, loc[1])
        if santa_turn:
            santa_loc = (santa_loc[0] + 1, santa_loc[1])
        else:
            robo_loc = (robo_loc[0] + 1, robo_loc[1])
    elif c == "v":
        loc = (loc[0] - 1, loc[1])
        if santa_turn:
            santa_loc = (santa_loc[0] - 1, santa_loc[1])
        else:
            robo_loc = (robo_loc[0] - 1, robo_loc[1])
    elif c == ">":
        loc = (loc[0], loc[1] + 1)
        if santa_turn:
            santa_loc = (santa_loc[0], santa_loc[1] + 1)
        else:
            robo_loc = (robo_loc[0], robo_loc[1] + 1)
    else:
        loc = (loc[0], loc[1] - 1)
        if santa_turn:
            santa_loc = (santa_loc[0], santa_loc[1] - 1)
        else:
            robo_loc = (robo_loc[0], robo_loc[1] - 1)
    if loc in houses:
        houses[loc] += 1
    else:
        houses[loc] = 1
    if santa_turn:
        if santa_loc in p2_houses:
            p2_houses[santa_loc] += 1
        else:
            p2_houses[santa_loc] = 1
    else:
        if robo_loc in p2_houses:
            p2_houses[robo_loc] += 1
        else:
            p2_houses[robo_loc] = 1
    santa_turn = not santa_turn

print(len(houses.keys()))
print(len(p2_houses.keys()))

pass
