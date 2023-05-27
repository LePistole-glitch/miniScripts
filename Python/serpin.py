import matplotlib.pyplot as plt
import random


verticeX = 0
verticeY = 0
puntosMediosX = 0
puntosMediosY = 0

pX1 = random.random(); pY1 = random.random()

vX1 = random.random(); vY1 = random.random()
vX2 = random.random(); vY2 = random.random()
vX3 = random.random(); vY3 = random.random()


for i in range(10000):
    if random.randint(0, 2) == 0:
        if i != 0:
            puntosMediosX = (vX1 + puntosMediosX)/2
            puntosMediosY = (vY1 + puntosMediosY)/2  
        else:
            puntosMediosX = (vX1 + pX1)/2
            puntosMediosY = (vY1 + pY1)/2

    elif random.randint(0, 2) == 1:
        if i != 0:
            puntosMediosX = (vX2 + puntosMediosX)/2
            puntosMediosY = (vY2 + puntosMediosY)/2  
        else:
            puntosMediosX = (vX2 + pX1)/2
            puntosMediosY = (vY2 + pY1)/2
    elif random.randint(0, 2) == 2:
        if i != 0:
            puntosMediosX = (vX3 + puntosMediosX)/2
            puntosMediosY = (vY3 + puntosMediosY)/2  
        else:
            puntosMediosX = (vX3 + pX1)/2
            puntosMediosY = (vY3 + pY1)/2

    plt.plot(puntosMediosX, puntosMediosY, marker =",", color = 'm')



plt.plot(vX1, vY1, marker ="o", color = 'red')
plt.plot(vX2, vY2, marker ="o", color = 'red')
plt.plot(vX3, vY3, marker ="o", color = 'red')

plt.show()