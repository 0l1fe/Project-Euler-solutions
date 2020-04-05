# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:20:06 2020

@author: kjiwj
"""

import datetime

y0 = 1901
y1 = 2001

count = 0

for year in range(y0, y1):
    for month in range(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:
            count += 1

print(count)
