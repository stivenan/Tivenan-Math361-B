#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:57:30 2019

@author: StephenTivenan
"""
import numpy as np
def pdivisor(x):
    p=[]
    for ii in range(1,x):
        if x % ii==0:
            p.append(ii) 
    return p
N=284
u=np.zeros( [0,2] )
for ii in range(2,N+1):
    y=pdivisor(ii)
    a=sum(y)
    for jj in range(2,N+1):
        q=pdivisor(jj)
        b=sum(q)
        if a==jj and b==ii:
            u=np.vstack( [u, np.array( [ii, jj] ) ] )
print('These are the amicable numbers below ', N,':\n', u)
