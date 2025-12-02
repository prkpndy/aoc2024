with open('p1/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(v) for v in l.split()] for l in lines]

l1 = [n[0] for n in nums]
l2 = [n[1] for n in nums]
l2f = {}
for v in l2:
    if v in l2f:
        l2f[v] += 1
    else:
        l2f[v] = 1

ans = 0
for v in l1:
    if v in l2f:
        ans += l2f[v] * v

print(ans)