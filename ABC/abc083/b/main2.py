#/usr/bin/env python

n, a, b = map(int, input().split())

def sumCols(val):
    return sum(list(map(int, list(str(val)))))

ret = 0
for i in range(n + 1):
    total = sumCols(i)
    if a <= total <= b:
        ret += i

print(ret)
