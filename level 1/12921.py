def solution(n):
    n = n + 1
    prime_num = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime_num[i]:
            for j in range(i + i, n, i):
                prime_num[j] = False
    return len([i for i in range(2, n) if prime_num[i]])