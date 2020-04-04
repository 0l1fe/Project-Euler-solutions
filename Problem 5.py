# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:22:53 2020

@author: kjiwj
"""

def gcd(a, b):
    if (b == 0):
         return a
    return gcd(b, a % b)
	
def lcm(a, b):
    return (a * b) // gcd(a, b)

limit = 20

m = 1

for n in range(1, limit):
    m = lcm(m, n)
    
print(m)
