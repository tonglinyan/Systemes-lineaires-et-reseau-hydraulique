import numpy as np
from random import random 
    

# Generation de la matrice correspondant au reseau considere :
#  - Entree : listeNoeuds (liste), listeArcs (liste), e (entier), E (double), s (entier), S (double)
#  - Sortie : A (matrice), b (vecteur)
def generateMatriceReseau(listeNoeuds, listeArcs, e, E, s, S):
	n = len(listeNoeuds)
	A = np.zeros((n,n))
	b = np.zeros(n)
    
    # Premiere partie : Construction de A
	for aa in listeArcs:
		p1 = int(aa[0])
		p2 = int(aa[1])
		ll = aa[2]
        
		A[p1,p1] = A[p1,p1] + ll
		A[p2,p2] = A[p2,p2] + ll
		A[p1,p2] = A[p1,p2] - ll
		A[p2,p1] = A[p2,p1] - ll
    
    
    # Methode d'elimination : 
    # Choix 1 :
    # Initialisation : (decommenter les lignes)
	tA = A*1.0
	tb = b*1.0
    # Completer ICI :

	for k in range (n):
		tA[e,k]=0
		tA[s,k]=0
	tA[e,e]=1
	tA[s,s]=1
	tb[e]=E
	tb[s]=S 


    # Choix 2 :
    # Initialisation : (decommenter les lignes)
#	tA = A*1.0
#	tb = b*1.0
    #Completer ICI :

#	for k in range (n):
#		tA[e,k]=0
#		tA[s,k]=0
#		tb[k]=tb[k]-tA[k,e]*E
#		tb[k]=tb[k]-tA[k,s]*S
#		tA[k,e]=0
#		tA[k,s]=0
#	tA[e,e]=1
#	tA[s,s]=1
#	tb[e]=E
#	tb[s]=S 

	return [tA,tb]
        
