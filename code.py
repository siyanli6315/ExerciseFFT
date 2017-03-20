#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

dat=[s for s in open("Data.txt").readlines()]
dat=[s.strip() for s in dat]
for i in range(len(dat)):
    if dat[i]=="Data_y:":
        print i

y=[float(s) for s in dat[162:]]
n=len(y)

plt.figure(figsize=(8,5))
plt.plot(range(n),y,lw=1.5,color="black")
plt.xlim(0,160)
plt.ylim(-3,3)
plt.savefig("fig0.png")

y_fft = np.fft.fft(y)
y_fft=y_fft[:(n/2+1)]
real=y_fft.real/(n/2)
imag=-y_fft.imag/(n/2)

#使用所有的分量进行拟合
##$y_i=\sum_{k=1}^{n/2}(\frac{ReX[k]}{n/2}cos(2\pi ki/n)+(-\frac{ImX[k]}{n/2})sin(2\pi ki/n))$
y_hat=[]
for i in range(n):
    tmp=np.sum(real[k]*np.cos(2*np.pi*k*i/n)+imag[k]*np.sin(2*np.pi*k*i/n) for k in range(n/2+1))
    y_hat.append(tmp)

plt.figure(figsize=(8,5))
plt.subplots_adjust(hspace=0)
plt.subplot(211)
plt.plot(range(n),y,lw=1.5,color="blue",label="$y$")
plt.xlim(0,160)
plt.ylim(-3,5)
plt.legend()
plt.subplot(212)
plt.plot(range(n),y_hat,lw=1.5,color="red",label="$\hat{y}$")
plt.xlim(0,160)
plt.ylim(-3,5)
plt.legend()
plt.savefig("fig1.png")

#使用最大的三个分量进行拟合
mod=[]
for i in range(len(real)):
    tmp=real[i]**2+imag[i]**2
    mod.append(tmp)

plt.figure(figsize=(8,5))
plt.plot(range(len(mod)),mod,lw=1.5,color="black",label="$mod$")
plt.xlim(0,20)
plt.savefig("fig2.png")

top3=np.argsort(-np.array(mod))[:3]
def myfun(k):
    curve=[real[k]*np.cos(2*np.pi*k*i/n)+imag[k]*np.sin(2*np.pi*k*i/n) for i in range(n)]
    return curve

[curve1,curve2,curve3]=[myfun(k) for k in top3]
curve=[curve1[i]+curve2[i]+curve3[i] for i in range(n)]
plt.figure(figsize=(8,5))
plt.subplots_adjust(hspace=0)
plt.subplot(211)
plt.plot(range(n),y,lw=1.5,color="black",label="$y$")
plt.plot(range(n),curve1,lw=1,color="red",label="$\hat{y}_1$")
plt.plot(range(n),curve2,lw=1,color="blue",label="$\hat{y}_2$")
plt.plot(range(n),curve3,lw=1,color="green",label="$\hat{y}_3$")
plt.xlim(0,190)
plt.ylim(-3,3)
plt.legend()
plt.subplot(212)
plt.plot(range(n),y,lw=1.5,color="black",label="$y$")
plt.plot(range(n),curve,lw=1.5,color="red",label="$\hat{y}$")
plt.xlim(0,190)
plt.ylim(-3,3)
plt.legend()
plt.savefig("fig3.png")
