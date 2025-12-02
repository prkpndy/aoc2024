def isPossible(A, f, i, t):
    if i >= len(A):
        return f == t
    return isPossible(A, f+A[i], i+1, t) or isPossible(A, f*A[i], i+1, t)

with open('p7/input.txt', 'r') as file:
    lines = file.read().splitlines()
    data = [[int(expr[0]), [int(v) for v in expr[1].split()]] for expr in [line.split(":") for line in lines]]

ans = 0

for v in data:
    if isPossible(v[1], v[1][0], 1, v[0]):
        ans += v[0]

print(ans)