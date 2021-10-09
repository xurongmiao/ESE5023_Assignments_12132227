#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 11:38:18 2021

@author: violetxu
"""

def Least_moves(x):
    i = 0
    loc_x = x
    while loc_x > 1:
        i += 1
        if loc_x % 2 == 0:
            loc_x /= 2
        else:
            loc_x -=1
    return i

print(Least_moves(2))
print(Least_moves(5))

        