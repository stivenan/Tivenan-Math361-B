#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:10:48 2019

@author: StephenTivenan
"""
import numpy as np
N=12
TOL=1e-4
z0=-8
p=2
f_z= lambda z: 1/100*(z**4+(np.e-2-np.sqrt(2))*z**3+(-np.sqrt(2)*np.e-3-2*np.e+2*np.sqrt(2))*z**2+(-3*np.e+2*np.sqrt(2)*np.e-3*np.sqrt(2))*z+3*np.sqrt(2)*np.e)
z_n= lambda z: 1/100*(4*z**3+(np.e-2-np.sqrt(2))*3*z**2+(-np.sqrt(2)*np.e-3-2*np.e+2*np.sqrt(2))*2*z+(-3*np.e+2*np.sqrt(2)*np.e-3*np.sqrt(2)))
m=[]
z=np.zeros([0,2])
for ii in range(N):
        b=z0-(f_z(z0)/z_n(z0))
        a=z0-b
        z = np.vstack( [z, np.array([z0,abs(a)])])
        z0=b
        if TOL>abs(a):
            m.append(z0)
            print('The last row in the left column is a root of the function,\n The second column is the absolute value differences between the current and previous values ')
            print(z)
            break
if TOL<abs(a):
    print('After', N, 'iterations there is no root')
    print(z)
