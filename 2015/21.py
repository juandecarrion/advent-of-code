import copy
import itertools
from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

boss_stats = {}
for line in lines:
    k, v = line.split(": ")
    boss_stats[k] = int(v)


shop = {}
for i in ["weapons", "armor", "rings"]:
    day = Path(__file__).stem
    input_file = f"{day}.{i}.txt"
    input_str = open(input_file).read().rstrip()
    lines = input_str.split("\n")
    lines.pop(0)
    shop[i] = []
    for j in range(len(lines)):
        values = lines[j].split()
        e = {
            "name": i + str(j),
            "cost": int(values[-3]),
            "damage": int(values[-2]),
            "armor": int(values[-1]),
        }
        e["roi"] = (e["damage"] + e["armor"]) / e["cost"]
        shop[i].append(e)


main_combinations = []
for a in [0, 1]:
    for r in [0, 1, 2]:
        main_combinations.append([1, a, r])


to_combine = []
for mc in main_combinations:
    new_comb = []
    for w in range(mc[0]):
        new_comb.append(shop["weapons"])
    for a in range(mc[1]):
        new_comb.append(shop["armor"])
    for r in range(mc[2]):
        new_comb.append(shop["rings"])
    to_combine.append(new_comb)
    pass

all_combinations = []
for comb in to_combine:
    new_combinations = list(itertools.product(*comb))
    all_combinations += new_combinations


unique_combinations = []
for comb in all_combinations:
    name_set = set()
    for i in comb:
        name_set.add(i["name"])
    if len(name_set) == len(comb):
        unique_combinations.append(comb)


def comb_cost(comb):
    return sum([x["cost"] for x in comb])


sorted_combinations = sorted(unique_combinations, key=comb_cost)


def calc_stats(comb):
    damage = 0
    armor = 0
    for i in comb:
        damage += i["damage"]
        armor += i["armor"]

    return {
        "Damage": damage,
        "Armor": armor,
        "Hit Points": 100,
    }


def player_wins(player, boss):
    player_turn = True
    while player["Hit Points"] > 0 and boss["Hit Points"] > 0:
        if player_turn:
            boss["Hit Points"] -= player["Damage"] - boss["Armor"]
            if TEST:
                print(f"The boss goes down to {boss['Hit Points']}")
        else:
            player["Hit Points"] -= boss["Damage"] - player["Armor"]
            if TEST:
                print(f"The player goes down to {player['Hit Points']}")
        player_turn = not player_turn
    return boss["Hit Points"] <= 0


if TEST:
    player_wins(
        {
            "Damage": 5,
            "Armor": 5,
            "Hit Points": 8,
        },
        {
            "Damage": 7,
            "Armor": 2,
            "Hit Points": 12,
        },
    )


for comb in sorted_combinations:
    player = calc_stats(comb)
    boss = copy.deepcopy(boss_stats)
    wins = player_wins(player, boss)
    if wins:
        p1 = comb_cost(comb)
        break
    if TEST:
        print(wins, comb_cost(comb), player, comb)


reversed_sorted_combinations = sorted_combinations.reverse()
for comb in sorted_combinations:
    player = calc_stats(comb)
    boss = copy.deepcopy(boss_stats)
    wins = player_wins(player, boss)
    if not wins:
        p2 = comb_cost(comb)
        break
    if TEST:
        print(wins, comb_cost(comb), player, comb)

print(p1)
print(p2)
pass
