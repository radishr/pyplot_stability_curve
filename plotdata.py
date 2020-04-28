#!/usr/bin/env python3
import numpy as np
import tables
import matplotlib.pyplot as plt
import linecache
import os
#plt.rc('text', usetex=True)  
#plt.rc('font', family='serif') 
datax=[]
datay=[]

datax=np.loadtxt("datax.txt")
datay=np.loadtxt("datay.txt")
m0x=np.loadtxt("m0x.txt")
m0y=np.loadtxt("m0y.txt")
m3x=np.loadtxt("m3x.txt")
m3y=np.loadtxt("m3y.txt")
m4x=np.loadtxt("m4x.txt")
m4y=np.loadtxt("m4y.txt")
m5x=np.loadtxt("m5x.txt")
m5y=np.loadtxt("m5y.txt")
m6x=np.loadtxt("m6x.txt")
m6y=np.loadtxt("m6y.txt")
m7x=np.loadtxt("m7x.txt")
m7y=np.loadtxt("m7y.txt")
#datat=np.loadtxt("datat.txt")




lowlimitx=np.min(datax)
highlimitx=np.max(datax)
lowlimity=np.min(datay)
highlimity=np.max(datay)

fig = plt.figure()
ax = fig.add_subplot(111)

#plt.plot(datax,datay, color='red')
ax.plot(datax,datay, color='k',linestyle='--')#linestyle=':'
ax.scatter(datax,datay, label="LSA",  marker=".", color="k", s=50)


#STABILITY CURVE
ax.scatter(m0x,m0y, label="m=0", marker="o", facecolors='none', color="black", s=20)
ax.scatter(m3x,m3y, label="m=3", marker="^", color="cyan", s=30)
ax.scatter(m4x,m4y, label="m=4", marker="s", color="red", s=25)
ax.scatter(m5x,m5y, label="m=5", marker="p", color="blue", s=60)
ax.scatter(m6x,m6y, label="m=6", marker="h", color="green", s=60)
ax.scatter(m7x,m7y, label="m=7", marker="*", color="magenta", s=40)
mz=20
"""
ax.scatter(0,1285, s=mz, color="black")
ax.scatter(700,778, s=mz, color="black")
ax.scatter(1750,928, s=mz, color="black")
ax.scatter(2100,1000, s=mz, color="black")
ax.scatter(2800,1220, s=mz, color="black")
ax.scatter(2926,500, s=mz, color="black")
#STABILITY CURVE
"""
"""
plt.scatter(357,3150, color='k',marker='x')
plt.text(348, 2900, r'a', fontsize=12)
plt.scatter(357,3500, color='k',marker='x')
plt.text(348, 3600, r'b', fontsize=12)
plt.scatter(714,2450, color='k',marker='x')
plt.text(706, 2150, r'c', fontsize=12)
plt.scatter(714,3150, color='k',marker='x')
plt.text(706, 3250, r'd', fontsize=12)
plt.scatter(714,350, color='k',marker='x')
plt.text(706, 450, r'e', fontsize=12)
plt.scatter(790,350, color='k',marker='x')
plt.text(786, 450, r'f', fontsize=12)
"""
"""
fz=14
ax.text(0, 1250, r'm=4', fontsize=fz)
ax.text(400, 920, r'm=4', fontsize=fz)
ax.text(500, 730, r'm=4', fontsize=fz)
ax.text(820, 620, r'm=4', fontsize=fz)
ax.text(1200, 740, r'm=4', fontsize=fz)
ax.text(1500, 940, r'm=5', fontsize=fz)
ax.text(1920, 860, r'm=6', fontsize=fz)
ax.text(2040, 1070, r'm=7', fontsize=fz)
ax.text(2650, 1250, r'm=7', fontsize=fz)
ax.text(2980, 1140, r'm=3', fontsize=fz)
ax.text(2980, 980, r'm=3', fontsize=fz)
ax.text(2980, 840, r'm=3', fontsize=fz)
ax.text(3020, 620, r'm=3', fontsize=fz)
ax.text(3050, 480, r'm=3', fontsize=fz)
ax.text(3050, 330, r'm=3', fontsize=fz)
ax.text(3050, 1, r'm=3', fontsize=fz)

ax.text(650, 270, r'"Stable axisymmetric"', fontsize=14, color='r')
ax.text(3500, 900, r'"Unstable"', fontsize=14, color='r')
ax.text(900, 1100, r'"Unstable"', fontsize=14, color='r')
"""
"""
#STABILITY CURVE
fz=14
ax.text(30, 1255, r'(a)', fontsize=fz)
ax.text(720, 800, r'(b)', fontsize=fz)
ax.text(1650, 970, r'(c)', fontsize=fz)
ax.text(2100, 920, r'(d)', fontsize=fz)
ax.text(2850, 1200, r'(e)', fontsize=fz)
ax.text(2900, 550, r'(f)', fontsize=fz)
#STABILITY CURVE
"""
fz=14
ax.text(2850, 1200, r'(e)', fontsize=fz)
plt.rc('xtick', labelsize=14) 
plt.rc('ytick', labelsize=14) 
#plt.plot(datat,datay, color='k',linestyle=':',label="Transient solver")
#ax.axhline(y=0, color='k')
#ax.axvline(x=0, color='k')
#ax.set_aspect(aspect=1)
ax.set_xlim([2000, 4500])
ax.set_ylim([800, 1350])
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)
#plt.xlim((0,4000))
#plt.ylim((0,1500))
plt.ylabel('Ma$_C$', fontsize=14)
plt.xlabel('Ma$_T$', fontsize=14)
#print(x)
#print(y)
#ax.legend()
plt.rc('legend', fontsize=13,loc="upper right") 
#plt.ylabel('Frequency', fontsize=14)
#plt.xlabel('Growth rate ( $\lambda$ )', fontsize=14)
plt.legend()
plt.show()
#np.savetxt('data1.txt', data)
