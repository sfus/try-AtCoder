#!/usr/bin/env python

n = int(input())

for i in range(2, 10):
    if n % i == 0 and 1 <= n // i <= 9:
        print('Yes')
        exit()

print('No')
