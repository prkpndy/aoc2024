with open('p6/input.txt', 'r') as file:
    lines = file.read().splitlines()

max_len = 0
for line in lines:
    max_len = max(max_len, len(line))
for i in range(len(lines)):
    lines[i] = lines[i] + " "*(max_len - len(lines[i]))

def get_result(l, o):
    if o == "+":
        ans = 0
        for i in range(len(l)):
            ans += l[i]
    elif o == "*":
        ans = 1
        for i in range(len(l)):
            ans *= l[i]
    else:
        print(f"Invalid Operation {o}")
        return 0
    return ans

ans = 0
n = len(lines)-1

nums = []
j = len(lines[0]) - 1
while j >= 0:
    p = 1
    v = 0
    for i in range(n-1, -1, -1):
        if lines[i][j] != " ":
            v += int(lines[i][j]) * p
            p *= 10
    nums.append(v)
    if lines[-1][j] != " ":
        ans += get_result(nums, lines[-1][j])
        nums = []
        j -= 1
    j -= 1

print(f"ans = {ans}")
