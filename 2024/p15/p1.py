with open('p15/input.txt', 'r') as file:
    data = file.read().splitlines()

A = []
M = ""

def fillAM():
    global M
    i = 0
    while True:
        if len(data[i]) == 0:
            i += 1
            break
        A.append([c for c in data[i]])
        i += 1
    while i < len(data):
        M += data[i]
        i += 1

fillAM()

m = len(A)
n = len(A[0])

dirMap = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1]
}

def shift(i, j, d):
    while i>=0 and i<m and j>=0 and j<n:
        if A[i][j] == "O":
            i += d[0]
            j += d[1]
        elif A[i][j] == ".":
            return True, [i, j]
        else:
            return False, [i, j]

def calculateGPS():
    gps = 0
    for i in range(m):
        for j in range(n):
            if A[i][j] == "O":
                gps += 100*i + j
    return gps

def printState():
    for l in A:
        print(''.join(l))

pos = []
for i in range(m):
    for j in range(n):
        if A[i][j] == "@":
            pos = [i, j]
            break

for move in M:
    d = dirMap[move]
    i, j = pos
    ni, nj = i + d[0], j + d[1]
    if A[ni][nj] == "#":
        continue
    elif A[ni][nj] == ".":
        A[i][j] = "."
        A[ni][nj] = "@"
        pos = [ni, nj]
    else:
        isPossible, np = shift(ni, nj, d)
        if isPossible:
            A[np[0]][np[1]] = "O"
            A[ni][nj] = "@"
            A[i][j] = "."
            pos = [ni, nj]

print(calculateGPS())
