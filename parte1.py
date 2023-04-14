from proyecto import Proyecto
import random
from mergesort import mergeSort

def f(a:tuple,b:tuple):
	if a[0] >= b[0]:
		return -1
	else:
		return 1


def parte1DivYConq(arr:list)->list:
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    izq = parte1DivYConq(L)
    der = parte1DivYConq(R)
    return _mergeDivYConq(izq,der)


def _mergeDivYConq(izq:list,der:list)->list:
	i:int = 0
	j:int = 0
	arreglo:list = []
	while j<len(der):
		if i == len(izq)-1 :
			arreglo.append(izq[i])
			i+=1
			continue
		if i != len(izq) :
			if izq[i][1] > der[j][1]:
				j += 1
			else:
				arreglo.append(izq[i])
				i+=1
				
		else:
			if izq[i-1][1] > der[j][1]:
				j += 1
			else:
				arreglo.append(der[j])
				j+=1
	if i != len(izq) :
		while i<len(izq):
			arreglo.append(izq[i])
			i+=1
	return arreglo

		


def main():
	posiblesGanancias = []
	for i in range(100):
		posiblesGanancias.append(i)
	arregloResoluble = []
	for j in range(6):
		proyect = (random.choice(posiblesGanancias),random.choice(posiblesGanancias))
		arregloResoluble.append(proyect)
	arregloresoluble = mergeSort(arregloResoluble,f)
	print("Arreglo a solucionar:")
	print()
	print(arregloresoluble)
	proyectosGanadorer = parte1DivYConq(arregloResoluble)
	print()
	print("Solucion con los proyectos ganadores:")
	print()
	for p in proyectosGanadorer:
		print(p)
	print()

main()
