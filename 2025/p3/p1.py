with open('p3/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [str(n) for n in lines]

ans = 0
for num in nums:
    l = len(num)
    fi = 0
    f = int(num[0])
    for i in range(1, l-1):
        if int(num[i]) > f:
            f = int(num[i])
            fi = i
    s = int(num[fi+1])
    for i in range(fi+2, l):
        if int(num[i]) > s:
            s = int(num[i])
    ans += 10*f + s

print(f"ans = {ans}")
