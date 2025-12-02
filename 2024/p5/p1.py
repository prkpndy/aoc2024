import math

with open('p5/rules.txt', 'r') as file:
    rules = file.read().splitlines()
    rules = [[int(v) for v in r.split("|")] for r in rules]

with open('p5/updates.txt', 'r') as file:
    updates = file.read().splitlines()
    updates = [[int(v) for v in u.split(",")] for u in updates]

ans = 0

for u in updates:
    passAllRules = True
    for r in rules:
        i1 = -1
        i2 = -1
        for i, v in enumerate(u):
            if v == r[0]:
                if i1 == -1:
                    i1 = i
                else:
                    print("something is wrong")
            if v == r[1]:
                if i2 == -1:
                    i2 = i
                else:
                    print("something is wrong")
        if i1 != -1 and i2 != -1 and i1 > i2:
                passAllRules = False
                break
    if passAllRules:
        m = math.floor(len(u)/2)
        ans += u[m]

print(ans)