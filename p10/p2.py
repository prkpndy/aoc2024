with open('p10/input.txt', 'r') as file:
    data = file.read().splitlines()

A = [[int(d) for d in l] for l in data]
m = len(A)
n = len(A[0])

count = [[-1 for _ in range(n)] for _ in range(m)]

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def getCount(i, j):
    if A[i][j] == 9:
        return 1
    if count[i][j] != -1:
        return count[i][j]
    v = A[i][j]
    c = 0
    for dir in dirs:
        ni = i + dir[0]
        nj = j + dir[1]
        if ni<m and ni>=0 and nj<n and nj>=0 and A[ni][nj]==v+1:
            c += getCount(ni, nj)
    count[i][j] = c
    # print(f"returning from ({i}, {j}, {v}) with count={c}")
    return c

ans = 0
for i in range(m):
    for j in range(n):
        if A[i][j] == 0:
            ans += getCount(i, j)

print(ans)