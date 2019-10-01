#!/usr/bin/env python

# n: # of vertex, m: # of edge
n, m = map(int, (input().split()))

dp = [-1] * n
graph = [[] for i in range(n)]

def rec(num):
    if dp[num] != -1:
        return dp[num]
    maximum = 0
    for i in graph[num]:
        maximum = max(maximum, rec(i) + 1)
    dp[num] = maximum
    return dp[num]

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

ans = 0
for i in range(n):
    ans = max(ans, rec(i))

print(ans)
