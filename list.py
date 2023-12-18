from colorama import Fore, Style
import os
import numpy as np

images_PNG = np.array([])
images_JPG = np.array([])
images_JPEG = np.array([])
videos = np.array([])
gif = np.array([])
cont = 1

for file in os.listdir():
    if file.endswith('.png'):
        images_PNG = np.append(images_PNG, file)
    elif file.endswith('.jpg'):
        images_JPG = np.append(images_JPG, file)
    elif file.endswith('.jpeg'):
        images_JPEG = np.append(images_JPEG, file)
    elif file.endswith('.mp4') or file.endswith('.MP4') or file.endswith('.mov') or file.endswith('.MOV') or file.endswith('.m4v'): 
        videos = np.append(videos, file)
    elif file.endswith('.gif') or file.endswith('.GIF'): 
        gif = np.append(gif, file)
print("Archivos a modificar!:")
print(Fore.RED, images_PNG, images_JPG , images_JPEG, Style.RESET_ALL)
print(Fore.RED, videos, Style.RESET_ALL)
print(Fore.RED, gif, Style.RESET_ALL)
newNombre = input("Ingresa el nuevo nombre que quieres ponerle: ")

while len(images_PNG) != 0: #PNG
    dirr = str(images_PNG[0])
    images_PNG = np.delete(images_PNG, 0)
    #print(dirr)

    if dirr.endswith('.png'):
        os.rename(dirr, newNombre+" ("+str(cont)+").png")
    cont += 1
    print(Fore.CYAN+"Se esta trabajando en: "+dirr+ Style.RESET_ALL) 

while len(images_JPEG) != 0: #JPEG
    dirr = str(images_JPEG[0])
    images_JPEG = np.delete(images_JPEG, 0)
    if dirr.endswith('.jpeg'):
        os.rename(dirr, newNombre+" ("+str(cont)+").jpeg")
    print(Fore.CYAN+"Se esta trabajando en: "+dirr+ Style.RESET_ALL)   
    cont += 1


while len(images_JPG) != 0: #JPG
    dirr = str(images_JPG[0])
    images_JPG = np.delete(images_JPG, 0)
    if dirr.endswith('.jpg'):
        os.rename(dirr, newNombre+" ("+str(cont)+").jpg")
    print(Fore.CYAN+"Se esta trabajando en: "+dirr+ Style.RESET_ALL)   
    cont += 1

if len(videos) != 0:
    while len(videos) != 0:
        dirr = str(videos[0])
        videos = np.delete(videos, 0)
        if dirr.endswith('.mp4'):
            os.rename(dirr, newNombre+" ("+str(cont)+").mp4")
        elif dirr.endswith('.MP4'):
            os.rename(dirr, newNombre+" ("+str(cont)+").MP4")
        elif dirr.endswith('.mov'):
            os.rename(dirr, newNombre+" ("+str(cont)+").mov")
        elif dirr.endswith('.MOV'):
            os.rename(dirr, newNombre+" ("+str(cont)+").MOV")
        elif dirr.endswith('.m4v'):
            os.rename(dirr, newNombre+" ("+str(cont)+").m4v")
        
        print(Fore.CYAN+"Se esta trabajando en: "+dirr+ Style.RESET_ALL)       

        cont += 1

if len(gif) != 0:
    while len(gif) != 0:
        dirr = str(gif[0])
        gif = np.delete(gif, 0)
        if dirr.endswith('.gif'):
            os.rename(dirr, newNombre+" ("+str(cont)+").gif")
        elif dirr.endswith('.GIF'):
            os.rename(dirr, newNombre+" ("+str(cont)+").GIF")
        print(Fore.CYAN+"Se esta trabajando en: "+dirr+ Style.RESET_ALL)
        cont += 1


print("Es todo!")
print = input()
