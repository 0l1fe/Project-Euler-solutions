# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:50:32 2020

@author: kjiwj
"""

def fibonacci(n) :
    if n <= 1 :
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))

limit = 4000000		

sum = 0
n = 1

while fibonacci(n) <= limit :
    if fibonacci(n) % 2 == 0 :
        sum += fibonacci(n)
    n += 1
    
print(sum)
