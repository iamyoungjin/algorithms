#https://www.acmicpc.net/problem/12015

# DP로 풀면 시간 초과(현재 위치 이전 모든 것들을 방문할 필요가 없다)
import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))