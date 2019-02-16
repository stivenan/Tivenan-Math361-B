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
m=9
my_list.append(F0)
my_list.append(F1)

for ii in range(0,N):
    y=my_list[-2]+my_list[-1]
    my_list.append(y)
    if (y%m==0):
        my_list2.append(y)
    else:
        continue
    
       
print(my_list2)

print(my_list)
