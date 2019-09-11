#!/usr/bin/env python

n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = list(float('inf') for i in range(n))
dp[0] = 0
for i in range(1, n):
    for j in range(i - k, i):
        if j < 0:
            continue
        dp[i] = min(dp[i], dp[j] + abs(h[i] - h[j]))

print(dp[n - 1])
