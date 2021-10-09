#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:43:58 2021

@author: violetxu
"""

import random
M1 = []
for i in range (5):
       b = []
       for j in range(10):
           b.append(random.randint(0, 50))
       M1.append(b)       
print(M1)


M2 = []
for i in range (10):
       b = []
       for j in range(5):
           b.append(random.randint(0, 50))
       M2.append(b) 
print(M2)        

def Matrix_multip(A, B):
  M = []
  for i in range (5):
        c = []
        for j in range (5):
            x = 0
            for k in range (10):
                x = x +(A[i][k]* B[k][j])
            c.append(x)
        M.append(c)
  return M

print(Matrix_multip(M1, M2))                 
