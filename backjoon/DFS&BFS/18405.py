#https://www.acmicpc.net/problem/18405
#경쟁적 전염
#BFS

from sys import stdin 
from collections import deque

move = [[-1,0],[1,0],[0,-1],[0,1]]
N , K = map(int, stdin.readline().split())
board = [list(map(int,stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, stdin.readline().split())

q = []
for i in range(N):
    for j in range(N):
        if board[i][j]!= 0:
            q.append([board[i][j],i,j,0])

q.sort()
q = deque(q)
X -= 1
Y -= 1

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break
    else:
        for [dx,dy] in move:
            if 0 <= x+dx < N and - <= y+dy < N and board[x+dx][y+dy] ==0:
                board[x+dx][y+dy] = virus
                q.append([virus,x+dx,y+dy,time+1])
print(board[X][Y])