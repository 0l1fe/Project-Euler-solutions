# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:41:44 2020

@author: kjiwj
"""

def isPrime(n): 
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True

limit = 10001

count = 0
n = 2

while True:
    if isPrime(n):
        count += 1
        if count == limit:
            break
    n += 1

print(n)
