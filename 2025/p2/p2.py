with open('p2/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(n) for n in r.split("-")] for r in lines[0].split(",")]

def is_repeating_at_least_twice(n, s):
    l = len(n)
    if l < 2*(s+1) or l % (s+1) != 0:
        return False
    t = l // (s+1)
    v = int(n[:(s+1)])
    for i in range(1, t):
        nv = int(n[((s+1)*i):(s+1)*(i+1)])
        if nv != v:
            return False
    return True

def is_invalid(n):
    n_str = str(n)
    l = len(n_str) // 2

    for i in range(l):
        if is_repeating_at_least_twice(n_str, i):
            return True

    return False

ans = 0
for l, r in nums:
    for i in range(l, r+1):
        if is_invalid(i):
            ans += i

print(f"ans = {ans}")