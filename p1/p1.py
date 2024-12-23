with open('p1/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(v) for v in l.split()] for l in lines]

l1 = [n[0] for n in nums]
l2 = [n[1] for n in nums]

l1.sort()
l2.sort()

ans = 0

for i in range(len(l1)):
    ans += abs(l1[i] - l2[i])

print(ans)