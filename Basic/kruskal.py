#신장트리 : 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프 (트리의 조건)

'''
최소한의 비용으로 구성되는 신장트리를 찾아야 할떄
ex) N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우
'''


#대표적인 최소 신장트리 알고리즘 : 크루스칼 알고리즘
#1) 간선 데이터를 비용에 따라 오름차순으로 정렬
#2) 간선을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인
#   1.사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#   2.사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
#3) 모든 간선에 대하여 2번 과정 반복 


#특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    #루트노드 찾을때 까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union연산) 의 개수 입력 받기
v,e = map(int,input().split())
parent = [0]*(v+1) #부모테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result = 0

#부모 테이블 상에서 ,부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] =i

#모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인 하며 
for edge in edges:
    cost,a,b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)