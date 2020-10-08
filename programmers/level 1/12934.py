import math
def solution(n):
    if math.sqrt(n)%1 == 0 :
        return pow(int(math.sqrt(n)) + 1, 2)
    else : return -1