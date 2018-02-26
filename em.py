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
Mu1=1.7 
Sig1=0.3 
Mu1=1.8 
Sig1=0.2  
phi1=1/3 
phi2=1/3 
phi3=1/3

#P X/N   
    # prob X/N1
i=0
while i < 16:
    PXsachN1.append(stats.norm.ppf(data[i], loc=1.6, scale= 0.1))
    i=i+1
    continue

    # prob X/N2
i=0
while i < 16:
    PXsachN2.append(stats.norm.ppf(data[i], loc=1.7, scale= 0.3))
    i=i+1
    continue

    # prob X/N3
i=0
while i < 16:
    PXsachN3.append(stats.norm.ppf(data[i], loc=1.8, scale= 0.2))
    i=i+1
    continue
#P N/X
    # prob N1/X
i=0
while i < 16:
    PN1sachX.append(PXsachN1[i]*phi1/(PXsachN1*phi1+PXsachN2*phi2+PXsachN3*phi3))
    i=i+1
    continue

    # prob N2/X
i=0
while i < 16:
    PN2sachX.append(PXsachN2[i]*phi2/(PXsachN1*phi1+PXsachN2*phi2+PXsachN3*phi3))
    i=i+1
    continue
    # prob N3/X
i=0
while i < 16:
    PN3sachX.append(PXsachN3[i]*phi3/(PXsachN1*phi1+PXsachN2*phi2+PXsachN3*phi3))
    i=i+1
    continue    

 
# print(liste)
print(x)