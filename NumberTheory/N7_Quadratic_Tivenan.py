#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:07:39 2019

@author: StephenTivenan
"""
import numpy as np
def prime_check(x):
    is_prime = True
    for ii in range(2, x):
        if  (x % ii==0) :
            return is_prime==False
    return is_prime
P=700
b=0
for jj in range(2, P+1):
    m=[]
    count_array=[]
    k=np.zeros([0,2])
    if prime_check(jj)==True:
        for ii in range(jj):
            p=ii*ii
            r=p%jj
            if r in set(m):
                break
            m.append(r)
            b=b+1
        k = np.vstack( [k, np.array([jj,len(m)])])
        print(k)
count_array.append(b)    
print('The first column states the prime number, the second column states the total amount of quadratic residues for a given prime. For p <=',P,'The total of number of Quadratic Residues is', count_array)    


print('\n 1 indicates that there is a 1-p that exist as a quadratic residue in mod p, while 0 idicates that there are no quadratic residues that equal 1-p in modp. The first column indicates which modular prime number is being used ')               
for nn in range(2, P+1):
    m=[]
    o=False
    count_array=[]
    neg_one=np.zeros([0,2])
    
    if prime_check(nn)==True:
        for ii in range(nn):
            p=ii*ii
            r=p%nn
            m.append(r)
            if r==nn-1 in set(m):
                o=True
                break
        neg_one = np.vstack( [neg_one, np.array([nn,o])])
        print(neg_one)
        
        
       