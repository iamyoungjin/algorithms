#음료수 얼려 먹기

def dfs(x,y):
    #주어진 경로를 벗어나는 경우 종료
    if x<=1 or x>=n or y<=1 or y>=m:
        return False
    #현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        #상 하 좌 우 위치 모두 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#n,m을 공백 기준으로 구분하여 입력 받기
n,m = map(int,input().split())

#2차원 리스트의 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행 
        if dfs(i,j) == True:
            result += 1

print(result)