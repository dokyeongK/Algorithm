import sys
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# n, m = map(int, input().split())
n, m = map(int, input().strip().split())
input = sys.stdin.readline
board = []
virus_pos = []

for i in range(n):
    temp = list(map(int, input().strip().split()))
    board.append(temp)
    for j in range(len(temp)):
        if temp[j]==2:
            virus_pos.append([i, j])

def virus(a, b, virus_board):
    if virus_board[a][b]==2:
        for i in range(4):
            next_a, next_b = a + dx[i], b + dy[i]
            if -1 < next_a < n and -1 < next_b < m:
                if virus_board[next_a][next_b] == 0:
                    virus_board[next_a][next_b] = 2
                    virus(next_a, next_b, virus_board)

answer = 0

def wall_make(start, wall_num):
    global answer
    if wall_num == 3:
        now_board = copy.deepcopy(board)
        for num in range(len(virus_pos)):
            virus(virus_pos[num][0],virus_pos[num][1], now_board)
        count = sum(i.count(0) for i in now_board)
        answer = max(answer, count)
        return True
    else:
        for i in range(start, n * m):  # 2차원 배열에서 조합 구하기
            r = i // m
            c = i % m
            if board[r][c] == 0:  # 안전영역인 경우 벽으로 선택가능
                board[r][c] = 1  # 벽으로 변경
                wall_make(i, wall_num + 1)  # 벽선택
                board[r][c] = 0

wall_make(0, 0)
print(answer)
