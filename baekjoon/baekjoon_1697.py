from collections import deque

n, k = map(int, input().split())
max_length = 100001
visit=[0]*max_length

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        now = queue.popleft()
        if now == k:
            return visit[now]

        back = now-1
        front = now+1
        jump = now*2
        if -1<back and back<max_length and (visit[back]==0 or visit[now]+1<visit[back]):
            visit[back]=visit[now]+1
            queue.append(back)
        if -1<front and front<max_length and (visit[front]==0 or visit[now]+1<visit[front]):
            visit[front]=visit[now]+1
            queue.append(front)
        if -1<jump and jump<max_length and (visit[jump]==0 or visit[now]+1<visit[jump]):
            visit[jump]=visit[now]+1
            queue.append(jump)
    return 0

print(bfs(n))

