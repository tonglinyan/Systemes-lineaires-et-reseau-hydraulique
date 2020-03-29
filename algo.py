import numpy as np
import copy

# Votre methode de resolution:
#  - Entree : A (matrice), b (vecteur)
#  - Sortie : sol (vecteur)
def solve(A,b):
	(n,p) = A.shape
	sol = b*0.0 
    # Completer ICI :
	L=np.eye(n)
	for i in range(n-1):
		for j in range(i+1,n):
			L[j,i]=A[j,i]/A[i,i]
			for k in range(i,n):
				A[j,k]=A[j,k]-L[j,i]*A[i,k]
	b=np.linalg.inv(L)@b
	sol=remontee(A,b)
	return sol


# Methode de Cramer
# - Entree : A,b
# - Sortie : x
def cramer(A,b):
	detA = det(A)
	x = b*0.0
	for i in range(len(b)):
		B = A*1.0
		B[:,i] = b 
        # Completer ICI :
		x[i] = det(B)/det(A)
	return x
    

# Calcul du determinant
# - Entree : A
# - Sortie : res    
def det(A):
	res = 0
	nn= len(A[:,0])
	if (nn == 1):
		return A[0,0]
    
	m1 = 1
	for j in range(nn):
		B = A[:,1:nn]
		B = B[[i for i in range(nn) if i != j],:]
		res = res + A[j,0]*m1*det(B)
        
		m1 = m1*(-1)
        
	return res
    
    
    
# Resolution de U x = b
#  - Entree : U (matrice), b (vecteur)
#  - Sortie : x (Vecteur)
def remontee(U,b):
	(n,p) = U.shape
	x = np.zeros(n)
	for l in range(n-1,-1,-1):
		x[l] = b[l]
		for c in range(l+1,n):
			x[l] = x[l] - U[l,c]*x[c]
		if (np.abs(U[l,l]) < 1e-10 ):  
			x[l] = 0.0
		else :
			x[l] = x[l] / U[l,l]
        
	return x
    
    
# Resolution de L x = b
#  - Entree : L (matrice), b (vecteur)
#  - Sortie : x (Vecteur)    
def descente(L,b):
	(n,p) = L.shape
	x = np.zeros(n)
	for l in range(n):
		x[l] = b[l]
		for c in range(l):
			x[l] = x[l] - L[l,c]*x[c]
		x[l] = x[l] / L[l,l]
    
	return x        
    
    

# Verification du Reseau
#  - Entree : listeNoeuds, listeArcs, listePression, Entree, Sortie  
#  - Sortie : Booleen
def verifReseau(listeNoeuds, listeArcs, listePression, Entree, Sortie):
    
	for aa in listeArcs:
		p1 = listeNoeuds[int(aa[0])]
		p2 = listeNoeuds[int(aa[1])]
		l1 = aa[2]
		l2 = aa[3]
        
		qq = listePression[int(aa[1])] - listePression[int(aa[0])]
		cc = 1.0
#		print(np.abs(qq),l2)
		if (np.abs(qq) > l2) :	
			return False
#	print(Sortie)
	for j,nn in enumerate(listeNoeuds):
		if ((not(j in Sortie)) and listePression[j] == 0):
#			print("pas d'eau")
			return False
    
	return True
    
