#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:12:47 2021

@author: violetxu
"""

a=float(input("输入数字a"))
b=float(input("输入数字b"))
c=float(input("输入数字c"))
def Print_values (a, b, c):
   if a > b:
       if b > c:
           print(a, b, c)
       else:
           if a > c :
               print(a, c, b)
           else:
               print(c, a, b)
   else:
       if b < c:
           print(c, b, a)
Print_values (a, b, c)              
   
