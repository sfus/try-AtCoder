#!/usr/bin/env python

a, b = list(map(int, input().split()))

for i in range(20):
    if (a - 1) * i + 1 >= b:
        print(i)
        exit()
