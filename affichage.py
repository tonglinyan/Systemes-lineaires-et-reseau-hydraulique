#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import data

from pylab import *        
        
        
        
def afficherReseauResultat(listeNoeuds, listeArcs, listePression, Entree, Sortie):
    
    theta = np.arange(0.0,2*np.pi,0.01)
    rb = 0.1
    xb = rb * np.cos(theta)
    yb = rb * np.sin(theta)
    
    for aa in listeArcs :
        p1 = listeNoeuds[int(aa[0])]
        p2 = listeNoeuds[int(aa[1])]
        l1 = aa[2]
        l2 = aa[3]
        
        qq = listePression[int(aa[1])] - listePression[int(aa[0])]
        cc = 1.0
        if (np.abs(qq) > l2) :
            if (qq < 0):
                plt.arrow(p1[0],p1[1],(p2[0]-p1[0])*cc,(p2[1]-p1[1])*cc,color='red',width=0.01,head_width=0.1,length_includes_head=True)
            if (qq > 0) :
                plt.arrow(p2[0],p2[1],(p1[0]-p2[0])*cc,(p1[1]-p2[1])*cc,color='red',width=0.01,head_width=0.1,length_includes_head=True)
            if (qq == 0):
                plt.arrow(p2[0],p2[1],(p1[0]-p2[0])*cc,(p1[1]-p2[1])*cc,color='red',width=0.01,head_width=0.1,length_includes_head=True)
                    
            plt.text(p1[0],p1[1]+0.2,round(listePression[int(aa[0])],2) )
            plt.text(p2[0],p2[1]+0.2,round(listePression[int(aa[1])],2) )
        else :
            if (qq < 0):
                plt.arrow(p1[0],p1[1],(p2[0]-p1[0])*cc,(p2[1]-p1[1])*cc,color='blue',width=0.01,head_width=0.1,length_includes_head=True)
            if (qq > 0):
                plt.arrow(p2[0],p2[1],(p1[0]-p2[0])*cc,(p1[1]-p2[1])*cc,color='blue',width=0.01,head_width=0.1,length_includes_head=True)
            if (qq == 0):
                plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'b-')
                #plt.arrow(p2[0],p2[1],(p1[0]-p2[0])*cc,(p1[1]-p2[1])*cc,color='blue',width=0.01,head_width=0.1,length_includes_head=True)
                
            plt.text(p1[0],p1[1]+0.2,round(listePression[int(aa[0])],2) )
            plt.text(p2[0],p2[1]+0.2,round(listePression[int(aa[1])],2) )
            
            
    for nn in listeNoeuds :
        plt.plot(xb+nn[0],yb+nn[1],'k-')
        
    for e in Entree:
        for iii in range(10):
            plt.plot(xb*(iii+1)*0.1+(listeNoeuds[e])[0],yb*(iii+1)*0.1+(listeNoeuds[e])[1],'r-')
        
    for s in Sortie:
        for iii in range(10):
            plt.plot(xb*(iii+1)*0.1+(listeNoeuds[s])[0],yb*(iii+1)*0.1+(listeNoeuds[s])[1],'g-')
                
    plt.axis('equal')
    plt.show()
    
    
def afficherReseau(listeNoeuds, listeArcs):
    
    theta = np.arange(0.0,2*np.pi,0.01)
    rb = 0.1
    xb = rb * np.cos(theta)
    yb = rb * np.sin(theta)
    
    for aa in listeArcs :
        p1 = listeNoeuds[int(aa[0])]
        p2 = listeNoeuds[int(aa[1])]
        l1 = aa[2]
        l2 = aa[3]
        plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'k-')
            
    for nn in listeNoeuds :
        plt.plot(xb+nn[0],yb+nn[1],'k-')
                
    plt.axis('equal')
    plt.show()