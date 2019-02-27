# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:29:08 2013

@author: Igor
"""
from math import log
from random import random

class pphoton:
    #Define photon with each isntance having the 3D positions, directions, and wavelength as its parameters    
    def __init__(self):
        self.pos_x=0;
        self.pos_y=0;
        self.pos_z=0;
        self.dir_x=0;
        self.dir_y=0;
        self.dir_z=0;
        self.wavelength=0;
        
    def UpdatePos(self):
        self.pos_x=1;
        self.pos_y=1;
        self.pos_z=1;
        
    def propagate(self,OpticalDensity):
       
        #zeta is a pseudo-random variable uniformly distributed on (0,1)
        #calculate propagation distance based on optical density and zeta    
        zeta=random()       
        PropagationDistance=-1.0/(OpticalDensity*log(zeta))
        return PropagationDistance