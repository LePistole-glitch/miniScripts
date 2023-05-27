#Code By Jesus Chavez Arias
import PIL
import os, gc, glob
import math
from PIL import Image

gc.set_threshold(900, 15, 15)
size_1 = 0
size_2 = 0
qlt = int(input("Quality 1 to 100?: "))

files = os.listdir() # We list all of the files and folders using os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'jfif', 'jpeg'))]
print(f"These are all of the files in our current working directory: {images}")

class Error(Exception):
    pass

def convert_image(image_path, image_type):
    # 1. Opening the image:
    im = Image.open(image_path)
    # 2. Converting the image to RGB colour:
    im = im.convert('RGB')
    # 3. Spliting the image path (to avoid the .jpg or .png being part of the image name):
    image_name = image_path.split('.')[0]
    print(f"This is the image name: {image_name}")
    # Saving the images based upon their specific type:
    if image_type == 'jpg' or image_type == 'png':
        im.save(f"{image_name}.webp", 'webp', quality = qlt, method = 6)
    else:
        raise Error

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return "%s %s" % (s, size_name[i])

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
    videos = (file for file in os.listdir() if file.endswith(('mp4','mov','MOV','avi')))
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
    

for image in images:
    if image.endswith('jpg') or image.endswith('JPG') or image.endswith('jfif') or image.endswith('jpeg'):
        convert_image(image, image_type='jpg')
    elif image.endswith('png'):
        convert_image(image, image_type='png')
    else:
        raise Error

del images, qlt, files


files = os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'jfif', 'jpeg'))]
image_webp = [file for file in files if file.endswith(('webp'))]

for x in images:
        size_1 = size_1 + os.stat(x).st_size
for y in image_webp:
        size_2 = size_2 + os.stat(y).st_size
        
print("Size of JPG/PNG: "+convert_size(size_1))
print("Size of WEBP: "+convert_size(size_2))

anw = input("Do you want to delete \n 1.-JPG and/or PNG files \n 2.-WEBP \n1 or 2?: ")

if anw == '1':
    for x in images:
        os.remove(x)
elif anw == '2':
    for y in image_webp:
        os.remove(y)

del size_1, size_2, files, image_webp

anw = input("Do you want change names of files in the folder? (Y/N): ")
if anw == 'Y' or anw == 'y' or anw == 'yes':
    rename()
else:
    pass

print("That's all... :)")



