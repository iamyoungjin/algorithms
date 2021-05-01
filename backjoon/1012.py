#https://www.acmicpc.net/problem/1012


import sys 
sys.setrecursionlimit(10000) 

t = int(input()) #test case 개수
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):  #X Y: 배추가 심어져있는 줄 위치
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q, w])


for i in range(t):
    m, n, k = map(int, input().split()) # M: 가로 N: 세로 K: 배추가 심어져 있는 위치 개수
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(q, w) 
                s[q][w] = 0
                cnt += 1
    print(cnt)