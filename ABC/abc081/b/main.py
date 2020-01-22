#!/usr/bin/env python

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    loop = True
    while loop:
        for i, item in enumerate(a):
            if item % 2 == 0:
                a[i] = item / 2
            else:
                loop = False
                break
        if loop:
            count += 1
    return count

print(solve())
