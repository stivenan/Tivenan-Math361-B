#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:07:17 2019

@author: StephenTivenan
"""
import matplotlib.pyplot as plt
import numpy as np
deg=3
P=15
N=10
x=2.2056
z=-.10278+.66546j
n=-.10278-.66546j
S=5
TOL=1E-4
f_z= lambda z:z**3-2*z**2-1
z_n= lambda z: 3*z**2-4*z
p_n= lambda z: 6*z-4
y0=np.linspace(-S,S,N)
x0=np.linspace(-S,S,N)

for jj in range (1,len(y0)):
    for ii in range (len(x0)):
        mm=complex(y0[jj],x0[ii])
        aa=mm.real
        bb=mm.imag
        plt.plot(aa,bb,'ko',markersize=3)
        for ll in range(P):
            st=f_z(mm)
            nd=z_n(mm)
            rd=p_n(mm)
            a=(nd/st)
            b=(rd/st)
            c=a**2-b
            d=(deg-1)*deg*c
            e=(deg-1)*a**2
            f=np.sqrt(d-e)
            g=a+f
            h=a-f
            if abs(g)<abs(h):
                p=h
            if abs(h)<abs(g):
                p=g
            lll=(deg)/p
            a=mm-lll
            mm=a
            aaa=a.real
            bbb=a.imag
            if (aaa-TOL)<x and x<(aaa+TOL):
                plt.plot(aa,bb,'ro',markersize=3)
            if (bbb-TOL)<z.imag and z.imag<(bbb+TOL):
                plt.plot(aa,bb,'go',markersize=3)
            if (bbb-TOL)<n.imag and n.imag<(bbb+TOL):
                plt.plot(aa,bb,'bo',markersize=3)
                break

plt.show()    
    
    
#abs(g.imag)<abs(h.imag) and abs(g.real)>abs(h.real)