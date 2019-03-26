#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:17:16 2019

@author: StephenTivenan
"""

p=[]
m=79
for ii in range(1,m+1):
    if m % ii==0 and ii!=1:
        p.append(ii)
print('These are the zeros of mod ', m,':', p, ' there are', len(p), 'elements' )