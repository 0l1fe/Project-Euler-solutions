# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:32:25 2020

@author: kjiwj
"""

def isPrime(n): 
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True

number = 600851475143

n = 1 a

while n < number:
    if number % n == 0:
        if isPrime(n):
            number //= n
            continue
    n += 1

print(n)
