#!/usr/bin/env python
from math import ceil, sqrt

n = int(input())

# a * b = N, a <= b then a <= sqrt(N)
for i in range(int(ceil(sqrt(n))), 0, -1):
    if n % i == 0:
        print(i + n // i - 2)
        exit(0)
    else:
        continue
