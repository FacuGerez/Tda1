import sys
from cuerdas import triangulaciones
from clasePunto import Punto

def abrirArchivos(nombreArchivo:str):
	try:
		arrayDePuntos = [] 
		with open(nombreArchivo) as puntos:
			for punto in puntos:
				x , y = punto.rstrip("\n").replace(",",".").split(" ")
				arrayDePuntos.append(Punto(float(x),float(y)))
		return arrayDePuntos
	except:
		raise Exception(f"No se encontro el archivo {nombreArchivo}")

def main():
	parametros = sys.argv[1:]
	if len(parametros) < 1:
		print("Faltan parametros")
		return
	nombreArchivo = parametros[0]
	poligonoConvexo = abrirArchivos(nombreArchivo)
	return triangulaciones(tuple(poligonoConvexo))

	