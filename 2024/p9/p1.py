import math

def getThirdArray(D, B):
    A = [[] for _ in range(len(B))]
    i = len(D) - 1
    j = 0
    while j<=i:
        if D[i] > 0:
            if B[j] > 0:
                take = min(B[j], D[i])
                D[i] -= take
                B[j] -= take
                A[j].append([take, 2*i])
            else:
                j += 1
        else:
            i -= 1
    return A, D

def getSumOfDigits(M, i, ind):
    if i > len(M):
        return 0, i, ind
    if M[i] == 0:
        return 0, i+1, ind
    return i*(M[i]**2 - M[i] + 2*ind*M[i]), i+1, ind+M[i]

def getSum(v, f, i):
    return int(v*(f**2 + 2*i*f - f)/2)

def getSumOfBlanks(M, i, ind):
    if i > len(M):
        return 0, i, ind
    if len(M[i]) == 0:
        return 0, i+1, ind
    ans = 0
    for a in M[i]:
        ans += getSum(a[1], a[0], ind)
        ind += a[0]
    return ans, i+1, ind

with open('p9/input.txt', 'r') as file:
    A = file.read().splitlines()[0]

D = [int(d) for i, d in enumerate(A) if i%2 == 0]
B = [int(d) for i, d in enumerate(A) if i%2 == 1]

A, D = getThirdArray(D, B)

ind = 0
isA = False
i, j = 0, 0
ans = 0

while i<len(A) or j<len(D):
    if isA:
        isA = False
        a, i, ind = getSumOfBlanks(A, i, ind)
        ans += a
    else:
        isA = True
        a, j, ind = getSumOfDigits(D, j, ind)
        ans += a

print(int(ans/2))