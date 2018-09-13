# coding=utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

big = 0
for x in range(100, 1000):
    for y in range(x, 1000):
        z = x*y
        s = str(z)
        if s == s[::-1] and z > big:
            big = z
print(big)


