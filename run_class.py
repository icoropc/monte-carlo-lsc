# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:57:15 2013

@author: Igor
"""

import photon_class
import sampler
from random import random
import concentrator_class
from math import log10
from math import pi
from math import acos
from math import cos
from math import sin
from random import random
from numpy import sign

class run:
    def __init__(self,concent):
        self.CurrentPhoton=photon_class.photon()
        self.concent=concent
    
    def isAbsorbed(self):
        zeta=random()
        if zeta<=self.concent.QuantumYield:
            return 1
        else:
            return 0
    
    def isReEmitted(self):
        zeta=random()
        if zeta<=self.concent.QuantumYield:
            return 1
        else:
            return 0
    
    def isStillInside(self, new_dir):
        if abs(new_dir[0][0])<self.concent.length & \
        abs(new_dir[1][0])<self.concent.width & \
        abs(new_dir[2][0])<self.concent.height:
            return 1
        else:
            return 0;
                
    
    def reachedEdge(self,new_dir):
        sep_x=(self.concent.length-abs(new_dir[0][0]))/new_dir[0][1]
        sep_y=(self.concent.width-abs(new_dir[1][0]))/new_dir[1][1] 
        sep_z=(self.concent.height-abs(new_dir[2][0]))/new_dir[2][1]
                 
        
    def UpdateDirection(self,OpticalDensity):
        #zeta is a pseudo-random variable uniformly distributed on (0,1)
        #calculate propagation distance based on optical density and zeta    
        g=0.00001
        zeta=random()       
        PropagationDistance=-1.0/(OpticalDensity*log10(zeta))
        zeta=random()
        phi=2*pi*random
        zeta=random()
        anisotropy=1/(2*g)*(1+g^2-((1-g^2)/(1+2*g*zeta-g^2))^2)
        theta=acos(sign(anisotropy)-anisotropy)
        #update direction consines
        self.dir_x=sin(theta)*cos(phi); 
        self.dir_y=sin(theta)*sin(phi); 
        self.dir_z=cos(theta)
        #calculate final coordiantes
        self.new_x=PropagationDistance*self.dir_x
        self.new_y=PropagationDistance*self.dir_y
        self.new_z=PropagationDistance*self.dir_z
        return [[self.new_x, self.dir_x],[self.new_y, self.dir_y],
                [self.new_z, self.dir_x]]
    
    def isLostTop(self):
        pass

    def propagate(self):
        NewDist=self.CurrentPhoton.propagate(self.concent.OpticalDensity)
        if self.isStillInside():
            return NewDist
        else: 
            pass

