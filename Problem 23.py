# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:46:27 2020

@author: kjiwj
"""

limit = 28123

def s(n):
    s = 0
    for d in range(1, n // 2 + 1):
        if n % d == 0:
            s += d
    return s

A = []

for n in range(limit):
    if s(n) > n:
        A.append(n)

B = [0] * limit

for i in range(len(A)):
    for j in range(i + 1):
        if (A[i] + A[j] < limit):
            B[A[i] + A[j]] = 1

s = 0

for i in range(limit):
    if B[i] == 0:
        s += i

print(s)
