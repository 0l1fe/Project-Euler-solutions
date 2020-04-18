# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:55:07 2020

@author: kjiwj
"""

limit = 100

A = []

for a in range(2, limit + 1):
    for b in range(2, limit + 1):
        A.append(a ** b)

print(len(set(A)))
