import sys
# not use itertools

person = int(input().split()[0])
team_member = person//2

s_map = [list(map(int, input().split())) for _ in range(person)]

temp_team= [0 for _ in range(person)] # 0, 0, 0, 0 -> 1, 1, 0, 0
ans = sys.maxsize

def dfs(idx, now_members):
    global ans
    if now_members==team_member:
        start, link = 0, 0
        for i in range(person):
            for j in range(person):
                if temp_team[i] and temp_team[j]:
                    start += s_map[i][j]
                elif not temp_team[i] and not temp_team[j]:
                    link += s_map[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, person):
        if temp_team[i]:continue
        else:
            temp_team[i]=1
            dfs(i+1, now_members+1)
            temp_team[i] = 0
dfs(0, 0)
print(ans)