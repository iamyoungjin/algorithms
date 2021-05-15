#https://www.acmicpc.net/problem/12015



# DP로 풀면 시간 초과(현재 위치 이전 모든 것들을 방문할 필요가 없다)
# import bisect

# x = int(input())
# arr = list(map(int, input().split()))

# dp = [arr[0]]

# for i in range(x):
#     if arr[i] > dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx = bisect.bisect_left(dp, arr[i])
#         dp[idx] = arr[i]

# print(len(dp))

# Use Binary Search 
import sys 

def find(target): 
    l, h = 1, len(stack)-1 
    while l < h:
         m = (l+h)//2 
         if stack[m] < target: 
             l = m+1 
        elif stack[m] > target: 
            h = m 
        else: l = h = m 
    return h
l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split())) 
stack = [0]
for a in arr:
    if stack[-1] < a: 
        stack.append(a) 
    else: stack[find(a)] = a 
print(len(stack)-1)

'''
잘 이해가가지 않는다... 시간을 갖고 생각해볼 것 
reference 
https://www.acmicpc.net/problem/12015
'''