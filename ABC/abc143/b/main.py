#!/usr/bin/env python

def solve():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            ans += d[i] * d[j]
    return ans

print(solve())
