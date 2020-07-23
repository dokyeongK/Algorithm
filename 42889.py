def solution(N, stages):
    answer = {}
    users = len(stages)
    for i in range(1, N+1):
        if users != 0 :
            fail_user = stages.count(i)
            answer[i]= fail_user/users
            users -= fail_user
        else :
            answer[i] = 0

    return sorted(answer, key=lambda x : answer[x],reverse = True)