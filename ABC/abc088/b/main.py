#/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

alice = bob = 0
for i, value in enumerate(sorted(a, reverse=True)):
    if i % 2 == 0:
        alice += value
    else:
        bob += value

print(alice - bob)
