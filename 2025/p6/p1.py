with open('p6/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = []
    for i in range(len(lines)-1):
        nums.append([int(n) for n in lines[i].split()])
    ops = lines[-1].split()

def get_result(j, o):
    if o == "+":
        ans = 0
        for i in range(len(nums)):
            ans += nums[i][j]
    elif o == "*":
        ans = 1
        for i in range(len(nums)):
            ans *= nums[i][j]
    else:
        print(f"Invalid Operation {o}")
        return 0
    return ans

ans = 0
for j in range(len(nums[0])):
    ans += get_result(j, ops[j])

print(f"ans = {ans}")