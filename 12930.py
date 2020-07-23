def solution(s):
    answer = []
    s = s.split(' ')
    for word in s:
        new_word = ''
        for j in range(len(word)):
            if j % 2 == 0 :
                new_word+=word[j].upper()
            else :
                new_word+=word[j].lower()
        answer.append(new_word)
    return ' '.join(answer)