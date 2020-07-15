#/usr/bin/env python

def solve():
    price = int(input())
    mod = price % 1000
    return (1000 - mod) % 1000

print(solve())
