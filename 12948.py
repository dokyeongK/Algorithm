def solution(phone_number):
    answer = []
    for i in range(len(phone_number)):
        if (len(phone_number)-1)-i >=4:
            answer.append('*')
        else:
            answer.append(str(phone_number[i]))
    return ''.join(answer)