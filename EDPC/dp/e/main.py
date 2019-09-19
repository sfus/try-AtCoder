#!/usr/bin/env python

n, cap = map(int, input().split())
max_num = 100
max_value = 1000
max_sum_v = max_value * max_num
dp = [[float('inf')] * (max_sum_v + 1) for i in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    w, v = map(int, input().split())
    for j in range(max_sum_v + 1):
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i][j - v] + w, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

ans = 0
for i in range(max_sum_v):
    if dp[n][i] <= cap:
        ans = max(ans, i)

print(ans)
