with open('p9/input.txt', 'r') as file:
    data = file.read().splitlines()[0]

D = [int(d) for i, d in enumerate(data) if i%2 == 0] # Digits
B = [int(d) for i, d in enumerate(data) if i%2 == 1] # Blanks

fsState = [[] for _ in range(len(B))]
fsMap = {k: [] for k in range(1, 10)}

for i in range(len(B)-1, -1, -1):
    if B[i] != 0:
        fsMap[B[i]].append(i)

def findMin(v):
    x = len(B)
    r = -1
    for m in range(v, 10):
        if len(fsMap[m]) > 0 and fsMap[m][-1] < x:
            x = fsMap[m][-1]
            r = m
    return r

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
    return r, ind

def getSumOfDigits(v, f, ind):
    return v*(f*ind + int(f*(f-1)/2)), ind+f

i = len(D)-1
while i >= 0:
    if D[i] != 0:
        x = findMin(D[i])
        if x != -1 and x < i:
            j = fsMap[x].pop()
            y = x - D[i]
            fsState[j].append([D[i], i])
            D[i] = 0
            if y > 0:
                fsMap[y] = push(fsMap[y], j)
    i -= 1

ind = 0
ans = 0
i = 0
while i < len(fsMap):
    s1, ind = getSumOfDigits(i, D[i], ind)
    s2, ind = getSumOfBlanks(fsState[i], ind)
    ans += s1 + s2
    i += 1

while i < len(D):
    s1, ind = getSumOfDigits(2*i, D[i], ind)
    ans += s1
    i += 1

print(ans)
