def solution(n, lost, reserve):
    only_reserve = []
    only_lost = []
    for i in range(len(reserve)):
        if reserve[i] not in lost: only_reserve.append(reserve[i])
    for j in range(len(lost)):
        if lost[j] not in reserve: only_lost.append(lost[j])
    for k in range(len(only_reserve)):
        front = only_reserve[k] - 1
        back = only_reserve[k] + 1
        if front in only_lost: only_lost.remove(front)
        elif back in only_lost: only_lost.remove(back)
    answer = n - len(only_lost)
    return answer