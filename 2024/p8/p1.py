with open('p8/input.txt', 'r') as file:
    A = file.read().splitlines()

m = len(A)
n = len(A[0])
B = [[0 for _ in range(n)] for _ in range(m)]

ant = {}
for i in range(m):
    for j in range(n):
        if A[i][j] != ".":
            if A[i][j] in ant:
                ant[A[i][j]].append([i, j])
            else:
                ant[A[i][j]] = [[i, j]]

def markAntennas(a, b):
    # print(a, b, m, n)
    p1i, p1j = 2*b[0] - a[0], 2*b[1] - a[1]
    p2i, p2j = 2*a[0] - b[0], 2*a[1] - b[1]
    if p1i>=0 and p1j>=0 and p1i<m and p1j<n:
        B[p1i][p1j] = 1
    if p2i>=0 and p2j>=0 and p2i<m and p2j<n:
        B[p2i][p2j] = 1

for ants in ant.values():
    for i in range(len(ants)):
        for j in range(i+1, len(ants)):
            markAntennas(ants[i], ants[j])

print(sum([sum(v) for v in B]))