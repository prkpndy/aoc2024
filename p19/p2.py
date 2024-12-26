with open('p19/input.txt', 'r') as file:
    data = file.read().splitlines()

T = data[0].split(", ")
P = data[2:]

DP = []

def getPossibleWays(p, s):
    if s == len(p):
        return 1
    if DP[s] != -1:
        return DP[s]
    n = 0
    for t in T:
        e = s + len(t)
        if e<=len(p) and p[s:e]==t:
            n += getPossibleWays(p, e)
    DP[s] = n
    return n

count = 0
for p in P:
    DP = [-1 for _ in range(len(p))]
    c = getPossibleWays(p, 0)
    print(f"{p} can be made in {c} ways")
    count += c

print(count)
