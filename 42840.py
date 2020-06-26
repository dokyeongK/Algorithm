def solution(answers):
    # 완전탐색
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct1, correct2, correct3 = 0, 0, 0

    answer = []

    for idx, right_value in enumerate(answers):
        if right_value == person1[idx % len(person1)]: correct1 += 1
        if right_value == person2[idx % len(person2)]: correct2 += 1
        if right_value == person3[idx % len(person3)]: correct3 += 1

    max_score = max(correct1, correct2)
    max_score = max(max_score, correct3)

    if max_score == correct1: answer.append(1)
    if max_score == correct2: answer.append(2)
    if max_score == correct3: answer.append(3)


    return answer