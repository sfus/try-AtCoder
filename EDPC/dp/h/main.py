#!/usr/bin/env python

h, w = map(int, input().split())

matrix = [list(input()) for i in range(h)]
dp = [[0] * w for i in range(h)]

dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if matrix[i][j] == '#':
            continue
        if j < w - 1 and matrix[i][j + 1] != '#':
            dp[i][j + 1] = dp[i][j] + dp[i][j + 1]
        if i < h - 1 and matrix[i + 1][j] != '#':
            dp[i + 1][j] = dp[i][j]

ans = dp[h - 1][w - 1] % (10 ** 9 + 7)
print(ans)
