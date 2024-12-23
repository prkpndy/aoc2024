dirs = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
word = "XMAS"

def isMas(A, x, y):
    return 1 if ((A[x-1][y-1] == "M" and A[x+1][y+1] == "S") or (A[x-1][y-1] == "S" and A[x+1][y+1] == "M")) and ((A[x-1][y+1] == "M" and A[x+1][y-1] == "S") or (A[x-1][y+1] == "S" and A[x+1][y-1] == "M")) else 0

with open('p4/input.txt', 'r') as file:
    lines = file.read().splitlines()

m = len(lines)
n = len(lines[0])
ans = 0

for i in range(1, m-1):
    for j in range(1, n-1):
        if lines[i][j] == "A":
            ans += isMas(lines, i, j)

print(ans)