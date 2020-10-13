# N : size, M: 물고기 수, Shark_size = 2
# 조건
# > 상하좌우 이동 가능
# > 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음
# > 자신의 크기보다 작은 물고기만 먹을 수 있음.

# 이동 조건
# 도움 요청 : 더 이상 먹을 수 있는 물고기가 공간에 없다.
# 먹을 수 있는 물고기 1 : 먹으러 간다.
# 먹을 수 있는 물고기 > 1 : 거리가 가장 가까운 물고기 (거리 : 지나야하는 칸의 개수)
# 거리가 가까운 물고기가 많다 => 가장 위에 있는 물고기 => 가장 왼쪽에 있는 물고기

# 상어는 1초에 1칸 이동.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가.
# EX ) 크기 2인 아기상어가 물고기 2마리 먹으면 크기 3 됨.

# Step 1 . 정보 입력받기
from collections import deque

n = int(input().split()[0])

fish_map = [list(map(int, input().split())) for _ in range(n)]
fish_list = [[[0, 0, 0,0]]*n for _ in range(n)] # [물고기좌표, 물고기좌표, 물고기크기, 먹기까지 걸린 시간]
shark = [] # [상어좌표, 상어좌표]
shark_size = 2

for i in range(n):
    for j in range(n):
        if fish_map[i][j]==9:
            shark=[i,j]

# Step 2. 먹을 수 있는 물고기가 있는지 확인.
# -----
# shark_pos에서부터 시작해서 상하좌우 살피면서 먹을 수 있는 물고기 확인
# 못지나가는 조건 : 자기의 사이즈보다 크다면.
# 먹을 물고기 선택
# -----

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def eating_time():
    global shark
    global shark_size
    global fish_list
    global eating_count
    visit = [[0] * n for _ in range(n)]

    shark_x, shark_y = shark[0], shark[1]
    visit[shark_x][shark_y]=1

    queue = deque()
    queue.append([shark_x, shark_y, 0])
    can_eating = [] #[물고기 좌표, 물고기 좌표, 크기, 거리]

    while queue:
        now = queue.popleft()
        for i in range(4):
            nx,ny = now[0]+dx[i], now[1]+dy[i]
            if -1<nx<n and -1<ny<n and visit[nx][ny]==0:
                if fish_map[nx][ny]==0 or fish_map[nx][ny]==shark_size:
                    visit[nx][ny]= now[2]+1
                    queue.append([nx, ny, now[2]+1])
                elif fish_map[nx][ny]<shark_size: #먹을 수 있는 물고기
                    visit[nx][ny]= now[2]+1 #[물고기좌표, 물고기좌표, 물고기크기, 먹기까지 걸린 시간] -> 최소 visit 시간 넣어줘야함.
                    can_eating.append([nx, ny, fish_map[nx][ny], now[2]+1])
                    queue.append([nx, ny, now[2]+1])

    if can_eating:
        can_eating = sorted(can_eating, key=lambda x:(x[0], x[1])) #[물고기좌표, 물고기좌표, 물고기크기, 먹기까지 걸린 시간]
    fish = []
    # # 먹을 물고기 정하기
    if len(can_eating)==0:
        return 0
    elif len(can_eating) == 1:
        fish = can_eating[0]  # fish의 x, y
    else:
        min_distance = can_eating[0][3]
        for k in range(1, len(can_eating)):
            min_distance = min(min_distance, can_eating[k][3])

        fishes = []

        for k in range(len(can_eating)):
            if can_eating[k][3]==min_distance:
                fishes.append(can_eating[k])

        fish = fishes[0]

    # eating fish -> fish를 먹고, 해당 위치로 shark pos 변경, 똑같은거 계속 해주면 됨.
    if fish:

        fish_map[fish[0]][fish[1]] = 9
        fish_map[shark_x][shark_y] = 0
        shark = [fish[0], fish[1]]

        return visit[fish[0]][fish[1]]


# -1이 return : 먹을 물고기가 없음.
# 먹었음? return 먹은 시간, 새 x,y좌표
result = 1
time = 0
eating_count = 0

while(result!=0):
    result = eating_time()
    time+=result
    if result!=0:
        eating_count+=1
        if eating_count==shark_size:
            shark_size +=1
            eating_count = 0
print(time)
