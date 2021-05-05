# https://www.acmicpc.net/problem/2178
import sys 
from collections import deque

def bfs(n,m,maze):
    q = deque()
    q.append((0,0))
    distance = [[0] * m for _ in range(n)]
    distance[0][0] = 1
    cnt = 1 
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            print('nx,ny-->{},{}'.format(nx,ny))
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if maze[ny][nx] == '1' and distance[ny][nx] == 0:
                distance[ny][nx] = distance[y][x] + 1
                q.append((nx, ny))
        print('--------')
        
    return distance[n-1][m-1]


def main(): 
    n, m = map(int, input().split(' '))
    maze = [input() for _ in range(n)]
    print(maze)
    print(bfs(n,m,maze))
 

if __name__ == '__main__': 
    main()

