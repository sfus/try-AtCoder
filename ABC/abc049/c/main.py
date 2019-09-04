#!/usr/bin/env python

s = input()
rev_s = s[::-1]
words = ['dream', 'dreamer', 'erase', 'eraser']
rev_words = [i[::-1] for i in words]

i = 0
max = len(s)
while i < max:
    found = False
    for word in rev_words:
        if rev_s[i:].startswith(word):
            found = True
            i += len(word)
            break
    if not found:
        print("NO")
        exit()

print("YES")
