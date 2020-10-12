from collections import deque

height, width = map(int, input().split())
board = [[0]*width for _ in range(height)]
dx = [0,0,-1,1] #상하좌우
dy = [-1,1,0,0]

def bfs(pos):
    art_size = 1
    a, b = pos[0], pos[1]
    queue = deque()
    queue.append([a,b])
    board[a][b]=2
    while queue:
        now = queue.popleft()
        for i in range(4):
            next_x, next_y = now[0]+dx[i], now[1]+dy[i]
            if -1<next_x<height and -1<next_y<width : #5, 6
                if board[next_x][next_y]==1:
                    board[next_x][next_y] = 2
                    art_size+=1
                    queue.append([next_x, next_y])
    return 1, art_size


for i in range(height):
    temp = list(map(int, input().split()))
    board[i] = temp

art_count = 0
max_art = 0

for i in range(height):
    for j in range(width):
        if board[i][j]==1:
            c,a = bfs([i, j])
            art_count += c
            max_art = max(max_art, a)
print(art_count)
print(max_art)