import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
stores = []
homes = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j]==1:homes.append([i, j])
        elif temp[j]==2:stores.append([i, j])

#뽑을 수 있는 치킨집들


def get_combination(chickin_stores, count):
    comb_list = [i for i in range(len(chickin_stores))]
    visit = [0 for _ in range(len(comb_list))]
    chickin_stores_comb = []

    def generate_comb(now_chosen):
        if len(now_chosen)==count:
            temp = []
            for k in range(len(now_chosen)):
                temp.append(chickin_stores[now_chosen[k]])
            chickin_stores_comb.append(temp)

        start = comb_list.index(now_chosen[-1])+1 if now_chosen else 0

        for next in range(start, len(comb_list)):
            if visit[next]==0 and (next==0 or comb_list[next-1]!=comb_list[next] or visit[next-1]):
                now_chosen.append(comb_list[next])
                visit[next]=1
                generate_comb(now_chosen)
                visit[next]=0
                now_chosen.pop()
    generate_comb([])

    return chickin_stores_comb


combination_list = get_combination(stores, M)#list(itertools.combinations(stores, M))


#하나의 집당 치킨거리 계산
def cal_distance(home, store_list):
    min_d = 1e9

    for k in range(len(store_list)):
        dist = abs(home[0]-store_list[k][0]) + abs(home[1]-store_list[k][1])
        min_d = min(min_d, dist)
    return min_d

chickin_distance = []

for i in range(len(combination_list)):
    dest_sum = 0
    for j in range(len(homes)):
        dest_sum += cal_distance(homes[j], combination_list[i])
    chickin_distance.append(dest_sum)

print(min(chickin_distance))