with open('p5/input.txt', 'r') as file:
    lines = file.read().splitlines()
    i = 0
    fresh_id_ranges = []
    available_ids = []
    while True:
        if len(lines[i]) == 0:
            break
        else:
            fresh_id_ranges.append([int(v) for v in lines[i].split("-")])
            i += 1
    i += 1
    while i < len(lines):
        available_ids.append(int(lines[i]))
        i += 1

fresh_id_ranges.sort(key=lambda r: r[0])

def is_fresh(id):
    for r in fresh_id_ranges:
        if r[0] <= id and id <= r[1]:
            return True
    return False

ans = 0
for id in available_ids:
    if is_fresh(id):
        ans += 1

print(f"ans = {ans}")
