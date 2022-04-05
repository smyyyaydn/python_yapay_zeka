#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:09:30 2021

@author: smyyaydn
"""
import random
import math
import numpy as np
def net(G1,Ai11,G2,Ai21,Ba1):
    return(G1*Ai11+G2*Ai21+1*Ba1)

ogr=0.5
mom=0.8
sse=0.03
Girdiler1=[0,0,1,1]
Girdiler2=[0,1,0,1]
Ciktilar=[0,1,1,0]
Ai=[[0 for x in range(2)] for y in range(2)]
Aa=[]
Ba=[]
NAi,NBa,NAa=[],[],[]
Bc=random.uniform(-1,1)
for x in range(0,2):
    for i in range(0,2):
        Ai[x][i]=(random.uniform(-1,1))
    Aa.append(random.uniform(-1,1))
    Ba.append(random.uniform(-1,1))


net1=net(Girdiler1[0],Ai[0][0],Girdiler2[0],Ai[1][0],Ba[0])
net2=net(Girdiler1[0],Ai[0][1],Girdiler2[0],Ai[1][1],Ba[1])
C1=1/(1+(math.exp(-(net1))))
C2=1/(1+(math.exp(-(net2))))

Netcikti=net(C1,Aa[0],C2,Aa[1],Bc)
CCikti=1/(1+(math.exp(-(Netcikti))))
E=Ciktilar[0]-CCikti
while E>sse:
    S1=CCikti*(1-CCikti)*E
    NAa[0]=ogr*S1*C1+mom*Ciktilar[0]
    NAa[1]=ogr*S1*C2+mom*Ciktilar[0]
    NBc=ogr*S1
    NAa[0]=Aa[0]-NAa[0]
    NAa[1]=Aa[1]-NAa[1]
    NBc=Bc-NBc
    
    Sa1=C1*(1-C1)*S1*Aa[0]
    Sa2=C2*(1-C2)*S1*Aa[1]
    
    NAi[0][0]=ogr*Sa1*Girdiler1[0]+mom*Ciktilar[0]
    NAi[0][1]=ogr*Sa1*Girdiler1[0]+mom*Ciktilar[0]
    NAi[1][0]=ogr*Sa1*Girdiler1[0]+mom*Ciktilar[0]
    NAi[1][1]=ogr*Sa1*Girdiler1[0]+mom*Ciktilar[0]
    NBa[0]=ogr*1*Sa1
    NBa[1]=ogr*1*Sa2
    
    if NAa==np.zeros((2,2)):
        NBa[0]=Ba[0]-NBa[0]
        NBa[1]=Ba[1]-NBa[1]
    
Nnet1=net(Girdiler1[0],Ai[0][0],Girdiler2[0],Ai[1][0],Ba[0])
Nnet2=net(Girdiler1[0],Ai[0][1],Girdiler2[0],Ai[1][1],Ba[1])
NC1=1/(1+(math.exp(-(net1))))
NC2=1/(1+(math.exp(-(net2))))

NNetcikti=net(C1,Aa[0],C2,Aa[1],Bc)
NCCikti=1/(1+(math.exp(-(Netcikti))))
NE=Ciktilar[0]-CCikti
print(NE)