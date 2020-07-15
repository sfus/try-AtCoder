#/usr/bin/env python

def solve():
    n = int(input())
    s = [input() for i in range(n)]
    ans = ''
    for v in ['AC', 'WA', 'TLE', 'RE']:
        ans += "{0} x {1}\n".format(v, s.count(v))
    return ans

print(solve())
