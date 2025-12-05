with open('p5/input.txt', 'r') as file:
    lines = file.read().splitlines()
    i = 0
    fresh_id_ranges = []
    while True:
        if len(lines[i]) == 0:
            break
        else:
            fresh_id_ranges.append([int(v) for v in lines[i].split("-")])
            i += 1

fresh_id_ranges.sort(key=lambda r: r[0])
fresh_id_ranges_comb = [fresh_id_ranges[0]]
for i in range(1, len(fresh_id_ranges)):
    if fresh_id_ranges_comb[-1][1] >= fresh_id_ranges[i][0]:
        end = max(fresh_id_ranges_comb[-1][1], fresh_id_ranges[i][1])
        fresh_id_ranges_comb[-1][1] = end
    else:
        fresh_id_ranges_comb.append(fresh_id_ranges[i])

ans = 0
for r in fresh_id_ranges_comb:
    ans += r[1] - r[0] + 1

print(f"ans = {ans}")
