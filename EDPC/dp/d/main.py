#!/usr/bin/env python

n, cap = map(int, input().split())
dp = [[0] * (cap + 1) for i in range(n + 1)]

for i in range(n):
    w, v = map(int, input().split())
    for j in range(cap + 1):
        if j - w >= 0:
            dp[i + 1][j] = max(dp[i][j - w] + v, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[n][cap])
