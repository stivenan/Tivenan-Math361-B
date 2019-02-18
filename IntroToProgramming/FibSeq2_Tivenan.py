#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:01:52 2019

@author: StephenTivenan
"""

my_list2=[]
my_list=[]
N=100
F0=0
F1=1
m=10
my_list.append(F0)
my_list.append(F1)

for ii in range(0,N):
    y=my_list[-2]+my_list[-1]
    my_list.append(y)
    if (y%m==0):
        my_list2.append(y)
    else:
        continue
    
print('These are the terms that are multiples of m:''\n')       
print(my_list2)
print('\n''This is the total amount of the terms that are multiples of m')  
print(len(my_list2))
