with open('p2/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(n) for n in r.split("-")] for r in lines[0].split(",")]

def is_invalid(n):
    n_str = str(n)
    if len(n_str) % 2 != 0:
        return False
    l = int(len(n_str)/2)
    ln = int(n_str[0:l])
    rn = int(n_str[l:])

    return ln == rn

ans = 0
for l, r in nums:
    for i in range(l, r+1):
        if is_invalid(i):
            ans += i

print(f"ans = {ans}")