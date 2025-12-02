MIN = 0
MAX = 99
START = 50

NUM = MAX - MIN + 1

with open('p1/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[l[0], int(l[1:])] for l in lines]

def move_right(c, n):
    assert c >= MIN and c <= MAX
    assert n > 0

    a = n % NUM
    v = c + a

    if v > MAX:
        return v - MAX - 1
    else:
        return v


def move_left(c, n):
    assert c >= MIN and c <= MAX
    assert n > 0

    a = n % NUM
    v = c - a

    if v < MIN:
        return MAX + 1 + v
    else:
        return v

c = START
ans = 0
for d, n in nums:
    print(f"Moving {n} steps {d} from {c}")
    if d == "L":
        c = move_left(c, n)
    elif d == "R":
        c = move_right(c, n)
    else:
        print(f"Invalid direction {d}")
    print(f"to {c}")
    if c == 0:
        ans += 1

print(f"ans = {ans}")
