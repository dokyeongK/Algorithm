from collections import deque
test_num = int(input().split()[0])
dx = [-2, -1, 1, 2, -2, -1, 1 ,2]
dy = [-1, -2, -2, -1,1, 2, 2, 1]

def bfs(start, end):
    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]
    visit = [[0] * board for _ in range(board)]
    visit[start_x][start_y]=1
    queue = deque()
    queue.append([start, 0])

    while queue:
        now_start, now_move = queue.popleft()
        if now_start[0] == end_x and now_start[1] == end_y:
            return now_move

        for i in range(8):
            next_x, next_y = now_start[0]+dx[i], now_start[1]+dy[i]
            if -1<next_x<board and -1<next_y<board and visit[next_x][next_y]==0:
                    visit[next_x][next_y]=1
                    queue.append([[next_x, next_y], now_move+1])
    return 0
for _ in range(test_num):
    board = int(input().split()[0])
    depar = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    print(bfs(depar, dest))