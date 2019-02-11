#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 23:11:43 2019

@author: StephenTivenan
"""
import numpy as np
partialprod=[]
n=900000
new=1
for ii in range(2,n):
    j=(ii**3-1)/(ii**3+1)
    new=j*new
    partialprod.append(new)



partialprod2=[]
n=450
total2=1
for pp in range(1,n):
    float_convert2=float(pp)
    pp=np.exp(float_convert2/100)/(float_convert2**10)
    total2=total2*pp
    partialprod2.append(total2)


partialprod3=[]
n=10000
product=1
for mm in range (0,n):
    float_convert1=float(mm)
    nn=(np.exp(float_convert1))**-1
    product=nn*product
    partialprod3.append(product)

print('The following set are the first 15 in Infinite Series, p_n')
up=np.array((partialprod[:15]))
print(up)
print("\n")

print('The following set are the last 15 in Infinite Series, p_n')
up1=np.array((partialprod[-15:]))
print(up1)
print("\n")
print('The following sets are the first 15 in Infinite Series, q_n')
down=np.array((partialprod2[:15]))
print(down)
print("\n")
print('The following sets are the last 15 in Infinite Series, q_n')
down1=np.array((partialprod2[-15:]))
print(down1)
print("\n")
print('The following sets are the first 15 in Infinite Series, 1/e^x')
middle=np.array((partialprod3[:15]))
print(middle)
print("\n")
print('The following sets are the last 15 in Infinite Series, 1/e^x')
middle1=np.array((partialprod3[-15:]))                 
print(middle1)
print("\n")


