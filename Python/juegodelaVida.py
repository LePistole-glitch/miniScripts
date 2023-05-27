from numpy import random
from matplotlib import animation, rc
import matplotlib.pyplot as plt

rc('animation', html = 'html5')

def actualiza(i):
    ax.clear()
    ax.imshow(Cs[i], cmap = "gray")
    ax.axis('off')
    return ax

def visualizar(C):
    plt.imshow(C, cmap = 'gray')
    plt.axis('off')
    plt.show()

def init(Nx = 100, Ny = 100):
    C = [[0 for j in range(Nx + 2)] for i in range(Ny + 2)] #[[random.randint(0, 1) for j in range(Nx)] for i in range(Ny)]
    for i in range(1, Ny+1):
        for j in range(1, Nx+1):
            C[i][j] = random.randint(0,2)
    
    return C

def iteracionMundo(C):
    Ny, Nx = len(C) - 2, len(C[0]) - 2
    C2 = [[0 for j in range(Nx + 2)] for i in range(Ny + 2)]
    for i in range(1, Ny+1):
            for j in range(1, Nx+1):
                c = C[i][j]                                         #Aqui
                v = C[i][j+1]   + C[i][j-1]   + C[i-1][j]   + C[i+1][j] + \
                    C[i+1][j+1] + C[i+1][j-1] + C[i-1][j+1] + C[i-1][j-1]                
                if c == 0:
                    if v == 3:
                        C2[i][j] = 1
                    else:
                        C2[i][j] = 0
                else:
                    if v == 3 or v == 2:
                        C2[i][j] = 1
                    else:
                        C2[i][j] = 0
    return C2

def juegoConway(C0, MAX = 1000):
    Cs = [C0]
    itera = 0
    while itera < MAX:
        C = iteracionMundo(C0)
        Cs.append(C)
        C0 = C  
        itera += 1
    return Cs

C = init()
Cs = juegoConway(C)
fig = plt.figure(figsize=(5,5))
ax = plt.subplot(1,1,1)
anim = animation.FuncAnimation(fig,actualiza,frames=len(Cs),interval=100)
plt.show()
plt.close()

anim