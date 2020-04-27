# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:12:49 2020

@author: kjiwj
"""

C = [1, 2, 5, 10, 20, 50, 100, 200]

limit = 200

S = [1] + [0] * limit

for c in C:
    for i in range(len(S) - c):
        S[i + c] += S[i]

print(S[-1])
