def solution(x, n):
    answer = []
    val = x
    for i in range(n):
        answer.append(val)
        val += x
    return answer