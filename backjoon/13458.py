#https://www.acmicpc.net/problem/13458

# N : 시험장 개수 
# B : 총감독관이 감시할 수 있는 응시자 수  / C: 부감독관이 감시할 수 있는 응시자 수 
# tester_num : 각 시험장에 있는 응시자 수 
# 각 시험장에 총감독관은 오직 1명, 부감독관은 여러명 가능 

import sys
input = sys.stdin.readline
n = int(input())
tester_num = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0
for i in tester_num:
    i -= b
    cnt = 1
    if i > 0:
        cnt += i // c
        if i % c != 0:
            cnt += 1
    result += cnt
print(result)