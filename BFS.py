#BFS 너비 우선 탐색 : 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘
'''
BFS는 큐 자료구조를 이용하며 구체적인 동작 과정은 다음과 같다
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다
*노드 거리가 동일할때 최단거리에 자주쓰임
'''
from collections import deque

def bfs(graph, start, visited):
    
    queue = deque([start])
    visited[start] =  True #현재 노드 방문 처리
    while queue: #큐가 빌 때까지 
        v = queue.popleft() #큐 원소 하나 출력
        print(v,end=' ')
        for i in graph[v]: #방문하지 않은 인접한 원소 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited)