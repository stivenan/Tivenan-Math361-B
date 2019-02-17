#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:15:44 2019

@author: StephenTivenan
"""
import matplotlib.pyplot as plt
import numpy as np
N=20
i=-3.
p=[]
def function2(x):
    if(x< -2):
        plt.ylim([-10, 10])
        plt.xlim([-3,3])
        x = np.linspace(-3.,-1.99, N)
        plt.plot(x,-3*((x+2)**2)+1)
        plt.show()
        return 
    elif(-2<=x<-1):
        x = np.linspace(-2., -.99, N)
        plt.ylim([-10,10])
        plt.xlim([-3,3])
        plt.plot(x,x==1)
        plt.show() 
        return 
    elif (-1<=x<=1):
        x = np.linspace(-1., 1., N)
        plt.ylim([-10,10])
        plt.xlim([-3,3])
        plt.plot(x,(x-1)**3+3)
        plt.show() 
        return 
    elif (1<x<2):
        x = np.linspace(1., 2, N)
        plt.ylim([-10,10])
        plt.xlim([-3,3])
        plt.plot(x,(np.sin(np.pi*x)+3))
        plt.show()
        return 
    elif (2<=x):
        x = np.linspace(2., 3., N)
        plt.ylim([-10,10])
        plt.xlim([-3,3])
        plt.plot(x,3*(x-2)**(1/2)+4)
        plt.show()
while i < 3:
    
    m=function2(i)
    p.append(m)
    if i==3:
        break 
    i+=.5
plt.plot(p)




