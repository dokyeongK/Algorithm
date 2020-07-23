def solution(numbers, hand):
    answer = []
    keypad = [[1,2,3], [4,5,6], [7,8,9], [-1, 0, -1]]
    L_x, L_y = 3, 0
    R_x, R_y = 3, 2
    for i in range(len(numbers)):
        for j in range(len(keypad)):
               if numbers[i] in keypad[j] :
                    if keypad[j].index(numbers[i]) == 0:
                        answer.append("L")
                        L_x, L_y = j, keypad[j].index(numbers[i])
                    elif keypad[j].index(numbers[i]) == 2:
                        answer.append("R")
                        R_x, R_y = j, keypad[j].index(numbers[i])
                    elif keypad[j].index(numbers[i]) == 1:
                        x, y = j, keypad[j].index(numbers[i])
                        distance_L = abs(L_x - x) + abs(L_y - y)
                        distance_R = abs(R_x - x) + abs(R_y - y)
                        if distance_L > distance_R:
                            R_x, R_y = x, y
                            answer.append("R")
                        elif distance_L<distance_R:
                            L_x, L_y = x, y
                            answer.append("L")
                        elif distance_L == distance_R:
                            if hand=='left' :
                                L_x, L_y = x,y
                                answer.append("L")
                            else:
                                R_x, R_y = x, y
                                answer.append("R")
    return ''.join(answer)