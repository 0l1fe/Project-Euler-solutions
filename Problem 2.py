# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:50:32 2020

@author: kjiwj
"""

def F(n):
    if n <= 1:
        return n
    else:
        return(F(n - 1) + F(n - 2))

limit = 4000000
		
sum = 0
n = 1

while F(n) <= limit:
    if F(n) % 2 == 0:
        sum += F(n)
    n += 1

print(sum)
