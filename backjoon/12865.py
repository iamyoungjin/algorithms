#dynamic programming 0511

'''
D[i][j] = 배낭에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치

D[i][j] = D[i - 1][j]  ( j < w )
D[i][j] = max( D[i - 1][j], D[i - 1][j - w] + v )  ( j >= w)
'''

import sys

n, k = map(int, input().split(' '))
_map = [ [0]*(k+1) for _ in range(n+1) ]

for i in range(1, n+1):
    w, v = map(int, input().split(' '))
    for j in range(1, k+1):
        if j < w:
            _map[i][j] = _map[i-1][j]
        else:
            _map[i][j] = max(_map[i-1][j], _map[i-1][j-w] + v)
            
print(_map[n][k])