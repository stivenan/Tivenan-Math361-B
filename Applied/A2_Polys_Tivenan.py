#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:13:54 2019

@author: StephenTivenan
"""
##Let polynomial p=[1,2,3] be the polynomial from descending order of powers of polynomials
##That is the highest polynomial power is the first integer while, the lowest is the last integer
## p could be written as x^2+2x+3

p=[1,2,3]
def eva(y,x):
    i=len(x)
    m=[]
    for mm in range(i):
        j=y
        b=len(x)-mm-1
        j=j**b
        a=x[mm]*j
        m.append(a)
        pp=sum(m)
    return pp

print(eva(2,[1,2,3]), 'is the value of my polynomial where x=2 \n')


def dif(t,x):
    m=[]
    for mm in range(len(x)):
        r=x[len(x)-mm-1]*mm
        p=r*(t**(mm-1))
        m.append(p)
        ii=sum(m)
    return ii
print(dif(4,[1,2,3]), 'is the value the derivative of the polynomial at x=4 \n')


def inte(p,q,x):
    i=len(x)
    m=[]
    l=p
    r=q
    for mm in range(i):
        p=l
        q=r
        b=len(x)-mm
        q=q**b
        p=p**b
        a=x[mm]/b 
        f=p*a-q*a
        m.append(f)
        ii=sum(m)
    return ii

print(inte(2,1,[1,2,3]), 'is the value of the integral of the polynomial between 1 and 2')
