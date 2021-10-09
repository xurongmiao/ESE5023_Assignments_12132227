#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 13:57:38 2021

@author: violetxu
"""

def operation_eval(op_list):
    sign_op = op_list[0]
    cur_val = 1
    val_list = []
    for i in range(8):
        cur_op = op_list[i+1]
        if cur_op == 0:
            cur_val = cur_val * 10 + (i+2)
        else:
            val_list.append(sign_op * cur_val)
            cur_val = i+2
            sign_op = cur_op
    val_list.append(sign_op * cur_val)

    res = 0
    for i in range(len(val_list)):
        res = res + val_list[i]
    return res, val_list

def valuelist_print(val_list, x):
    isVisuable = False
    asw_str = "" + str(val_list[0])
    loop_counter = len(val_list) - 1
    for i in range(loop_counter):
        cur_value = val_list[i+1]
        if cur_value > 0:
            asw_str += "+" + str(cur_value)
        else:
            asw_str += str(cur_value)
    asw_str += "=" + str(x)
    if isVisuable:
        print(asw_str)
    return

def Find_expression(x):
    loop_counter= 0
    asw_counter = 0
    max_count   = 3 ** 8
    for i in range(max_count):
        op_list = [1]
        # 将0-3^8改写为8位的三进制数，枚举
        for j in range(8):
            cur_op = ((loop_counter // (3 ** j)) % 3) - 1
            op_list.append(cur_op)
        # 将数字与符号关联得到计算结果
        loc_res, loc_val_list = operation_eval(op_list)
        if loc_res == x:
            asw_counter += 1
            valuelist_print(loc_val_list, x)
        loop_counter += 1

    for i in range(max_count):
        op_list = [-1]
        for j in range(8):
            cur_op = ((loop_counter // (3 ** j)) % 3) - 1
            op_list.append(cur_op)
        loc_res, loc_val_list = operation_eval(op_list)
        if loc_res == x:
            asw_counter += 1
            valuelist_print(loc_val_list, x)
        loop_counter += 1
    return asw_counter

def plot_answer_number():
    asw_num = []
    for i in range(100):
        num = Find_expression(i+1)
        asw_num.append(num)
    # To Do: Plotting
    # print(asw_num)
    return asw_num


cnt = Find_expression(50)
# print(cnt)
# 第二问
Total_solutions = plot_answer_number()
print(Total_solutions)

import matplotlib.pyplot as plt
number= range(1,101)
plt.plot(number, Total_solutions)
plt.show


loc_max = -1
loc_min = 100000
loc_max_index = -1
loc_min_index = -1
for i in range(100):
    if Total_solutions[i] > loc_max:
        loc_max = Total_solutions[i]
        loc_max_index = i
    if Total_solutions[i] < loc_min:
        loc_min = Total_solutions[i]
        loc_min_index = i
print("Number " + str(loc_max_index+1) +" have the max expression")
print("Number " + str(loc_min_index+1) +" have the max expression")

        
    


