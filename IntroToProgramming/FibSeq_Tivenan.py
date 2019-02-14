#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 07:59:02 2019

@author: StephenTivenan

"""
my_list2=[]
my_list=[]
N=100
F0=1
F1=2
my_list.append(F0)
my_list.append(F1)

for ii in range(0,N):
    y=my_list[-2]+my_list[-1]
    my_list.append(y)
    

print('\nThis indicates whether the Catalans Principle is true for each term')
for xx in range(N-1):
    if (my_list[xx])**2-my_list[xx+1]*my_list[xx-1]==(-1)**(xx-1):
        print('true')
    else:
        print('false')


print('\n This is the last ten values in the sequence')        
print(my_list[-10:])

