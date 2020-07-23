def solution(n, m):
    answer = []
    g, l = 0, 0
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m % i == 0 :
            g = i
    for j in range(max(n,m), (n*m)+1):
        if j%n == 0 and j%m == 0 :
            l = j
            break
    answer.append(g)
    answer.append(l)
    return answer