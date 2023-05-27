import numpy as np
import matplotlib.pyplot as plt

colum = 1000
filas = 1000 

def divergencia(re, imagin, maxIter):
    c = complex(re, imagin)
    z = 0.0j

    for i in range(maxIter):
        z = z*z + c

        if z.real*z.real + z.imag*z.imag >= 4:
            return i
    return maxIter

planoImag = np.zeros([colum, filas])

for indiceF, re in enumerate(np.linspace(-2, 1, num=filas)):
    for indiceC, im in enumerate(np.linspace(-1, 1, num=colum)):
        planoImag[indiceC, indiceF] = divergencia(re, im, 100)

plt.figure(dpi=100)
plt.imshow(planoImag, cmap='inferno', extent=[-2,1,-1,1])
plt.show()