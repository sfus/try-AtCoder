#/usr/bin/python

def solve():
    a, b = input().split()
    ab = a * int(b)
    ba = b * int(a)
    if ab < ba:
        return ab
    else:
        return ba

print(solve())
