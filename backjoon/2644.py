#https://www.acmicpc.net/problem/2644

from collections import deque

def bfs(v, target):
    count = 0
    q = deque([[v, count]])
    print('q---->{}'.format(q))
    while q:
        value = q.popleft()
        print('value---->{}'.format(value))
        v = value[0]
        print('v---->{}'.format(v))
        count = value[1]
        if v == target:
            return count
            
        if not visited[v]:
            count += 1
            visited[v] = True
            for e in adj[v]:
                if not visited[e]:
                    q.append([e, count])
    return -1

n = int(input()) # 전체 사람의 수 
q1, q2 = map(int, input().split()) #촌수를 계산해야 하는 서로 다른 두 사람의 번호 
m = int(input()) # 부모 자식들 관계 개수 
adj = [[] for _ in range(n+1)]
print('adj--->{}'.format(adj))
visited = [False] * (n+1)
print('visited--->{}'.format(visited))


#연결 관계 만들기 
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    print('adj--->{}'.format(adj))
    
print(bfs(q1, q2))