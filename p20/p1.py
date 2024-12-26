with open('p20/input.txt', 'r') as file:
    data = file.read().splitlines()

T = [[v for v in l] for l in data]
M = len(T)
N = len(T[0])
S = 0
E = 0
SL = 0

D = [[-1 for _ in range(N)] for _ in range(M)]  # -1 => don't know or not possible, other values => min steps to reach end

dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def makeT(cheats):
    global T, D
    T = [[v for v in l] for l in data]
    D = [[-1 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            for c in cheats:
                if c[0] == i and c[1] == j:
                    T[i][j] = "."

def findPoint(point):
    for i in range(M):
        for j in range(N):
            if T[i][j] == point:
                return i, j

def findCosts(si, sj):
    l = [(si, sj)]
    cc = 0
    clc = len(l)
    nlc = 0

    while len(l) > 0:
        while clc > 0:
            clc -= 1
            i, j = l.pop(0)
            D[i][j] = cc
            for d in dirs:
                ni, nj = i+d[0], j+d[1]
                if ni<0 or nj<0 or ni>=M or nj>=N or T[ni][nj]=="#" or D[ni][nj]!=-1:
                    continue  # not possible or already sorted
                l.append((ni, nj))
                T[ni][nj] = "#"
                nlc += 1
        clc = nlc
        nlc = 0
        cc += 1

    return False if D[si][sj] == -1 else True, D[i][j]

saveMap = {}

def addInSaveMap(v):
    if v in saveMap:
        saveMap[v] += 1
    else:
        saveMap[v] = 1

def answer():
    global S, E
    S = findPoint("S")
    E = findPoint("E")

    _, oc = findCosts(S[0], S[1])

    ans = 0
    for i in range(M):
        for j in range(N):
            makeT([])
            if T[i][j] == "#":
                for d in dirs:
                    ni, nj = i+d[0], j+d[1]
                    if ni>=0 and nj>=0 and ni<M and nj<N:
                        makeT([[i, j], [ni, nj]])
                        isPossible, cost = findCosts(S[0], S[1])
                        if isPossible:
                            saved = cost - oc
                            if saved >= SL:
                                ans += 1
                                addInSaveMap(saved)
                        makeT([])
    print(ans)
    print(saveMap)

answer()
