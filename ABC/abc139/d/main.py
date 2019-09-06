#!/usr/bin/env python

n = int(input())

# n%1 + 1%2 + 2%3 + ... + (n-1)%n = n + 1 + 2 + ... + n-1 = 1/2 * (n-1) * n)
print((n - 1) * n // 2)

# 1 ~ n の合計は 1/2 * n * (n + 1)
# https://mathwords.net/1karannowa
