#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:27:07 2021

@author: violetxu
"""
import math 

def Pascal_triangle(k):
  pascal_line = []
  for i in range( k+1 ):
      pascal_line.append(math.comb(k,i))
  return pascal_line

print(Pascal_triangle(100))
print(Pascal_triangle(200))
    