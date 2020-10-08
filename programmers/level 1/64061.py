def solution(board, moves):
    answer = 0
    toy_bucket = [] # 잡은 장난감을 넣을 공간
    for mov in moves:
        for i in range(len(board)):
            if board[i][mov-1] > 0: # board에서 장난감을 꺼낼 수 있는 상황
                toy_idx = board[i][mov-1]
                board[i][mov-1]=0 # bucket으로 옮겼으므로 공란으로 만들어주기
                if len(toy_bucket)>0 and toy_bucket[-1]==toy_idx:
                    answer+=2
                    toy_bucket.pop()
                else:
                    toy_bucket.append(toy_idx)
                break # 하나의 mov에 대한 탐색이 끝났으므로 break
    return answer