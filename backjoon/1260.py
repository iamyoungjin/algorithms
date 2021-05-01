#https://www.acmicpc.net/problem/1260

# N : 정점의 개수
# M : 간선의 개수
# V : 탐색을 시작할 정점의 번호 

N,M,V=map(int,input().split()) 
matrix=[[0]*(N+1) for i in range(N+1)]   # 4 5 1 -> 5 x 5 matrix (start 0)

for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
    # print('matrix changed--->',matrix)
visit_list=[0]*(N+1)
# print('visit_list--->',visit_list) #[0,0,0,0,0]

def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(V)
print()
bfs(V)