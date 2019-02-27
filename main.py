# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:28:30 2013

@author: Igor
"""
import concentrator_class
import photon_class


def mainf(tempgain):
    MaxPhoton=50000
    global TotalPhoton, NotAbsorbed, NotEmitted, LostTop, PhotonCollected, Reflected
    TotalPhoton=PhotonCollected=NotAbsorbed=NotEmitted=LostTop=Reflected=0
    concent=concentrator_class.concentrator(tempgain)

    
    global wll
    wll=[]
        
    
    while PhotonCollected<MaxPhoton:
        photon=photon_class.new_photon(concent)
        TotalPhoton+=1
        photon.InitialDepth()
        if photon.isReflected()==1:
            Reflected+=1
        elif photon.isAbsorbed()==0:
            NotAbsorbed+=1
        else:
            collected=False; lost=False;
            while collected==False and lost==False:                 
                 if photon.isReEmitted()==0:
                    NotEmitted+=1; lost=True;
                 else: 
                     photon.ReEmit()
                     wll+=[photon.freepath]
                     finish=False
                     while collected==False and lost==False and finish==False:
                         photon.GetNewPositions()
                         if photon.isStillInside():
                            photon.UpdatePosition()
                            finish=True;
                         elif photon.isCollected():
                             PhotonCollected+=1; collected=True; 
                         elif photon.isLostTop():
                             LostTop+=1; lost=True         
                         else:
                             photon.UpdateReflection();
                             if photon.NoEvent==True:
                                 return 0

    
                             
    print("Collected", PhotonCollected/TotalPhoton)
    print("Reflected", Reflected/TotalPhoton)
    print("Not Absorbed",NotAbsorbed/TotalPhoton)
    print("Not Re-emitted",NotEmitted/TotalPhoton)
    print("Lost Top", LostTop/TotalPhoton)
    return PhotonCollected/TotalPhoton
        
mainf(2)
    
   

