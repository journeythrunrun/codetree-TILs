# 빠른 유형 습득 훑이 좋을 터인데 

n = int(input())

MAX_NUM = 45

dp = [0 for _ in range(MAX_NUM + 1)]

dp[1] = dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    
print(dp[n])