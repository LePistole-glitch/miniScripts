import os, gc, glob
import math


def rename():
    cont = 1
    files = os.listdir()
    images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'jfif', 'webp', 'jpeg'))]
    anw_2 = input("New Names of files: ")
    for x in images:
        if x.endswith('.webp'): 
            os.rename(x, anw_2+" ("+str(cont)+").webp")
        elif x.endswith('.png'): 
            os.rename(x, anw_2+" ("+str(cont)+").png")
        elif x.endswith('.jpg'): 
            os.rename(x, anw_2+" ("+str(cont)+").jpg")    
        elif x.endswith('.JPG'): 
            os.rename(x, anw_2+" ("+str(cont)+").JPG")
        elif x.endswith('.jpeg'): 
            os.rename(x, anw_2+" ("+str(cont)+").jpeg")
        elif x.endswith('.jfif'): 
            os.rename(x, anw_2+" ("+str(cont)+").jfif")
        cont = cont + 1
    

    del files, images 
    #files = os.listdir()
    videos = (file for file in os.listdir() if file.endswith(('mp4','mov','MOV','avi','mkv')))
    if videos:
        for x in videos:
            try:
                if x.endswith('.mp4'): 
                    os.rename(x, anw_2+" ("+str(cont)+").mp4")
                elif x.endswith('.mov'): 
                    os.rename(x, anw_2+" ("+str(cont)+").mov")
                elif x.endswith('.MOV'): 
                    os.rename(x, anw_2+" ("+str(cont)+").MOV")    
                elif x.endswith('.avi'): 
                    os.rename(x, anw_2+" ("+str(cont)+").avi")
                elif x.endswith('.mkv'): 
                    os.rename(x, anw_2+" ("+str(cont)+").mkv")    
                cont = cont + 1
            except FileExistsError:
                pass
    else:
        del videos
    
    #files = os.listdir()
    gifs = (file for file in os.listdir() if file.endswith(('gif','GIF')))
    if gifs:
        for x in gifs:
            if x.endswith('.gif'): 
                os.rename(x, anw_2+" ("+str(cont)+").gif")
            elif x.endswith('.GIF'): 
                os.rename(x, anw_2+" ("+str(cont)+").GIF")
        cont = cont + 1
    else:
        del gifs
    
    del cont, anw_2

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return "%s %s" % (s, size_name[i])