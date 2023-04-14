def _merge(izq:list,der:list,f)->list:
	i = 0
	j = 0
	k = 0
	arrayOrdenado = [0] * (len(izq)+len(der))
	while i < len(izq) and j < len(der):
		if f(izq[i],der[j]) >= 1:
			arrayOrdenado[k] = der[j]
			j+=1
		else:
			arrayOrdenado[k] = izq[i]
			i+=1
		k+=1

	while i < len(izq):
		arrayOrdenado[k] = izq[i]
		i+=1
		k+=1

	while j < len(der):
		arrayOrdenado[k] = der[j]
		j+=1
		k+=1
	return arrayOrdenado


def mergeSort(array:list,comparador)->list:
	"""	comparador tiene que ser una funcion que reciba dos objetos del array y los compara
		si devuelve un numero mayor a 1 implica que el de la izq es mayor al de la derecha
		si devuelve 0 implica que son iguales
		y si devuelve un numero menor a -1 implica que el de la izq es menor al de la derecha
	"""
	if len(array) == 1:
		return array

	mitad = len(array) // 2
	izq = mergeSort(array[:mitad],comparador)
	der = mergeSort(array[mitad:],comparador)
	return _merge(izq,der,comparador)