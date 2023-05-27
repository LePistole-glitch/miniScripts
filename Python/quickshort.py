#from random import random
import numpy as np
import time

inicio = time.time()
n = 100000

def particion(lista, min, max):
	pivote = lista[max]
	i = min - 1
	for j in range(min, max):
		if lista[j] <= pivote:
			i = i + 1
			(lista[i], lista[j]) = (lista[j], lista[i])
	(lista[i + 1], lista[max]) = (lista[max], lista[i + 1])
	return i + 1

def quickshort(lista, min, max):
	if min < max:
		pi = particion(lista, min, max)
		quickshort(lista, min, pi - 1)
		quickshort(lista, pi + 1, max)


lista1 = [np.random.randint(0, 10000) for _ in range(n)]
print(lista1)

size = len(lista1)

quickshort(lista1, 0, size - 1)

print(lista1)

fin = time.time()
print("Tiempo de ejecucion: ", round(fin-inicio, 4)) 
