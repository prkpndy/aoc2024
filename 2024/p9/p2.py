with open('p9/input.txt', 'r') as file:
    data = file.read().splitlines()[0]

D = [int(d) for i, d in enumerate(data) if i%2 == 0] # Digits
B = [int(d) for i, d in enumerate(data) if i%2 == 1] # Blanks

A = [int(d) for d in data]

mState = [[] for _ in range(len(B)+len(D))]
fsMap = {k: [] for k in range(1, 10)}

for i in range(len(B)-1, -1, -1):
    if B[i] != 0:
        fsMap[B[i]].append(2*i + 1)
for i, v in enumerate(D):
    mState[2*i].append([v, i])

def findMin(v):
    x = len(B)
    r = -1
    for m in range(v, 10):
        if len(fsMap[m]) > 0 and fsMap[m][-1] < x:
            x = fsMap[m][-1]
            r = m
    return r, x

def push(l, v):
    if not l:
        return [v]
    for i in range(len(l)):
        if l[i] < v:
            l.insert(i, v)
            return l
    l.append(v)
    return l

def getSumOfBlanks(a, ind):
    r = 0
    for v in a:
        r += v[1]*(v[0]*ind + int(v[0]*(v[0]-1)/2))
        ind += v[0]
    return r

i = len(D)-1
while i >= 0:
    if D[i] != 0:
        k, j = findMin(D[i])
        if k != -1 and j < 2*i:
            fsMap[k].pop()
            y = k - D[i]
            mState[2*i] = []
            mState[j].append([D[i], i])
            D[i] = 0
            if y > 0:
                fsMap[y] = push(fsMap[y], j)
    i -= 1

ind, ans = 0, 0
for i, st in enumerate(mState):
    s  = getSumOfBlanks(st, ind)
    ind += A[i]
    ans += s
    i += 1

print(ans)