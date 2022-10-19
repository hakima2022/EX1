
import math
D1=input("entrer la valeur de la distance :")
V1=input("donner la valeur de la vitesse V1:")
V2=input("saisir la valeur de la vitesse V2:")
MV=input("donner la valeur de la masse volumique ")
angle=10*3.14/180
try:
    D1=float(D1)
    V1=float(V1)
    V2=float(V2)
    MV=float(MV)
    L=D1/(2*math.tan(angle))*(1-math.sqrt(V1/V2))
    DP=1/2*MV*((V1**2)-(V2**2))
    print("la longeur est : ",L,"en mm")
    print("la différence de pression est: ",DP,"en Pa")
except:
    print("la valeur que vous avez de la distance ou les vitesses ou la masse volumique n'est pas correcte")
