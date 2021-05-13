#https://www.acmicpc.net/problem/11053


#Dynamic Programming 풀이법
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]: #현재 위치(i)보다 이전 원소(j)가 작은지 확인 (크거나 같으면 가장 긴 증가하는 부분 수열이 될 수 없음)
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

