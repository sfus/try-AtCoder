#!/usr/bin/env python

n = int(input())
h = list(map(int, input().split()))

dp = list(float('inf') for i in range(n))
dp[0] = 0
for i in range(1, n):
    if i == 1:
        dp[1] = abs(h[1] - h[0])
    else:
        jump1 = dp[i - 1] + abs(h[i] - h[i - 1])
        jump2 = dp[i - 2] + abs(h[i] - h[i - 2])
        dp[i] = min(jump1, jump2)

print(dp[n - 1])
