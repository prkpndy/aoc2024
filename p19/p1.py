with open('p19/input.txt', 'r') as file:
    data = file.read().splitlines()

T = data[0].split(", ")
P = data[2:]

DP = []

def isPossible(p, s):
    if s >= len(p):
        return True
    if DP[s] != -1:
        return DP[s]
    for t in T:
        e = s + len(t)
        if e<=len(p) and p[s:e]==t and isPossible(p, e):
            DP[s] = True
            break
    if DP[s] == True:
        return True
    else:
        DP[s] = False
        return False

count = 0
for p in P:
    DP = [-1 for _ in range(len(p))]
    if isPossible(p, 0):
        count += 1
    print(DP)

print(count)
