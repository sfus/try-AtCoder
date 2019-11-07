#!/usr/bin/env python

def solve():
    n = int(input())
    s = input()
    ans = 1
    prev = s[0]
    for i in range(1, n):
        if prev != s[i]:
            ans += 1
            prev = s[i]
    return ans

print(solve())
