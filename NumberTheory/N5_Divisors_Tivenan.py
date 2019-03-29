#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 07:48:43 2019

@author: StephenTivenan
"""
def pdivisor(x):
    p=[]
    for ii in range(1,x):
        if x % ii==0:
            p.append(ii)
    return p

       