# https://www.acmicpc.net/problem/2606
# 일반적으로 dfs/bfs문제를 풀 때 트리 방식으로 문제를 해결하지만
# 상위/하위 노드가 정해진것이 아니면 그래프 방식도 가능 


from sys import stdin
read = stdin.readline
'''
그러나 반복문으로 여러줄 입력받는 상황에서는
sys.stdin.readline()을 사용해야 시간초과가 발생하지 않는다.

sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 
개행문자가 같이 입력 받아진다
만약 3을 입력했다면, 3\n 이 저장되기 때문에, 
개행문자를 제거해야 한다
'''

dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)
print('dic02-->{}'.format(dic))

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
        print(visited)
visited = []
dfs(1, dic)
print(len(visited)-1)