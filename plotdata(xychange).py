#!/usr/bin/env python3
import numpy as np
#import tables
import matplotlib.pyplot as plt
#import linecache
#import os

datax=[]
datay=[]

datax=np.loadtxt("datay.txt")
datay=np.loadtxt("datax.txt")
#datat=np.loadtxt("datat.txt")




lowlimitx=np.min(datax)
highlimitx=np.max(datax)
lowlimity=np.min(datay)
highlimity=np.max(datay)

fig = plt.figure()
ax = fig.add_subplot(111)

#plt.plot(datax,datay, color='red')
ax.plot(datax,datay, color='k')#linestyle=':'
ax.scatter(datax,datay, color='k')


"""
ax.text(1300, 1, r'm=4(a)', fontsize=fz)
ax.text(990, 350, r'm=4', fontsize=fz)
ax.text(850, 660, r'm=4(b)', fontsize=fz)
ax.text(850, 1350, r'm=4', fontsize=fz)
ax.text(980, 1700, r'm=5(c)', fontsize=fz)
ax.text(1000, 2050, r'm=6(d)', fontsize=fz)
ax.text(1150, 2400, r'm=7', fontsize=fz)
ax.text(1280, 2760, r'm=7(e)', fontsize=fz)
ax.text(480, 3150, r'm=3(f)', fontsize=fz)
ax.text(1, 3150, r'm=3', fontsize=fz)

ax.text(1300, 1, r'm=4', fontsize=fz)
ax.text(990, 350, r'm=4', fontsize=fz)
ax.text(850, 660, r'm=4', fontsize=fz)
ax.text(850, 1350, r'm=4', fontsize=fz)
ax.text(980, 1700, r'm=5', fontsize=fz)
ax.text(1000, 2050, r'm=6', fontsize=fz)
ax.text(1150, 2400, r'm=7', fontsize=fz)
ax.text(1280, 2760, r'm=7', fontsize=fz)
ax.text(480, 3150, r'm=3', fontsize=fz)
ax.text(1, 3150, r'm=3', fontsize=fz)
"""

#plt.text(160, 1300, r'"Stable"', fontsize=13)
#plt.text(1250, 1300, r'"Unstable"', fontsize=13)
#plt.text(200, 3700, r'"Unstable"', fontsize=13)


#plt.plot(datat,datay, color='k',linestyle=':',label="Transient solver")
#ax.axhline(y=0, color='k')
#ax.axvline(x=0, color='k')
fz=10
ax.set_aspect(aspect=0.5)
ax.set_ylim([0, 3000])
ax.set_xlim([0, 2000])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.text(1300, 1, r'm=4', fontsize=fz)
ax.text(990, 350, r'm=4', fontsize=fz)
ax.text(850, 660, r'm=4', fontsize=fz)
ax.text(850, 1350, r'm=4', fontsize=fz)
ax.text(980, 1700, r'm=5', fontsize=fz)
ax.text(1000, 2050, r'm=6', fontsize=fz)
ax.text(1150, 2400, r'm=7', fontsize=fz)
ax.text(1280, 2760, r'm=7', fontsize=fz)
ax.text(480, 3150, r'm=3', fontsize=fz)
ax.text(1, 3150, r'm=3', fontsize=fz)
#plt.xlim((0,4000))
#plt.ylim((0,1500))
#plt.ylabel('Velocity magnitute (x,0,0.0025) (m/s)')
#plt.xlabel('r (m)')
#print(x)
#print(y)
#ax.legend()
plt.show()
#np.savetxt('data1.txt', data)
