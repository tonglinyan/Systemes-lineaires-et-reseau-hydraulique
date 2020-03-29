#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np

#import random



"""
    Generateur de reseau aleatoire
"""

## Attention : Pour executer le programme, il faut utiliser python3 genReseau.py
listeNoeuds = []
listeArcs = []

# Parametre du reseau :
nn = 7
h = 0.5
ccr = 1.6

for j in range(nn):
    yy = j*h
    for i in range(nn):
        xx = i*h
        listeNoeuds.append([xx,yy])
        
        if ((i < nn-1) and (j < nn-1)):
            ind = j*nn + i
            indP = j*nn + i + 1
            indPP = (j + 1)*nn + i
            indPPP = (j+1)*nn + i + 1
            
            n1 = np.random.random()
            n2 = np.random.random()
            n3 = np.random.random()
            if(n1 > 0.5):
                listeArcs.append([int(ind),int(indP),1.0,ccr+np.random.random()])
            else:
                listeArcs.append([int(ind),int(indPP),1.0,ccr+np.random.random()])
            if(n2 > 0.5):
                listeArcs.append([int(ind),int(indPPP),1.0,ccr+np.random.random()])
            else:
                listeArcs.append([int(indP),int(indPP),1.0,ccr+np.random.random()])
                
        if ((j==nn-1) and (i < nn-1)):
            ind = j*nn + i
            indP = j*nn + i + 1
            
            listeArcs.append([int(ind),int(indP),1.0,ccr+np.random.random()])
            
        if ((i==nn-1) and (j < nn-1)):
            ind = j*nn + i
            indPP = (j+1)*nn + i
            
            listeArcs.append([int(ind),int(indPP),1.0,ccr+np.random.random()])
            
np.savetxt('reseauGrandN.data',listeNoeuds,delimiter='\t')
np.savetxt('reseauGrandA.data',listeArcs,delimiter='\t')            