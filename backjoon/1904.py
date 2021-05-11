#dynamic programing
'''
길이가 i인 수열을 형성하는 방법은 두가지 뿐
1) i-1 + [1] 
2) i-2 + [00]
따라서  D[i] = D[i-1] + D[i-2]
피보나치 수열과 동일한 문제 
'''

import sys 
input = sys.stdin.readline
n = int(input()) 
dp = [0] * 1000001 
dp[1] = 1 
dp[2] = 2 

for i in range(3,n+1):
     dp[i] = (dp[i-1]+ dp[i-2])%15746 
print(dp[n])

