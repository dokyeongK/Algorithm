from collections import deque

N = int(input().split()[0])
city = [[0]*N for _ in range(N)]

for i in range(N):
    temp = str(input().split()[0])
    for j in range(len(temp)):
        city[i][j] = int(temp[j])

dx = [0, 0 ,-1, 1]
dy = [-1, 1, 0, 0]

def bfs(pos):
    x, y = pos[0], pos[1]
    town_size = 1
    city[x][y] = -1
    queue = deque()
    queue.append([x,y])
    while queue:
        now = queue.popleft()
        for i in range(4):
            next_x, next_y = now[0] + dx[i], now[1] + dy[i]
            if -1<next_x<N and -1<next_y<N and city[next_x][next_y]==1:
                city[next_x][next_y] = -1
                town_size+=1
                queue.append([next_x, next_y])

    return 1, town_size

total_town = 0
city_town = []

for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            c, t = bfs([i, j])
            total_town += c
            city_town.append(t)
city_town.sort()
print(total_town)
if total_town == 0:
    print(0)
else:
    for i in range(len(city_town)):
        print(city_town[i])
