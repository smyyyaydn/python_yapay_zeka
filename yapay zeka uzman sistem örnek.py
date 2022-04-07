#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:26:53 2021

@author: smyyaydn
"""

from random import choice
from experta import *

class Dis(Fact):
    """Dişler ile ilgili bilgiler"""
    pass
class DisAgrisi(KnowledgeEngine):
    @Rule(Dis(belirti="Diş fırçalarken diş eti kanaması"))
    def kanama(self):
        print("Diş fırçalarken diş eti kanaması olduğu için, diş hastalığı vardır ve diş hekimine başvur")
    
    @Rule(Dis(belirti="Diş fırçalarken uzun süreli diş eti kanaması"))
    def uzun_kanama(self):
        print("Diş fırçalarken uzun süreli diş eti kanaması olduğu için, dişeti çekilmesi vardır ve diş hekimine başvur.")
   
    @Rule(Dis(belirti="Diş eti çekilmesi var ve diş kökü görünüyor"))
    def dis_eti(self):
        print("Diş eti çekilmesi var ve diş kökü görünüyor, dolgu yaptır")
    
    @Rule(Dis(belirti="Yeni diş çıkarken morarma görünüyor"))
    def morarma(self):
        print("Yeni diş çıkarken morarma görünüyor, diş hekimine başvur")
    
    @Rule(Dis(belirti="Dişte ağrı yapmayan çürük var"))
    def curuk(self):
        print("Dişte ağrı yapmayan çürük var, dolgu yaptır")
   
    @Rule(Dis(belirti="Dişteki çürük ileri derece"))
    def ileri_curuk(self):
        print("Dişte ileri derece çürük var, kanal tedavisi ve dolgu yaptır")
 
uzman= DisAgrisi()
uzman.reset()
uzman.declare(Dis(belirti=choice["Diş fırçalarken diş eti kanaması","Diş fırçalarken uzun süreli diş eti kanaması", "Diş eti çekilmesi var ve diş kökü görünüyor","Yeni diş çıkarken morarma görünüyor","Dişte ağrı yapmayan çürük var","Dişteki çürük ileri derece"]))
uzman.run()
    