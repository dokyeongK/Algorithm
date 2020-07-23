def solution(s, n):
    answer = ''
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for idx in s:
        if idx == ' ': answer+=' '
        elif idx in low:
            answer += low[(low.index(idx)+n)%len(low)]
        elif idx in up:
            answer += up[(up.index(idx)+n)%len(up)]
    return answer