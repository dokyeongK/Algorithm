def solution(x):
    x_array = list(str(x))
    s = 0
    for i in x_array:
        s += int(i)
    if x % s == 0:
        return True
    else : return False