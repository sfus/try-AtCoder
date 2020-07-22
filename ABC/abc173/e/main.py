#/usr/bin/env python

def solve():
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)

    mod = 10 ** 9 + 7
    l = 0
    r = n - 1
    ans = 1

    if k % 2 == 1:
        ans = a[0]
        l = 1

    # If the maximum number is negative and k is odd, the answer is the product of the first k numbers.
    if ans < 0:
        mul = 1
        for i in range(k):
            mul = mul * a[i] % mod
        return mul

    # otherwise, multiply the leftmost two products and the rightmost two products, whichever is larger.
    for i in range(k//2):
        l_mul = a[l] * a[l+1]
        r_mul = a[r] * a[r-1]
        if l_mul >= r_mul:
            ans = ans * l_mul % mod
            l += 2
        else:
            ans = ans * r_mul % mod
            r -= 2

    return ans

print(solve())
