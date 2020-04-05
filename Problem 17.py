# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:10:44 2020

@author: kjiwj
"""

TO20 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def write(n):
        WORD = ""
        if n // 100 != 0:
            WORD += TO20[n // 100] + "hundred"
            if n % 100 != 0:
                WORD += "and"
        if n % 100 != 0:
            if n % 100 < 20:
                WORD += TO20[n % 100]
            else:
                WORD += TENS[(n % 100) // 10]
                WORD += TO20[n % 10]
        return WORD

R = 1000
onethousand = 11

S = 0

for n in range(R):
    S += len(write(n))
    
print(S + onethousand)
