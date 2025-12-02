with open('p16/input.txt', 'r') as file:
    A = file.read().splitlines()

m = len(A)
n = len(A[0])

FC = 1
TC = 1000

DP = [[{"n":-2, "e":-2, "s":-2, "w":-2, "v": False} for _ in range(n)] for _ in range(m)]

dirs = {
    "n": [-1, 0],
    "e": [0, 1],
    "s": [1, 0],
    "w": [0, -1]
}

movements = {
    "n": ["e", "w"],
    "e": ["n", "s"],
    "s": ["w", "e"],
    "w": ["s", "n"]
}

def canMove(i, j):
    return i>=0 and i<m and j>=0 and j<n and A[i][j] != "#" and not DP[i][j]["v"]

def makeMove(i, j, d, possibleCosts, pc):
    ni, nj = i+dirs[d][0], j+dirs[d][1]
    if canMove(ni, nj):
        cost = traverse(ni, nj, d)
        if cost != -1:
            cost += pc
            possibleCosts.append(cost)
        DP[i][j][d] = cost
    else:
        DP[i][j][d] = -1

# this function will return the minimum cost to reach end from (i, j) with d direction
def traverse(i, j, d):
    if A[i][j] == "E":
        return 0
    if DP[i][j][d] != -2:
        return DP[i][j][d]

    DP[i][j]["v"] = True

    possibleCosts = []

    # continuing in the same direction
    makeMove(i, j, d, possibleCosts, FC)

    # trying in other two possible directions
    for move in movements[d]:
        makeMove(i, j, move, possibleCosts, FC+TC)

    DP[i][j]["v"] = False

    if len(possibleCosts) == 0:
        return -1
    else:
        return min(possibleCosts)

si, sj = m-2, 1
print(min(traverse(si, sj, "e"), TC + traverse(si, sj, "n")))
print(DP)