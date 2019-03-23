#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:06:29 2019

@author: StephenTivenan
"""
import math
import numpy as np
def prime_check(x):
    is_prime = True
    for ii in range(2, math.ceil(x**.5)+1):
        if  (x % ii==0) and (x != 1) and (x!= 2):
            return is_prime==False
    return is_prime

N=10000
list1=[]
m=1
for ii in range(1,N):
    if (ii % 2!=0) and (prime_check(ii)==False):
        m=0
        for jj in range(2,N):
             if prime_check(jj)==True and ii>jj:
                 a=np.sqrt((ii-jj)/2)
                 if a.is_integer()==True and ii>jj:
                     m=1
                     break
        if (m==0):
            print('The number ',ii,' cannot be written as the sum of a prime and twice a square')
            break
            
   


