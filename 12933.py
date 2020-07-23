def solution(n):
    answer = 0
    num_list = sorted(list(str(n)), reverse=True)
    return int(''.join(num_list))