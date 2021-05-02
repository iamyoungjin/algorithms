#https://www.acmicpc.net/problem/4796

# L, P: 연속하는 P일 중 L일 동안만 캠핑장을 사용할 수 있음 
# V: V일 짜리 휴가를 시작 

import sys
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int,input().split())
    if L+P+V == 0:
        break

    res = (V//P)*L
    res += min((V%P),L)
    print('Case %d: %d' %(i,res))
    i+=1