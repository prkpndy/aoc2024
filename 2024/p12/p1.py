with open('p12/input.txt', 'r') as file:
    data = file.read().splitlines()

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

A = [[c for c in l] for l in data]
m = len(A)
n = len(A[0])
visited = [[False for _ in range(n)] for _ in range(m)]

def traverse(i, j, c):
    a = 1
    p = 0
    visited[i][j] = True
    for dir in dirs:
        ni = i + dir[0]
        nj = j + dir[1]
        if ni<m and ni>=0 and nj<n and nj>=0:
            if A[ni][nj] == c:
                if not visited[ni][nj]:
                    na, np = traverse(ni, nj, c)
                    a += na
                    p += np
            else:
                p += 1
        else:
            p += 1
    return a, p

ans = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            # c = A[i][j]
            a, p = traverse(i, j, A[i][j])
            # print(f"cost of region growing {c} starting at ({i}, {j}) is {a} * {p} = {a*p}")
            ans += a*p

print(ans)