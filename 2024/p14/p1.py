with open('p14/input.txt', 'r') as file:
    data = file.read().splitlines()

P = [[int(v) for v in l.split()[0].split("=")[1].split(",")] for l in data]
V = [[int(v) for v in l.split()[1].split("=")[1].split(",")] for l in data]

X = 101
Y = 103
T = 100

x = int(X/2)
y = int(Y/2)

v1, v2, v3, v4 = 0, 0, 0, 0

for i in range(len(P)):
    px = P[i][0] + V[i][0] * T
    py = P[i][1] + V[i][1] * T
    px %= X
    py %= Y
    # print(px, py)
    if px < x and py < y:
        v1 += 1
    elif py < y and px > x:
        v2 += 1
    elif py > y and px < x:
        v3 += 1
    elif py > y and px > x:
        v4 += 1

print(v1*v2*v3*v4)
