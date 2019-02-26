#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:54:50 2019

@author: StephenTivenan
"""


    
def prime_check(x):
    is_prime = True
    
    for ii in range(2,x):
        if  x % ii==0 :
            return False
    return is_prime

n=1
ii=0
prime_number=[]
while len(prime_number)<=n:
    ii+=1
    if prime_check(ii)==True:
       prime_number.append(ii)

print('This is the', n,'th  prime number is:\n', prime_number[-1])


