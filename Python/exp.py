
# Python code to demonstrate math.factorial()
import math
  

def func(x, n):
    suma = 0
    for i in range(n):
        suma += math.pow(x, i) / math.factorial(i)
    return suma

print(func(5, 5))