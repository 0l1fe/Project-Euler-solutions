# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:32:25 2020

@author: kjiwj
"""

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 6
    while(i * i <= n):
        if (n % (i - 1) == 0 or n % (i + 1) == 0):
            return False
        i = i + 6
    return True

number = 600851475143

n = 1 #ignore 2

while n < number:
    if number % n == 0:
        if isPrime(n):
            number //= n
            continue
    n += 2

print(n)
