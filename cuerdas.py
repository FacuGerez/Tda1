import math
from clasePunto import Punto

def obtenerDistancias(puntos:tuple)->dict:
    distancias = {}
    puntosCalculados = set()

    for p in puntos:
        distancias[p] = {}
    for p1 in puntos:

        for p2 in puntos:

            if p1 == p2 or ((p1,p2) in puntosCalculados):
                 continue

            distancia = math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
            distancias[p1][p2] = distancia
            distancias[p2][p1] = distancia
            puntosCalculados.add((p1,p2))
            puntosCalculados.add((p2,p1))

    return distancias


def tiangulaciones(puntos:tuple)->float:
    distanciasTotales = obtenerDistancias(puntos)
    OPT = {}
    return _triangulaciones(distanciasTotales,puntos,OPT)

def _triangulaciones(distancias:dict,lista:tuple,OPT:dict)->float:
    if len(lista) == 3:
        return distancias[(lista[0])][(lista[1])] + distancias[(lista[0])][(lista[2])] + distancias[(lista[1])][(lista[2])]

    for i in range(len(lista)):

        for j in range(i+1,len(lista)-1):

            izq = lista[i:j+2]

            if OPT.get(izq) is None:
                OPT[izq] = _triangulaciones(distancias,izq,OPT)

            if len(izq) == len(lista):
            	der = 0
            	OPT[der] = 0
            else:
	            der = ([lista[i]]+list(lista[j+1:])+list(lista[0:i]))
	            der = tuple(der)
	            if OPT.get(der) is None:
	                OPT[der] = _triangulaciones(distancias,der,OPT)

            if OPT.get(lista) is None:

                OPT[lista] = OPT[izq] + OPT[der]

            else:

                if OPT[lista] > OPT[izq] + OPT[der]:

                    OPT[lista] = OPT[izq] + OPT[der]
    return OPT[lista]