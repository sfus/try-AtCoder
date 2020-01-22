#/usr/bin/env python

def solve():
    n, a, b = map(int, input().split())

    def sumCols(val):
        sum = 0
        next = val
        while next > 0:
            sum += next % 10
            next //= 10
        return sum


    ret = 0
    for i in range(n + 1):
        sum = sumCols(i)
        if a <= sum <= b:
            ret += i

    return ret

print(solve())
