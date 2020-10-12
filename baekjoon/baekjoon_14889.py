from itertools import combinations
person = int(input().split()[0])
team_member = person//2

s_map = [list(map(int, input().split())) for _ in range(person)]
res = -1

team_list = [i for i in range(person)]
for comb in combinations(team_list, team_member):
    start = comb
    link = list(set(team_list)-set(start))

    start_combination = combinations(start, 2)
    link_combination = combinations(link, 2)

    start_sum = 0
    for x, y in start_combination:
        start_sum+=s_map[x][y]+s_map[y][x]
    link_sum = 0
    for x, y in link_combination:
        link_sum += s_map[x][y]+s_map[y][x]

    if res == -1 :
        res = abs(start_sum-link_sum)
    else:
        res = min(res, abs(start_sum-link_sum))
print(res)

