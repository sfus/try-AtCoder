#!/usr/bin/env python

def solve():
    a, b = map(int, input().split())
    ans = a - b * 2
    return max(ans, 0)

print(solve())
