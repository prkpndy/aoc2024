with open('p4/input.txt', 'r') as file:
    lines = file.read().splitlines()
    rolls = [list(l) for l in lines]

DIRS = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]

R = len(rolls)
C = len(rolls[0])

def num_adj_rolls(i, j):
    total_adj_rolls = 0
    for d in DIRS:
        ni = i + d[0]
        nj = j + d[1]
        if ni >= 0 and nj >= 0 and ni < R and nj < C and rolls[ni][nj] == "@":
            total_adj_rolls += 1
    return total_adj_rolls

ans = 0

removed = 0
while True:
    if removed == -1:
        removed = 0
    for i in range(R):
        for j in range(C):
            if rolls[i][j] == "@" and num_adj_rolls(i, j) < 4:
                removed += 1
                rolls[i][j] = "."
    if removed == 0:
        break
    ans += removed
    removed = 0

print(f"ans = {ans}")
