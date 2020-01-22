#/usr/bin/env python

def sumCols(val):
    return sum(list(map(int, list(str(val)))))

def solve():
    n, a, b = map(int, input().split())
    ret = 0
    for i in range(n + 1):
        total = sumCols(i)
        if a <= total <= b:
            ret += i
    return ret

print(solve())
