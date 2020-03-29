#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import affichage

import algo
import data

import random

"""
    Etude d'un reseau hydrolique 
"""

## Attention : Pour executer le programme, il faut utiliser python3 main.py

##----------------------------------
# But du programme :
# 1. Visualiser le reseau.
# 2. Resolution du probleme de reseau.
butPrgm = 1
print("Que souhaitez vous faire ?")
print(" 1. Visualiser le reseau.")
print(" 2. Resolution du probleme de reseau.")
print(" 3. Detection du reseau admissible.")
butPrgm = input("Entrer le choix : ")

print("")
##----------------------------------

##----------------------------------
nomData = ""
# Choix des donnees :
# 1. Reseau simple
# 2. Grand reseau
choixData = 1
print("Choix donnees ?")
print(" 1. Reseau simple")
print(" 2. Votre reseau.")
#print(" 3. Automatisation de la procedure.")
choixData = input("Entrer le choix : ")

print("")
##----------------------------------


##----------------------------------
# Visualiser les donnees :
if (butPrgm=="1"):
    listeNoeuds = []
    listeArcs = []
    # Recuperations des donnees :
    if (choixData =="1"):
        listeNoeuds = np.genfromtxt("reseauSimpleN.data", delimiter="\t")
        listeArcs = np.genfromtxt("reseauSimpleA.data", delimiter="\t")
    if (choixData =="2"):
        listeNoeuds = np.genfromtxt("reseauGrandN.data", delimiter="\t")
        listeArcs = np.genfromtxt("reseauGrandA.data", delimiter="\t")
        
    affichage.afficherReseau(listeNoeuds, listeArcs)    
##----------------------------------    
    
    
##----------------------------------
# Resolution du probleme de reseau :
if (butPrgm=="2"):
	listeNoeuds = []
	listeArcs = []
    # Recuperations des donnees :
	if (choixData =="1"):
		listeNoeuds = np.genfromtxt("reseauSimpleN.data", delimiter="\t")
		listeArcs = np.genfromtxt("reseauSimpleA.data", delimiter="\t")
	if (choixData =="2"):
		listeNoeuds = np.genfromtxt("reseauGrandN.data", delimiter="\t")
		listeArcs = np.genfromtxt("reseauGrandA.data", delimiter="\t")
            
	choixMeth = ""
    # Choix methode :
    # 1. Cramer
    # 2. Votre methode
	choixMeth = 1
	print("Choix donnees ?")
	print(" 1. Methode de Cramer")
	print(" 2. Votre methode.")
	choixMeth = input("Entrer le choix : ")

	print("")    
    
	listeVal = []
	valEntree = 10.0
	valSortie = 0.0
	listE = []
	listS = []
	listePression = []
	nbN = len(listeNoeuds)
    
	posE = 0
	posS = nbN-1
	[A,b] = data.generateMatriceReseau(listeNoeuds, listeArcs,  posE, valEntree, posS, valSortie)
	if (choixMeth == "1"):
		listePression = algo.cramer(A,b)
	if (choixMeth == "2"):
		listePression = algo.solve(A,b)
    
	listE = [posE]
	listS = [posS]    
	verif = algo.verifReseau(listeNoeuds, listeArcs, listePression, listE, listS)
	affichage.afficherReseauResultat(listeNoeuds, listeArcs, listePression, listE, listS)
##----------------------------------


##----------------------------------
# Detection dans le reseau de toute les positions de source et de sortie admissibles :

# Decommenter et completer ICI :
if (butPrgm=="3"):
	listeNoeuds = []
	listeArcs = []
    # Recuperations des donnees :
	if (choixData =="1"):
		listeNoeuds = np.genfromtxt("reseauSimpleN.data", delimiter="\t")
		listeArcs = np.genfromtxt("reseauSimpleA.data", delimiter="\t")
	if (choixData =="2"):
		listeNoeuds = np.genfromtxt("reseauGrandN.data", delimiter="\t")
		listeArcs = np.genfromtxt("reseauGrandA.data", delimiter="\t")
            
	choixMeth = ""
    # Choix methode :
    # 1. Cramer
    # 2. Votre methode
	choixMeth = 1
	print("Choix donnees ?")
	print(" 1. Methode de Cramer")
	print(" 2. Votre methode.")
	choixMeth = input("Entrer le choix : ")

	print("")    
    
	listeVal = []
	valEntree = 10.0
	valSortie = 0.0
	listE = []
	listS = []
	listePression = []
	nbN = len(listeNoeuds)
	for posE in range(nbN):
		for posS in range(nbN):
			if posE != posS:
				[A,b] = data.generateMatriceReseau(listeNoeuds, listeArcs,  posE, valEntree, posS, valSortie)
				if (choixMeth == "1"):
					listePression = algo.cramer(A,b)
				if (choixMeth == "2"):
					listePression = algo.solve(A,b)
				listE = [posE]
				listS = [posS]    
				verif = algo.verifReseau(listeNoeuds, listeArcs, listePression, listE, listS)
				if verif:
					print("Le couple entrée/sortie ",posE,"/", posS," engendre un réseau admissible")


##----------------------------------


print("FIN \n")
########################################
