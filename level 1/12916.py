def solution(s):
    p_num, y_num = 0, 0
    for idx in s:
        if idx.lower() == 'p':
            p_num +=1
        elif idx.lower() == 'y':
            y_num +=1
    if p_num != y_num:
        return False

    return True