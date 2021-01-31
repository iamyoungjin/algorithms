import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) #무한을 의마하는 값으로 10억 설정

n,m = map(int, input().split()) #노드 간선의 갯수 입력 받기

start = int(input()) #시작 노드 번호 입력 

graph = [[] for i in range(n+1)] # 각 노드에 연결되어 이는 노드에 대한 정보를 담는 리스트 
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화 

# 모든 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())   #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))



def dijkstra(start):
    q=[] #우선순위큐
    heapq.heappush(q,(0,start))  #시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입
    distance[start]=0
    while q: #큐가 비어있지 않다면
        dist,now = heapq.heappop(q) #가장 최단 거리가 짧은 노드에 대한 정보꺼내기
        if distance[now]<dist: #현재 있는 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]: #현재 노드와 연결된 다른 인접한 노드 확인 
            cost = dist+i[1] 
            if cost < distance[i[0]]: #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0])) #값이 갱신 될때마다 우선순위 큐에 삽입

dijkstra(start) #다익스트라 알고리즘 수행

for i in range(1,n+1): 
    if distance[i]==INF: #도달할 수 없는 경우 무한 출력
        print("INFINITY")
    else: # 도달할 수 있는 경우 거리를 출력
        print(distance[i])