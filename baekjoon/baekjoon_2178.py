import sys
from collections import deque

map_info = list(map(int, sys.stdin.readline().split()))

N, M = map_info[0], map_info[1]

map = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]
for i in range(N):
    temp = sys.stdin.readline().split()[0]
    for j in range(len(temp)):
        map[i][j] = int(temp[j])


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visit[start_x][start_y] = 1

    while queue:
        pos = queue.popleft()
        for i in range(4):
            next_x, next_y = pos[0] + dx[i], pos[1] + dy[i]

            if -1<next_x<N and -1<next_y<M and visit[next_x][next_y]==False and map[next_x][next_y] != 0:
                visit[next_x][next_y]= visit[pos[0]][pos[1]] +1
                queue.append([next_x, next_y])

    return visit[N-1][M-1]

print(bfs(0, 0))

