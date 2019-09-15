#!/usr/bin/env python

n = int(input())
score = [0, 0, 0]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(3):
        max_num = 0
        for k in range(3):
            if j == k:
                continue
            max_num = max(max_num, score[k])
        line[j] += max_num
    score = line

print(max(score))
