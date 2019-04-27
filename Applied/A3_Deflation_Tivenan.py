#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:39:42 2019

@author: StephenTivenan
"""
import numpy as np
def add(f,p):
    r=[]
    if len(f)==len(p):
        aa=f
        bb=p
        a=len(p)
        b=len(f)
    if len(p)>len(f):
        aa=p
        bb=f
        a=len(p)
        b=len(f)
    if len(f)>len(p):
        aa=f
        bb=p
        a=len(f)
        b=len(p)
    for ii in range(a):
        for jj in range(b):
            if ii==jj:
                aa[ii]=aa[ii]+bb[jj]
        r.append(aa[ii])
    return r       


def subtract(f,p):
    r=[]
    if len(f)==len(p):
        aa=f
        bb=p
        a=len(p)
        b=len(f)
    if len(p)>len(f):
        aa=p
        bb=f
        a=len(p)
        b=len(f)
    if len(f)>len(p):
        aa=f
        bb=p
        a=len(f)
        b=len(p)
    for ii in range(a):
        for jj in range(b):
            if ii==jj:
                aa[ii]=aa[ii]-bb[jj]
        r.append(aa[ii])
    return r       


def multiplication(x,u):
    m=[]
    for ii in range(len(x)):
        for jj in range(len(u)):
            b=x[ii]*u[jj]
            if x[ii]==0:
                for pp in range(len(x)):
                    t=0
                    m.append(t)
                    break
                break
            m.append(b)
    return m 


def DivisionLT(f,p):
    r=[]
    if len(f)==len(p):
        aa=f
        bb=p
        a=len(p)
        b=len(f)
    if len(p)>len(f):
        aa=p
        bb=f
        a=len(p)
        b=len(f)
    if len(f)>len(p):
        aa=f
        bb=p
        a=len(f)
        b=len(p)
    l=aa[0]/bb[0]
    r.append(l)
    for jj in range(a-b):
        r.append(0)
    return r





def clean_poly(p):
    highest_deg = 0
    for ii in range(0,len(p)):
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg += 1
    
    
    
            
        
    del p[:highest_deg]
    
    
    return p

## The function f is from highest degree to lowest degree of the polynomial
## The function g is the polynomial that divides the larger the larger polynomial f and its degree is from highest to lowest
def division(f,g):
    q=[0]
    m=list(f)
    r=f
    quo=[]
    while r!=[] and len(f)>len(g):
        f=r
        a=DivisionLT(f,g)
        q=add(q,a)
        quo.append(a[0])
        b=multiplication(a,g)
        r=subtract(r,b)
        r=clean_poly(r)
        return print('\nThis is function of life:', m,'\nThis is the divisor:', g,'\nThis is the quotient:', quo,'\nThis is the remainder:',r)
division([2,3,4],[2,3])
#for ii in range(1):
#     r=p
#     a=DivisionLT(p,w)
#     print(a)
#     q=add(q,a)
#     print(q)
#     b=multiplication(a,w)
#     print(b)
#     r=subtract(r,b)
#     print(r)
#     r=clean_poly(r)
#     print(r)


