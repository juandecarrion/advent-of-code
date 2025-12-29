import copy
import random
import sys
from pathlib import Path

TEST = False
print(f"{TEST=}")

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

MAGIC_MISSILE = "Magic Missile"
DRAIN = "Drain"
SHIELD = "Shield"
POISON = "Poison"
RECHARGE = "Recharge"

spells = {
    MAGIC_MISSILE: {
        "cost": 53,
        "damage": 4,
        "turns": 0,
    },
    DRAIN: {
        "cost": 73,
        "damage": 2,
        "heals": 2,
        "turns": 0,
    },
    SHIELD: {
        "cost": 113,
        "armor": 7,
        "turns": 6,
    },
    POISON: {
        "cost": 173,
        "damage": 3,
        "turns": 6,
    },
    RECHARGE: {
        "cost": 229,
        "mana": 101,
        "turns": 5,
    },
}


boss_stats = {}
for line in lines:
    k, v = line.split(": ")
    boss_stats[k] = int(v)


class Game:
    def __init__(
        self,
        boss,
        spell_combo,
        wizard_hit_points=None,
        wizard_mana=None,
        boss_hit_points=None,
        boss_damage=None,
        hard_mode=False,
    ):
        self.boss_hit_points = (
            boss["Hit Points"] if boss_hit_points is None else boss_hit_points
        )
        self.boss_damage = boss["Damage"] if boss_damage is None else boss_damage
        self.spell_combo = copy.deepcopy(spell_combo)
        self.wizard_hit_points = 50 if wizard_hit_points is None else wizard_hit_points
        self.wizard_mana = 500 if wizard_mana is None else wizard_mana
        self.wizard_armor = 0
        self.timer = {
            SHIELD: 0,
            POISON: 0,
            RECHARGE: 0,
        }
        self.wizard_turn = True
        self.used_mana = 0
        self.hard_mode = hard_mode

    def do_effects(self):
        self.wizard_armor = 7 if SHIELD in self.timer and self.timer[SHIELD] > 0 else 0

        if TEST:
            print(f"-- {'Player' if self.wizard_turn else 'Boss'} turn --")
            print(
                f"Player has {self.wizard_hit_points} hit points, {self.wizard_armor} armor, {self.wizard_mana} mana"
            )
            print(f"Boss has {self.boss_hit_points} hit points")

        for k, v in self.timer.items():
            if v > 0:
                spell = spells[k]
                if "damage" in spell:
                    damage_effect = spell["damage"]
                    self.boss_hit_points -= damage_effect
                    if TEST:
                        print(f"{k} deals {damage_effect} damage")
                if "heals" in spell:
                    heals_effect = spell["heals"]
                    self.wizard_hit_points += heals_effect
                if "mana" in spell:
                    mana_effect = spell["mana"]
                    self.wizard_mana += mana_effect

                self.timer[k] -= 1
                if TEST:
                    print(f"{k}'s timer is now {self.timer[k]}")

    def do_attack(self):
        if self.wizard_turn:
            spell_name = self.spell_combo.pop(0)
            spell = spells[spell_name]
            if spell["cost"] > self.wizard_mana:
                raise Exception("Insufficient mana")
            cost = spell["cost"]
            self.wizard_mana -= cost
            self.used_mana += cost
            if spell["turns"] == 0:
                if "damage" in spell and spell["damage"] > 0:
                    self.boss_hit_points -= spell["damage"]
                    if TEST:
                        print(f"{spell_name} deals {spell['damage']} damage")
                if "heals" in spell and spell["heals"] > 0:
                    self.wizard_hit_points += spell["heals"]
                    if TEST:
                        print(f"{spell_name} heals {spell['heals']} hit points")
            else:
                if self.timer[spell_name] > 0:
                    raise Exception("The previous effect was still active")
                self.timer[spell_name] = spell["turns"]
            if TEST:
                print(f"Player casts {spell_name}")
        else:
            self.wizard_hit_points -= self.boss_damage - self.wizard_armor

        self.wizard_turn = not self.wizard_turn

        if TEST:
            print()

    def is_wizard_winner(self):
        while self.wizard_hit_points > 0 and self.boss_hit_points > 0:
            if self.hard_mode and self.wizard_turn:
                self.wizard_hit_points -= 1
            if self.wizard_hit_points <= 0 or self.boss_hit_points <= 0:
                continue
            self.do_effects()
            if self.wizard_hit_points <= 0 or self.boss_hit_points <= 0:
                continue
            self.do_attack()
        return self.wizard_hit_points > 0


if TEST:
    combo1 = [POISON, MAGIC_MISSILE]
    combo2 = [RECHARGE, SHIELD, DRAIN, POISON, MAGIC_MISSILE]

    g1 = Game(
        boss_stats,
        combo1,
        wizard_hit_points=10,
        wizard_mana=250,
        boss_hit_points=13,
        boss_damage=8,
    )
    g2 = Game(
        boss_stats,
        combo2,
        wizard_hit_points=10,
        wizard_mana=250,
        boss_hit_points=14,
        boss_damage=8,
    )

    for g in [g1, g2]:
        result = g.is_wizard_winner()
        if TEST:
            print("True" if result else "False")
            print(f"Used Mana: {g.used_mana}")
            print()
            print("==================")
            print()


p1 = sys.maxsize
p2 = sys.maxsize
for hard_mode in [False, True]:
    spell_keys = list(spells.keys())
    for _ in range(2**12):
        combo = [POISON, RECHARGE, SHIELD]
        while len(combo) < 10:
            next_spell = random.choice(spell_keys)
            if spells[next_spell]["turns"] == 0 or next_spell not in combo[-2:]:
                combo.append(next_spell)
        g = Game(boss_stats, combo, hard_mode=hard_mode)
        try:
            if g.is_wizard_winner():
                if not hard_mode:
                    p1 = min(p1, g.used_mana)
                else:
                    p2 = min(p2, g.used_mana)
        except Exception as e:
            pass

    pass


print(p1)
print(p2)
pass
