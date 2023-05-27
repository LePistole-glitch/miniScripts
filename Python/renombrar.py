# -*- coding: utf-8 -*-# coding=utf-8
import os

def rename():
    #Funcion de renombre de archivos de imagenes, videos y gifs
    cont = 1
    images = [file for file in os.listdir() if file.endswith(('jpg', 'png', 'JPG', 'jfif', 'webp', 'jpeg', 'heif', 'heic'))]
    anw_2 = input("Nuevo nombre para esto archivos: ")
    while len(images) != 0:
        x = images.pop(0)
        if x.endswith('.heif'): 
            os.rename(x, anw_2+" ("+str(cont)+").heif")
        elif x.endswith('.heic'): 
            os.rename(x, anw_2+" ("+str(cont)+").heic")
        elif x.endswith('.webp'): 
            os.rename(x, anw_2+" ("+str(cont)+").webp")
        elif x.endswith('.png'): 
            os.rename(x, anw_2+" ("+str(cont)+").png")
        elif x.endswith('.jpg'): 
            os.rename(x, anw_2+" ("+str(cont)+").jpg")    
        elif x.endswith('.JPG'): 
            os.rename(x, anw_2+" ("+str(cont)+").JPG")
        elif x.endswith('.jpeg'): 
            os.rename(x, anw_2+" ("+str(cont)+").jpeg")
        elif x.endswith('.JPEG'): 
            os.rename(x, anw_2+" ("+str(cont)+").JPEG")
        elif x.endswith('.jfif'): 
            os.rename(x, anw_2+" ("+str(cont)+").jfif")
        cont = cont + 1
    

    del images 

    
    gifs = [file for file in os.listdir() if file.endswith(('gif','GIF'))]
    if len(gifs) > 0:
        while len(gifs) != 0:
            x = gifs.pop(0)
            if x.endswith('.gif'): 
                os.rename(x, anw_2+" ("+str(cont)+").gif")
            elif x.endswith('.GIF'): 
                os.rename(x, anw_2+" ("+str(cont)+").GIF")
        cont = cont + 1
    
    del gifs
    
    videos = [file for file in os.listdir() if file.endswith(('mp4','mov','MOV','avi','mkv', 'MP4'))]
    if len(videos) > 0:
        while len(videos) != 0:
            x = videos.pop(0)
            if x.endswith('.mp4'): 
                os.rename(x, anw_2+" ("+str(cont)+").mp4")
            elif x.endswith('.MP4'): 
                os.rename(x, anw_2+" ("+str(cont)+").MP4") 
            elif x.endswith('.mov'): 
                os.rename(x, anw_2+" ("+str(cont)+").mov")
            elif x.endswith('.MOV'): 
                os.rename(x, anw_2+" ("+str(cont)+").MOV")    
            elif x.endswith('.avi'): 
                os.rename(x, anw_2+" ("+str(cont)+").avi")
            elif x.endswith('.mkv'): 
                os.rename(x, anw_2+" ("+str(cont)+").mkv")    
               
            cont = cont + 1 

    del videos
    
    
    del cont, anw_2, gifs



if __name__ == "__main__":
    rename()
