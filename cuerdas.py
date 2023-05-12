import math

def triangulaciones(lista:list)->float:
    OPT = {}
    for i in range(len(lista)):
        OPT[i] = {}

    for i in range(len(lista)-1,-1,-1):

        for j in range(i+1,len(lista)):
            distanciaIJ = math.sqrt((lista[i][0]-lista[j][0])**2+(lista[i][1]-lista[j][1])**2)

            if i+1 == j:
                OPT[i][j] = distanciaIJ
            else:
                for k in range(i+1,j):
                    OPT[i][j] = min(OPT[i].get(j,float("inf")),distanciaIJ + OPT[i][k] + OPT[k][j])

    return OPT[0][len(lista)-1]
