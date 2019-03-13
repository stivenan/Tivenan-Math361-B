#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:22:29 2019

@author: StephenTivenan
"""
funlist=[]
N=11
a0=53
funlist.append(a0)
for ii in range(N-1):
    if (a0 % 2==0):
        a0=a0/2
        funlist.append(a0)
    else:
        a0=3*a0+1
        funlist.append(a0)
    if(a0==1):
        print(funlist)
        print('It took',len(funlist), 'terms to reach 1')
        break
if(a0!=1):
    print('We did not reach the value 1 after',N, 'terms')