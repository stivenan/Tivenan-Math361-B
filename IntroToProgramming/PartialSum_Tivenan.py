#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:28:45 2019

@author: StephenTivenan
"""
import numpy as np


empty=[]
empty3=[]
empty2=[]
p=np.array([empty, empty2, empty3])
addsum=0
n=1000000
for xx in range(1,n):
    float_convert=float(xx)
    yy=np.log(float_convert**4+float_convert+3)/(float_convert**(1/2)+3)
    addsum=addsum+yy
    empty.append(addsum)


addsum1=0
n=10000
for xx in range(1,n):
    float_convert1=float(xx)
    yy=np.exp(float_convert1/100)/(float_convert1**10)
    addsum1=addsum1+yy
    empty2.append(addsum1)
    
addsum2=0
n=10000
for mm in range(1,n): 
   pp=1/(mm**(4))
   addsum2=addsum2+pp
   empty3.append(addsum2)

print('The following set are the first 15 in the s_n Infinite Series')
up=np.array((empty[:15]))
print(up)
print("\n")

print('The following sets are the last 15 terms of s_n Infinite Series')
up1=np.array((empty[-15:]))
print(up1)
print("\n")
print('The following sets are the first 15  in the t_n Infinite Series')
down=np.array((empty2[:15]))
print(down)
print("\n")
print('The following sets are the last 15 terms of t_n Infinite Series')
down1=np.array((empty2[-15:]))
print(down1)
print("\n")
print('The following sets are the first 15 terms of 1/x^4 Infinite Series')
middle=np.array((empty3[:15]))
print(middle)
print("\n")
print('The following sets are the last 15 terms of 1/x^4 Infinite Series')
middle1=np.array((empty3[-15:]))                 
print(middle1)
print("\n")

