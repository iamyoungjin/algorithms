'''
서로소 disjoints sets (union find자료구조) : 소로소 집합 : 공통원소가 없는 두집합
서로소 집합 자류구조는 서로소 부분집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- 합집합(union) : 두개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
- 찾기(find) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
'''

#1. 합집합(Union) 연산을 확인하여 서로 연결된 두노드 a,b를 확인
#    -1) A와 B루트 노드 A`, B`를 각각 찾는다
#    -2) A`를 B` 부모 노드로 설정 
#2. 모든 합집합(Union) 연산을 처리할때 까지 1번 과정 반복

'''
기본적은 형태의 소로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없어, 부모 테이블을 계속 확인하여 거슬러 올라가야 한다
'''

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
#루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x 
#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
#노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = map(int,input().split())
parent = [0] * (v+1) #부모 테이블 초기화
#부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i
#Union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()
#부모 테이블 내용 출력
print('부모 테이블:',end ='')
for i in range(1,v+1):
    print(parent[i],end=' ')