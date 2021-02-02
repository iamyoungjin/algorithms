#위상 정렬 
'''
사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것을 의미한다
예시) 선수 과목을 고려한 학습 순서 설정 

-진입차수(indegree):특정한 노드로 들어오는 간선의 개수
-진출차수(Outdegree):특정한 노드에서 나가는 간선의 개수 

큐를 이용하는 위상 정렬 알고리즘의 동작 과정

1. 진입차수가 0인 모든 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정 반복
    1)큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
    2)새롭게 진입차수가 0이된 노드를 큐에 넣는다
-->결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다

위상정렬을 수행할 그래프는 사이클이 없는 방향 그래프(DAG)여야 한다
'''

#위상 정렬의 특징
#1. 위상 정렬은 DAG에 대해서만 수행할 수 있다
#2. 위상 정렬에서는 여러가지 답이 존재할 수 있다 (한 단계에서 큐에 새롭게 들어가는 원소가 2개이상인 경우)
#3. 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다(사이클에 포함된 원소 중 어떠한 원소도 큐에 들어갈 수 없다)
#4. 스택을 활용한 DFS를 이용해 위상정렬을 수행할 수도 있다

from collections import deque

v,e = map(int,input().split())
indegree=[0]*(v+1)
graph=[[]for i in range(v+1)]

for _ in range(e):
    a,b =map(int,input().split())
    indegree[b] +=1

def topology_sort():
    result=[]
    q = deque()
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now =q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i] ==0:
                q.append(i)
    for i in result:
        print(i,end=' ')
topology_sort()