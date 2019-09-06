#!/usr/bin/env python

n = int(input())
h = list(map(int, input().split()))

count = 0
for i in range(n):
    cur_count = 0
    for j in range(i, n - 1):
        if h[j] >= h[j + 1]:
            cur_count += 1
        else:
            break

    if cur_count > count:
        count = cur_count

print(count)
