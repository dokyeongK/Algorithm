from collections import deque
#상 하 좌 우 좌상 좌하 우상 우하
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        now = queue.popleft()
        for i in range(8):
            next_x, next_y = now[0]+dx[i], now[1]+dy[i]
            if -1<next_y<w and -1<next_x<h:
                if board[next_x][next_y]==1 and visit[next_x][next_y]==0:
                    visit[next_x][next_y]=1
                    queue.append([next_x, next_y])
    return 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 : break
    board = [[0]*w for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    for i in range(h):
        temp = list(map(int, input().split()))
        board[i]=temp
    count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visit[i][j]==0:
                visit[i][j] = 1
                count += bfs(i, j)

    print(count)