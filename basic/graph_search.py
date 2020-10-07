from collections import deque

def bfs(graph, root):
    visited_list = [] # 현재 탐색 한 노드들을 저장하는 리스트
    queue = deque([root]) # root인 1이 들어간 상태의 queue

    while queue:
        n = queue.popleft() # queue의 가장 왼쪽
        if n not in visited_list: # 방문하고자 하는 노드가 방문을 하지 않은 상태라면
            visited_list.append(n) # 방문 노드에 넣어주고
            queue += graph[n] - set(visited_list) # 그래프의 'n' 노드에 연결되어있어 앞으로 읽어야 할 노드를 추가합니다.

    return visited_list

def dfs(graph, root):
    visited_list = [] # 현재 탐색 한 노드들을 저장하는 리스트
    stack = [root] # root인 1이 들어간 상태의 stack

    while stack:
        n = stack.pop() # 가장 마지막에 담긴 노드 꺼내기
        if n not in visited_list: # 방문하고자 하는 노드가 방문을 하지 않은 상태라면
            visited_list.append(n) # 방문 노드에 넣고
            stack += graph[n] - set(visited_list) # 앞으로 읽어야 할 노드 추가.
    return visited_list

if __name__ == '__main__':
    search_graph = {
        1: set([2, 3, 4]),
        2: set([1, 5, 6]),
        3: set([1, 7]),
        4: set([1, 8]),
        5: set([2, 9]),
        6: set([2, 10]),
        7: set([3]),
        8: set([4]),
        9: set([5]),
        10: set([6]),
        }

    root_node = 1
    print(bfs(search_graph, root_node))
    print(dfs(search_graph, root_node))