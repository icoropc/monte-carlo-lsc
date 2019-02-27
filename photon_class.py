# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:29:08 2013

@author: Igor

"""
import sampler
from math import log10
from math import pi
from math import acos
from math import cos
from math import sin
from random import random
from numpy import sign

class new_photon:
    #Define photon with each isntance having the 3D positions, directions, and 
    #wavelength as its parameters    
    def __init__(self,concentrator):
        self.concent=concentrator
        self.pos_x=0;
        self.pos_y=0;
        self.pos_z=0;
        self.new_x=0
        self.new_y=0
        self.new_z=0
        self.wavelength=405;
        self.dir_x=0
        self.dir_y=0
        self.dir_z=0
        self.freepath=0
        self.NoEvent=False

    def InitialDepth(self):
        zeta=random()       
        self.freepath=-1.0/(self.concent.OpticalDensity[405])*log10(zeta)
        if self.freepath<=self.concent.height:
            self.pos_z=self.concent.height/2-self.freepath
        else:
            self.pos_z=self.freepath-self.concent.height
            
    def isReflected(self):
        temp=random()
        if temp<=.933:
            return 0
        else:
            return 1
        
    def isAbsorbed(self):
        if self.freepath<=self.concent.height:
            return 1
        else:
            return 0
    
    def isReEmitted(self):
        zeta=random()
        if zeta<=self.concent.QuantumYield:
            return 1
        else:
            return 0
            
            
    def ReEmit(self):
        self.wavelength=sampler.EmissionSampler()

        #zeta is a pseudo-random variable uniformly distributed on (0,1)
        #calculate propagation distance based on optical density and zeta    
        g=0.000001
        zeta=random()       
        self.freepath=-1.0/(self.concent.OpticalDensity[self.wavelength])*log10(zeta)
        zeta=random()
        phi=2*pi*random()
        zeta=random()
        anisotropy=1/(2*g)*(1+g**2-((1-g**2)/(1+2*g*zeta-g**2))**2)
        theta=acos(sign(anisotropy)-anisotropy)
        #update direction consines
        self.dir_x=sin(theta)*cos(phi); 
        self.dir_y=sin(theta)*sin(phi); 
        self.dir_z=cos(theta)
    
    def GetNewPositions(self):
                #calculate final coordiantes
        self.new_x=self.pos_x+self.freepath*self.dir_x
        self.new_y=self.pos_y+self.freepath*self.dir_y
        self.new_z=self.pos_z+self.freepath*self.dir_z
        self.sep_x=abs((self.concent.length/2*sign(self.dir_x)-self.pos_x)/self.dir_x)
        self.sep_y=abs((self.concent.width/2*sign(self.dir_y)-self.pos_y)/self.dir_y)
        self.sep_z=abs((self.concent.height/2*sign(self.dir_z)-self.pos_z)/self.dir_z)
    
    def UpdatePosition(self):
        self.pos_x=self.new_x
        self.pos_y=self.new_y
        self.pos_z=self.new_z
    
    def isStillInside(self):
        if abs(self.new_x)<=self.concent.length/2 and \
        abs(self.new_y)<=self.concent.width/2 and \
        abs(self.new_z)<=self.concent.height/2:
            return 1
        else:
            return 0;
    
    def isCollected(self):
        if (abs(self.new_x)>=self.concent.length/2 and \
        self.sep_x<=self.sep_z) or \
        (abs(self.new_y)>=self.concent.width/2 and \
         self.sep_y<=self.sep_z):
            return True
        else:
            return False
    
    def isLostTop(self):
        if self.sep_z<self.sep_x and self.sep_z<self.sep_y:
            if abs(self.dir_z)>self.concent.CriticDir:
                return True
            else:
                return False
        else:
            return False

    def UpdateReflection(self):        
        if self.sep_z<self.sep_x and self.sep_z<self.sep_y and self.new_z>0:
            self.dir_z=self.dir_z*-1
            self.pos_z=self.concent.height/2
            self.pos_x+=self.sep_z*self.dir_x
            self.pos_y+=self.sep_z*self.dir_y
            self.freepath=self.freepath-self.sep_z
        elif self.sep_z<self.sep_x and self.sep_z<self.sep_y and self.new_z<0:
            self.dir_z=self.dir_z*-1
            self.pos_z=-self.concent.height/2
            self.pos_x+=self.sep_z*self.dir_x
            self.pos_y+=self.sep_z*self.dir_y
            self.freepath=self.freepath-self.sep_z
        else:
            print(no)
        
