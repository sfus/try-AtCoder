#!/usr/bin/env python

n = int(input())
p = list(map(float, input().split()))
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(n + 1):
        dp[i + 1][j] += dp[i][j] * (1 - p[i])
        if (j < n):
            dp[i + 1][j + 1] += dp[i][j] * p[i]

num_half = (n + 1) // 2
print(sum(dp[n][num_half:]))
