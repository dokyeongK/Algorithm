def solution(n):
    answer = 0
    for idx in range(1, n+1):
        if n%idx == 0:
            answer += idx
    return answer