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
    ans += n // NUM
    if d == "L":
        nc = move_left(c, n)
        if c != 0:
            if nc > c or nc == 0:
                ans += 1
        c = nc
    elif d == "R":
        nc = move_right(c, n)
        if nc < c:
            ans += 1
        c = nc
    else:
        print(f"Invalid direction {d}")

print(f"ans = {ans}")
