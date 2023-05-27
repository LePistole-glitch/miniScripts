import math
import time

inicio = time.time()
cont = 0
L1 = int(input("Ingresa lim 1: "))
L2 = int(input("Ingresa lim 1: "))

def calc(i):
    if i == 4 or i == 0 or i == 1:
        return False
    for x in range(2, math.trunc(i/2)): #math.trunc(math.sqrt(i))
        if i % x == 0:
            return False
    return True
    

for i in range(L1, L2):
    if calc(i) == True:
        print("primo: ", i)
        cont = cont + 1

print("Total de primos: ",cont)
fin = time.time()
print("Tiempo de ejecucion: ",round(fin-inicio, 4) )

