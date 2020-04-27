# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:30:54 2020

@author: kjiwj
"""

def isPrime(n): 
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True

n = 10
s = 0
count = 0

while True:
    k = 1
    while isPrime(n % 10**k) and isPrime(n // 10**(len(str(n)) - k)):
        if (n % 10**k) == n:
            s += n
            count += 1
            break
        k += 1
    if count == 11:
        break
    else:
        n += 1

print(s)
