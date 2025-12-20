from pathlib import Path

day = Path(__file__).stem
input_file = f'{day}.txt'
input_str = open(input_file).read()
lines = input_str.split('\n')

p1 = 0
p2 = 0
for l in lines:
    if not l:
        continue
    
    a, b, c = [int(x) for x in l.split('x')]

    if a >= b and a >= c:
        p1 += b * c
        p2 += 2 * (b + c)
    elif b >= a and b >= c:
        p1 += a * c
        p2 += 2 * (a + c)
    else:
        p1 += a * b
        p2 += 2 * (a + b)

    p1 += 2 * (a * b + b * c + c * a)
    p2 += a * b * c

print(p1)
print(p2)
pass
