# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:13:15 2013

@author: Igor
"""
import numpy as np

absor_prov=np.loadtxt('abs.txt')
fluor_prov=np.loadtxt('fl.txt')

prov=int(absor_prov[0][0])
absor_p=[0,0]
for i in range(1,prov):
    absor_p=np.vstack((absor_p,[i,0.0]))
absor=np.vstack((absor_p,absor_prov))

prov=int(fluor_prov[0][0])
fluor_p=[0,0]
for i in range(1,prov):
    fluor_p=np.vstack((fluor_p,[i,0.0]))
fluor=np.vstack((fluor_p,fluor_prov))