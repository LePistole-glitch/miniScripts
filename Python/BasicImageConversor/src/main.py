from toPNG import main as mainPNG
from toJPG import main as mainJPG
from toWEBP import main as mainWEBP
from toAVIF import main as mainAVIF
from toHEIF import main as mainHEIF
#//////////////////////////////////////////////////////////////////////////////////////
elct = int(input("Que quieres convertir? \n\t1.- A WEBP \n\t2.- A PNG \n\t3.- A JPG\n\t4.- A AVIF\n\t5.- A HEIF\n\tRespuesta: "))

class Error(Exception):
        pass

if elct == 1:
    mainWEBP()
elif elct == 2:
    mainPNG()
elif elct == 3:
    mainJPG()
elif elct == 4:
    mainAVIF()  
elif elct == 5:
    mainHEIF()
else:
    pass

print("Eso es todo!")
elct = input()
