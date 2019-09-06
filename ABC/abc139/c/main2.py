#!/usr/bin/env python

n = int(input())
h = list(map(int, input().split()))

ans = 0
index = 0
while index < n:
    count = 0
    for j in range(index, n - 1):
        if h[j] >= h[j + 1]:
            count += 1
        else:
            break

    if count > ans:
        ans = count

    index += count + 1

print(count)
