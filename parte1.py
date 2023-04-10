from proyecto import Proyecto
import random

def parte1DivYConq(arreglo:list,inicio:int,fin:int)->(int,int,int):
	if inicio >= fin:
		
		return arreglo[inicio].ganancia,arreglo[inicio].prestigio,inicio
	mitad:int = (inicio + fin)//2
	izq = parte1DivYConq(arreglo,inicio,mitad)
	der = parte1DivYConq(arreglo,mitad+1,fin)
	if izq[0]<der[0] and izq[1]< der[1]:
		return der
	else:
		return izq

def main():
	posiblesGanancias = []
	for i in range(100):
		posiblesGanancias.append(i)
	arregloResoluble = []
	printearArreglo = "[ "
	for j in range(15):
		proyect = Proyecto(random.choice(posiblesGanancias),random.choice(posiblesGanancias))
		printearArreglo += f"{str(proyect)} ,\n"
		arregloResoluble.append(proyect)
	print("Arreglo a solucionar:")
	print()
	printearArreglo = printearArreglo[:len(printearArreglo)-2] + "]"
	print(printearArreglo)
	proyectoGanador = parte1DivYConq(arregloResoluble,0,len(arregloResoluble)-1)
	print()
	print("Solucionado y proyecto ganador:")
	print()
	print(arregloResoluble[proyectoGanador[2]])
	print()

main()
