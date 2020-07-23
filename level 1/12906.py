def solution(arr):
    answer = []
    answer.append(arr[0])
    for idx in arr:
        if idx != answer[-1]:
            answer.append(idx)
    return answer