import os
import time

with open('p14/input.txt', 'r') as file:
    data = file.read().splitlines()

P = [[int(v) for v in l.split()[0].split("=")[1].split(",")] for l in data]
V = [[int(v) for v in l.split()[1].split("=")[1].split(",")] for l in data]

X = 101
Y = 103
T = 1000
D = 0.5


def get_matrix(t):
    A = [[" " for _ in range(X)] for _ in range(Y)]
    for i in range(len(P)):
        px = P[i][0] + V[i][0] * t
        py = P[i][1] + V[i][1] * t
        px %= X
        py %= Y
        A[py][px] = "."
    return A

def animate_console_matrix():
    for t in range(T):
        os.system('clear')
        matrix = get_matrix(t)
        print(f"t = {t}")
        # for i, row in enumerate(matrix):
        #     if i%2 == 0:
        #         print(''.join([c for i, c in enumerate(row) if i%2==0]))
        
        for i, row in enumerate(matrix):
            print(''.join(row))

        time.sleep(D)

animate_console_matrix()
