import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
liste = []
premLois = []
deuxLois = []
troiLois = []
PXsachN1 = []
PXsachN2 = []
PXsachN3 = []
PN1sachX = []
PN2sachX = []
PN3sachX = []
Erreur1 = []
Erreur2 = []
Erreur3 = []
data = []

#  =LOI.NORMALE  
#  =LOI.NORMALE.INVERSE(A14;1,5;0,01)
# On doit chercher l'equivalent de ces 2 lois en python !

i=0
while i < 7:
    liste.append(np.random.random())
    i=i+1
    continue

i=0
while i < 7:
    premLois.append(stats.norm.ppf(liste[i], loc=1.5, scale= 0.01))
    i=i+1
    continue
    
i=0
while i < 6:
    deuxLois.append(stats.norm.ppf(liste[i], loc=1.7, scale= 0.01))
    i=i+1
    continue
i=0
while i < 3:
    troiLois.append(stats.norm.ppf(liste[i], loc=1.9, scale= 0.01))
    i=i+1
    continue

data=premLois+deuxLois+troiLois

# loi1(1.6,0.1) loi2(1.7,0.3) loi3(1.8,0.2) suposition !  ph1=1/3 phi2=1/3 phi3=1/3
Mu1=1.6 
Sig1=0.1
Mu2=1.7 
Sig2=0.3 
Mu3=1.8 
Sig3=0.2  
phi1=0.33333333
phi2=0.33333333
phi3=0.33333333


j=0
while j < 10:    
#P X/N   
    # prob X/N1
    
    i=0
    while i < 16:
        PXsachN1.append(float(stats.norm.cdf(data[i], loc=Mu1, scale= Sig1)))
        i=i+1
        continue

        # prob X/N2
    i=0
    while i < 16:
        PXsachN2.append(float(stats.norm.cdf(data[i], loc=Mu2, scale= Sig2)))
        i=i+1
        continue

        # prob X/N3
    i=0
    while i < 16:
        PXsachN3.append(float((stats.norm.cdf(data[i], loc=Mu3, scale= Sig3))))
        i=i+1
        continue
    #P N/X

        # prob N1/X
    i=0
    while i < 16:
        PN1sachX.append(PXsachN1[i]*phi1/(PXsachN1[i]*phi1+PXsachN2[i]*phi2+PXsachN3[i]*phi3))
        i=i+1
        continue

        # prob N2/X
    i=0
    while i < 16:
        PN2sachX.append(PXsachN2[i]*phi2/(PXsachN1[i]*phi1+PXsachN2[i]*phi2+PXsachN3[i]*phi3))
        i=i+1
        continue
        # prob N3/X
    i=0
    while i < 16:
        PN3sachX.append(PXsachN3[i]*phi3/(PXsachN1[i]*phi1+PXsachN2[i]*phi2+PXsachN3[i]*phi3))
        i=i+1
        continue    

    #Recalculer la moyenne
    Mu1=0

    i=0
    while i < 16:
        Mu1=Mu1+data[i]*PN1sachX[i]
        i=i+1
        continue

    Mu1=Mu1/16 
    Mu2=0

    i=0
    while i < 16:
        Mu2=Mu2+data[i]*PN2sachX[i]
        i=i+1
        continue

    Mu2=Mu2/16   
    Mu3=0

    i=0
    while i < 16:
        Mu3=Mu3+data[i]*PN3sachX[i]
        i=i+1
        continue
    Mu3=Mu3/16   

    #Recalculer l'erreur

    i=0
    while i < 16:
        Erreur1.append(PN1sachX[i]*((data[i]-Mu1)**2))
        i=i+1
        continue

    i=0
    while i < 16:
        Erreur2.append(PN2sachX[i]*((data[i]-Mu2)**2))
        i=i+1
        continue

    i=0
    while i < 16:
        Erreur3.append(PN3sachX[i]*((data[i]-Mu3)**2))
        i=i+1
        continue

    #Calculer sigma
    SommeErreur1=0
    SommeErreur2=0
    SommeErreur3=0
    Sommeproba1=0
    Sommeproba2=0
    Sommeproba3=0

    i=0 
    while i < 16:
        SommeErreur1=SommeErreur1+Erreur1[i]
        SommeErreur2=SommeErreur2+Erreur2[i]
        SommeErreur3=SommeErreur3+Erreur3[i]
        Sommeproba1=Sommeproba1+PN1sachX[i]
        Sommeproba2=Sommeproba2+PN2sachX[i]    
        Sommeproba3=Sommeproba3+PN3sachX[i]            
        i=i+1
        continue


    Sig1 = SommeErreur1 / Sommeproba1

    Sig2 = SommeErreur2 / Sommeproba2

    Sig3 = SommeErreur3 / Sommeproba3

    phi1=Sommeproba1/(Sommeproba1+Sommeproba2+Sommeproba3)
    phi2=Sommeproba2/(Sommeproba1+Sommeproba2+Sommeproba3)
    phi3=Sommeproba3/(Sommeproba1+Sommeproba2+Sommeproba3)

    j=j+1
    continue

# print(liste)

print("Mu1 :")
print(Mu1)
print("Sig1 :")
print(Sig1)

print("Mu2 :")
print(Mu2)
print("Sig2 :")
print(Sig2)

print("Mu3 :")
print(Mu3)
print("Sig3 :")
print(Sig3)

