with open('p11/input.txt', 'r') as file:
    data = file.read().splitlines()[0]

A = [int(v) for v in data.split()]

def splitEvenDigits(v):
    s = str(v)
    n = len(s)
    m = int(n/2)
    l = s[0:m]
    r = s[m:n]
    return int(l), int(r)

BLINK = 75

for b in range(BLINK):
    nA = []
    for i in range(len(A)):
        if A[i] == 0:
            nA.append(1)
        elif len(str(A[i]))%2 == 0:
            n1, n2 = splitEvenDigits(A[i])
            nA.append(n1)
            nA.append(n2)
        else:
            nA.append(2024*A[i])
    A = nA

print(len(A))