with open('p6/input.txt', 'r') as file:
    path = file.read().splitlines()

def findFirstObstacle(A, B, m, n, i, j, di, dj):
    while i>=0 and j>=0 and i<m and j<n:
        if A[i][j] == "#":
            return False, i-di, j-dj
        else:
            B[i][j] = 1
            i += di
            j += dj
    return True, -1, -1  # => out from arena

def getNewDirection(di, dj):
    if di==-1 and dj==0:
        return 0, 1
    if di==0 and dj==1:
        return 1, 0
    if di==1 and dj==0:
        return 0, -1
    if di==0 and dj==-1:
        return -1, 0
    raise Exception("something is wrong in getNewDirection function")

m = len(path)
n = len(path[0])
si, sj = 0, 0
sdi, sdj = -1, 0
B = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if path[i][j] == "^":
            si, sj = i, j
            B[i][j] = 1

isOut, ni, nj = findFirstObstacle(path, B, m, n, si, sj, sdi, sdj)
ndi, ndj = getNewDirection(sdi, sdj)

while not isOut:
    isOut, ni, nj = findFirstObstacle(path, B, m, n, ni, nj, ndi, ndj)
    ndi, ndj = getNewDirection(ndi, ndj)

print(sum([sum(l) for l in B]))