#!/usr/bin/python

def solve():
    n, m = map(int, input().split())
    if n == m:
        return 'Yes'
    else:
        return 'No'

print(solve())
