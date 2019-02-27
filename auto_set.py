# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:05:37 2015

@author: Igor
"""

import main

efficiency_list=[]

gains_list=[1,2,3,4,5,7,10,15,20,50,100,150,200,250,300,350,400]
for geometric_gain in gains_list:
    efficiency=main.mainf(geometric_gain)
    efficiency_list+=[efficiency]

print(efficiency_list)