from pathlib import Path

TEST = False

day = Path(__file__).stem
input_file = f"{day}.test.txt" if TEST else f"{day}.txt"
input_str = open(input_file).read().rstrip()
lines = input_str.split("\n")


p1 = 0
p2 = 0

RACE_DURATION = 1000 if TEST else 2503


class Deer:
    def __init__(self, name: str, speed, speed_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.speed_duration = speed_duration
        self.rest_duration = rest_duration

        self.position = 0
        self.points = 0
        self.state = "running"
        self.remaining_speed = speed_duration
        self.remaining_rest = rest_duration

    def next_step(self):
        if self.state == "running":
            self.position += self.speed
            self.remaining_speed -= 1
            if self.remaining_speed == 0:
                self.state = "resting"
                self.remaining_rest = self.rest_duration
        else:
            self.remaining_rest -= 1
            if self.remaining_rest == 0:
                self.state = "running"
                self.remaining_speed = self.speed_duration


deers = []
for line in lines:
    words = line.split()
    name = words[0]
    speed = int(words[3])
    speed_duration = int(words[6])
    rest_duration = int(words[13])
    deers.append(Deer(name, speed, speed_duration, rest_duration))


for i in range(RACE_DURATION):
    for deer in deers:
        deer.next_step()
    best_position = 0
    for deer in deers:
        best_position = max(best_position, deer.position)
    for deer in deers:
        if deer.position == best_position:
            deer.points += 1


for deer in deers:
    p1 = max(p1, deer.position)
    p2 = max(p2, deer.points)

print(p1)
print(p2)
pass
