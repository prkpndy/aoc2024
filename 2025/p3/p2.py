with open('p3/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [str(n) for n in lines]

# get the largest digit in s[f:t+1]
def get_largest_digit_index(s, f, t):
    ni = f
    n = int(s[f])
    for i in range(f, t+1):
        if int(s[i]) > n:
            ni = i
            n = int(s[i])
    return ni

LEN = 12
ans = 0
for num in nums:
    l = len(num)
    assert l >= LEN

    joltage = 0

    f = 0
    for i in range(LEN):
        ni = get_largest_digit_index(num, f, l - LEN + i)
        f = ni + 1
        v = int(num[ni])
        joltage += v*(10**(LEN - 1 - i))

    ans += joltage

print(f"ans = {ans}")
