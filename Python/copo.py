from numpy import random
from turtle import *


def copo(direccion, itera):
    if itera == 0:
        forward(direccion)
        return
    direccion /= 3.0
    copo(direccion, itera-1)
    left(60)
    copo(direccion, itera-1)
    right(120)
    copo(direccion, itera-1)
    left(60)
    copo(direccion, itera-1)

#funcion main
if __name__ == "__main__":
    speed(0)
    ancho = 150.0
    penup()

    backward(ancho/2.0)

    itera = random.randint(1, 6)

    pendown()
    for i in range(3):
        copo(ancho, itera)
        right(120)

    mainloop()