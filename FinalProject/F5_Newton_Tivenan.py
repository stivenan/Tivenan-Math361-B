#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:32:24 2019

@author: StephenTivenan
"""

import numpy as np
import matplotlib.pyplot as plt

f_z= lambda z:z**3-2*z**2-1
z_n= lambda z: 3*z**2-4*z
TOL=1E-4
x=2.2056 ## real solution, red
z=.66546 ## imaginary solution, green
n=-.66546 ## imaginary solution, blue
N=200
P=15
size=3
S=5



y0=np.linspace(-S,S,N)
x0=np.linspace(-S,S,N)



for jj in range (1,len(y0)):
    for ii in range (len(x0)):
        mm=complex(y0[jj],x0[ii])
        aa=mm.real
        bb=mm.imag
        plt.plot(aa,bb,'ko',markersize=size)
        for ll in range(P):
            b=mm-(f_z(mm)/z_n(mm))
            a=mm-b
            mm=b
            aa0=b.real
            bb0=b.imag
            if TOL>abs(a):
                aaa=b.real
                bbb=b.imag
                if (aaa-TOL)<x and x<(aaa+TOL):
                    plt.plot(aa,bb,'ro',markersize=size)
                if (bbb-TOL)<z.imag and z.imag<(bbb+TOL):
                    plt.plot(aa,bb,'go',markersize=size)
                if (bbb-TOL)<n.imag and n.imag<(bbb+TOL):
                    plt.plot(aa,bb,'bo',markersize=size)
                break

plt.show() 


