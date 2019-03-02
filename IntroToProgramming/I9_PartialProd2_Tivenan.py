#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:37:21 2019

@author: StephenTivenan
"""
b_n= lambda n:n**3+1

a_n= lambda n:n

N=500

p=[]
a=1
for ii in range(1, N):
    d=(a_n(ii)/b_n(ii))+1
    a=d*a
    p.append(a)
       
print('These are the first 15 terms of the 1st infinite series \n ', p[:15],' \n')

print('These are the last 15 terms of the 1st infinite series \n ', p[-15:],' \n')





b=1/4
q=[]
one=1
for mm in range(1,N):
    x=1+b**mm
    one=one*x
    q.append(one)
print('These are first 15 terms of the 2nd infinite series  \n ', q[:15],' \n')
    
print('These are last 15 terms of the 2nd infinite series  \n ', q[-15:])