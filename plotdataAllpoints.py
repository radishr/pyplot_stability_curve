#!/usr/bin/env python3
import numpy as np
import tables
import matplotlib.pyplot as plt
import linecache
import os

datax=[]
datay=[]

datax=np.loadtxt("datax.txt")
datay=np.loadtxt("datay.txt")
stblx=np.loadtxt("stblx.txt")
stbly=np.loadtxt("stbly.txt")
unstblx=np.loadtxt("unstblx.txt")
unstbly=np.loadtxt("unstbly.txt")
#datat=np.loadtxt("datat.txt")




lowlimitx=np.min(datax)
highlimitx=np.max(datax)
lowlimity=np.min(datay)
highlimity=np.max(datay)

fig = plt.figure()
ax = fig.add_subplot(111)

#plt.plot(datax,datay, color='red')
ax.plot(datax,datay, color='k')#linestyle=':'
#ax.scatter(datax,datay, marker=".", color="black", s=100)
ax.scatter(stblx,stbly, marker="o", facecolors='none', edgecolors='black', color="black", s=20)
ax.scatter(unstblx,unstbly, marker=".", color="black", s=20)
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
ax.text(2980, 840, r'm=3', fontsize=fz)
ax.text(3020, 620, r'm=3', fontsize=fz)
ax.text(3050, 480, r'm=3', fontsize=fz)
ax.text(3050, 330, r'm=3', fontsize=fz)
ax.text(3050, 1, r'm=3', fontsize=fz)
"""
#ax.text(800, 270, r'"Stable axisymmetric"', fontsize=14)
#ax.text(3000, 900, r'"Unstable"', fontsize=14)
#ax.text(900, 1100, r'"Unstable"', fontsize=14)

plt.rc('xtick', labelsize=12) 
plt.rc('ytick', labelsize=12) 
#plt.plot(datat,datay, color='k',linestyle=':',label="Transient solver")
#ax.axhline(y=0, color='k')
#ax.axvline(x=0, color='k')
#ax.set_aspect(aspect=1)
ax.set_xlim([0, 4000])
ax.set_ylim([0, 1350])
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)
#plt.xlim((0,4000))
#plt.ylim((0,1500))
#plt.ylabel('Velocity magnitute (x,0,0.0025) (m/s)')
#plt.xlabel('r (m)')
#print(x)
#print(y)
#ax.legend()
plt.show()
#np.savetxt('data1.txt', data)
