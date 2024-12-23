with open('p10/input.txt', 'r') as file:
    data = file.read().splitlines()

A = [[int(d) for d in l] for l in data]
m = len(A)
n = len(A[0])

count = [[[] for _ in range(n)] for _ in range(m)]
dyk = [[False for _ in range(n)] for _ in range(m)]

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def getId(i, j):
    return m*i + j

def getUnion(a, b):
    return list(set(a).union(b))

def getCount(i, j):
    if A[i][j] == 9:
        return [getId(i, j)]
    if dyk[i][j]:
        return count[i][j]
    v = A[i][j]
    c = []
    for dir in dirs:
        ni = i + dir[0]
        nj = j + dir[1]
        if ni<m and ni>=0 and nj<n and nj>=0 and A[ni][nj]==v+1:
            ids = getCount(ni, nj)
            c = getUnion(c, ids)
    count[i][j] = c
    # print(f"returning from ({i}, {j}, {v}) with count={c}")
    return c

ans = 0
for i in range(m):
    for j in range(n):
        if A[i][j] == 0:
            ids = getCount(i, j)
            ans += len(ids)

print(ans)
