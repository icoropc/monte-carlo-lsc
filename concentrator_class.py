# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:29:47 2013

@author: Igor
"""

from math import cos
from math import asin
import spectra

class concentrator:
    def __init__(self,tempgain):
        self.geometricGain=tempgain
        self.height=1
        self.width=self.geometricGain*4
        self.length=self.geometricGain*4
        self.RefrIndex=1.7
        self.CriticDir=cos(asin(1/self.RefrIndex))
        self.OpticalDensity=self.CalcOpticalDensity()
        self.QuantumYield=0.79

    def CalcOpticalDensity(self):
        abs_excitation=1/spectra.absor[405][1]*0.48
        new_density=[]
        for i in spectra.absor:
            pass
            new_density+=[i[1]*abs_excitation]
        return new_density
    