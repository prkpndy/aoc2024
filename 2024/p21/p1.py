with open('p21/input.txt', 'r') as file:
    data = file.read().splitlines()

CODES = data

NUMPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
MOVEPAD = [["", "^", "A"], ["<", "v", ">"]]

DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

NPSP = {}

def getMinPath(si, sj):
    l = [(si, sj)]
    cc = 0
    clc = len(l)
    nlc = 0

    minPaths = {}

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