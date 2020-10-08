def solution(d, budget):
    num = 0
    use_budget = 0
    d.sort()
    for i in range(len(d)):
        use_budget += d[i]
        if use_budget == budget:
            num += 1
            break
        elif use_budget > budget:
            break
        elif use_budget < budget:
            num += 1
    return num     