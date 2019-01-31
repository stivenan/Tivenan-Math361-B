#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:56:22 2019

@author: StephenTivenan
"""
emptylist2=[]
x=55 ##Input variable x
y=30 ##Input variable y
z=100 ##Input variable z
##Start of operations

##Operation1
a=x+y
emptylist2.append(a)

##Operation2
b=(y*z)+3*x
emptylist2.append(b)

##Operation3
c=a**2
emptylist2.append(c)

##Operation4
d=(2*y-((.5)*x))/a
emptylist2.append(d)

##Operation5
e=7%3
emptylist2.append(e)

print(emptylist2)
print('This is the Original Set without Modifications')

emptylist2[2]=emptylist2[2]+3
print('This is the 3rd element +3')

print(emptylist2[2])
print('This is the Set with Modifications')

print(emptylist2)
emptylist2[4]=emptylist2[4]*(3/4)
print('This is the 5th element multiplied 3/4')
print(emptylist2[4])

print(emptylist2)
print('This is the Set with Modifications')

print(emptylist2[0]+emptylist2[1]+emptylist2[2]+emptylist2[3]+emptylist2[4])
print('This is the Sum of the Set')
