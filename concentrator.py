# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:29:47 2013

@author: Igor
"""

class pconcentrator:
    def __init__(self):
        self.height=1;
        self.width=4;
        self.length=4;
        self.RefrIndex=1.5;
        self.OpticalDensity=1.0;
        self.QuantumYield=0.9;
    def SetDimensions(self,new_height,new_width,new_length):
        self.height=new_height
        self.width=new_width
        self.length=new_length

    