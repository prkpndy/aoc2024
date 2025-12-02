dirs = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
word = "XMAS"

def isXmas(A, x, y, dx, dy, m, n):
    for i in range(len(word)):
        nx = x + i*dx
        ny = y + i*dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            return 0
        elif A[nx][ny] != word[i]:
            return 0
    return 1


with open('p4/input.txt', 'r') as file:
    lines = file.read().splitlines()

m = len(lines)
n = len(lines[0])
ans = 0

for i in range(m):
    for j in range(n):
        if lines[i][j] == "X":
            for d in dirs:
                ans += isXmas(lines, i, j, d[0], d[1], m, n)

print(ans)