#https://www.acmicpc.net/problem/18352
#특정 거리의 도시 찾기
'''
1번부터 N번 까지의 도시와 M개의 단방향 도로가 존재하고, 모든 도로의 거리는 1
X로부터 출발하여 도착할 수 있는 모든 도시중에 최단 거리가 K인 모든 도시 출력
'''

#풀이 
#1. 각 도시가 단방향으로 연결되어 있어, 노드 연결 상태를 배열에 저장하고 BFS로 최단거리 구하기
#2. 마지막에 최단 거리와 K가 같은 노드만 따로 정답 배열에 저장하여 정렬 후 출력 
#주의 input.split()으로 진행시 입력이 많기 때문에 시간 초과가 난다 -> sys.stdin.readline()으로 대체한다


from collections import deque
#n: 도시 개수 m: 단방향 도로 개수 k: 최단 거리, x: 시작 도시
n,m,k,x = map(int,input().split())
visited = [False] * (n+2)

graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

answer=[]
q = deque()
q.append((x,0)) #x,0번 부터 출발하는게 맞는가? (재확인_

while q:
    town,count = q.popleft()
    if count == k:
        answer.append(town)
    elif count < k:
        for i in graph[town]:
            if not visited[i]:
                visited[i] = True
                q.append((i,count+1))

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for ans in answer:
        print(ans)