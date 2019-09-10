#!/usr/bin/env python

n = int(input())
h = list(map(int, input().split()))
ans = float('inf')

def loop(index, cost):
    global ans
    if index == n - 1:
        ans = min(ans, cost)
    elif index == n - 2:
        ans = min(ans, cost + abs(h[index] - h[index + 1]))
    else:
        loop(index + 1, cost + abs(h[index] - h[index + 1]))
        loop(index + 2, cost + abs(h[index] - h[index + 2]))

loop(0, 0)
print(ans)
