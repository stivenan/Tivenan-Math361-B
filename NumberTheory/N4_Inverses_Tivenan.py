#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:56:44 2019

@author: StephenTivenan
"""
p=[]
m=19
for ii in range(1,m+1):
    if m % ii==1:
        p.append(ii)
print('These are the inverses of mod ', m,':', p, ' there are', len(p), 'elements' )