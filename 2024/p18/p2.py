import sys
sys.setrecursionlimit(5000)

with open('p18/input.txt', 'r') as file:
    data = file.read().splitlines()

B = [[int(v) for v in l.split(",")] for l in data]

SM, SN = 71, 71
MAX_BITS = 1024

S = [["." for _ in range(SN)] for _ in range(SM)]

for c in range(MAX_BITS):
    S[B[c][1]][B[c][0]] = "#"

D = [[-1 for _ in range(SN)] for _ in range(SM)]  # -1 => don't know or not possible, other values => min steps to reach end(SM-1, SN-1)

dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def printMatrix(mat, s):
    for l in mat:
        print(s.join(["===" if v==-1 else "---" if v==-2 else str(v) + " "*(3 - len(str(v))) for v in l]))

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
                if ni<0 or nj<0 or ni>=SM or nj>=SN or S[ni][nj]=="#" or D[ni][nj]!=-1:
                    continue  # not possible or already sorted
                l.append((ni, nj))
                S[ni][nj] = "#"
                nlc += 1
        clc = nlc
        nlc = 0
        cc += 1

while MAX_BITS < len(B):
    S = [["." for _ in range(SN)] for _ in range(SM)]
    for c in range(MAX_BITS):
        S[B[c][1]][B[c][0]] = "#"
    D = [[-1 for _ in range(SN)] for _ in range(SM)]
    findCosts(SM-1, SN-1)
    if D[0][0] == -1:
        print(f"for B[{MAX_BITS}]={B[MAX_BITS]} it is not possible")
        # break
    else:
        print(f"for B[{MAX_BITS}]={B[MAX_BITS]} it is {D[0][0]}")
    MAX_BITS += 1
