#!/usr/bin/env python

n = int(input())
pos = [list(map(int, input().split())) for i in range(n)]

prev_t, prev_x, prev_y = 0, 0, 0

for i in range(n):
    t, x, y = pos[i][0], pos[i][1], pos[i][2]

    lag = t - prev_t
    distance = abs(x - prev_x) + abs(y - prev_y)
    if distance > lag or lag % 2 != distance % 2:
        print("No")
        exit()

    prev_t, prev_x, prev_y = t, x, y

print("Yes")
