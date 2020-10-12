from collections import deque
N = int(input().split()[0])

peopleA = ['R','G','B']
peopleB = ['R','B']

dx = [0,0,-1,1]
dy = [-1,1,0,0]

boardA = [['']*N for _ in range(N)]
boardB = [['']*N for _ in range(N)]

for i in range(N):
    temp = input().split()[0]
    for j in range(N):
        if temp[j]=='B':
            boardA[i][j]=temp[j]
        else:
            boardA[i][j] = temp[j]
            boardB[i][j] = 'R'

def bfs(start, board, visit):
    queue = deque()
    queue.append(start)

    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            next_x, next_y = now_x+dx[i], now_y+dy[i]
            if -1<next_x<N and -1<next_y<N:
                if board[now_x][now_y] == board[next_x][next_y] and visit[next_x][next_y]==0:
                    visit[next_x][next_y] = 1
                    queue.append([next_x,next_y])

    return 1

visitA = [[0]*N for _ in range(N)]
visitB = [[0]*N for _ in range(N)]

countA, countB = 0, 0

for i in range(N):
    for j in range(N):
        if visitA[i][j]==0:
            visitA[i][j] = 1
            countA += bfs([i, j], boardA, visitA)

for i in range(N):
    for j in range(N):
        if visitB[i][j]==0:
            visitB[i][j] = 1
            countB += bfs([i, j], boardB, visitB)
print(countA, countB)