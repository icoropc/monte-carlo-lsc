# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:46:59 2013

@author: Igor
"""
import numpy as np
import spectra


sum=0
for i in spectra.fluor:
    sum=sum+i[1]

wave_array=[]; probs=[]

for i in spectra.fluor:
    wave_array+=[int(i[0])]
    probs+=[i[1]/sum]


def EmissionSampler():    
    #samples the emission spectrum given as a NX2 array
    new_wavelength=np.random.choice(wave_array,1,p=probs)
    return new_wavelength[0]

