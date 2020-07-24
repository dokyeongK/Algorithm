def solution(m, n, puddles):
    answer = 0
    home_maps = [[0]*(m+1) for _ in range(n+1)]
    home_maps[1][1] = 1
    for i in range(1, n+1):
        for j in range(1,  m+1):
            if i==1 and j == 1:
                continue
            if [j, i] in puddles:
                home_maps[i][j] = 0
            else:
                home_maps[i][j] += (home_maps[i-1][j]+home_maps[i][j-1])
    return (home_maps[-1][-1])%1000000007