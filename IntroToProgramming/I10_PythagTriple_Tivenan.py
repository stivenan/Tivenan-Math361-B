#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:05:33 2019

@author: StephenTivenan
"""
c=0
import numpy as np
y=np.zeros( [0,4] )
N=1000
for ii in range(1,N):
    for jj in range(ii,N):
        c=np.sqrt(ii**2+jj**2)
        if ii+jj+c>1026:
                break
        if c.is_integer() == True:
            y = np.vstack( [y, np.array( [ii, jj, c, ii+jj+c] ) ] )
            if ii+jj+c==1026:
                print('This is the pythagorean triplet where a+b+c=1026 \nwhere "a" is the 1st column, "b" is the 2nd column, and "c" is the 3rd column \n ', y[-1])
                break

        
       
   
                    
    
        
        