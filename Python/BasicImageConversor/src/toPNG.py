from PIL import Image
from pillow_heif import register_heif_opener
import pillow_heif, os, gc, math, io

register_heif_opener()

class Error(Exception):
    pass

gc.enable()
gc.set_threshold(900, 15, 15)

def rename():
    cont = 1
    images = [file for file in os.listdir() if file.endswith(('jpg', 'png', 'JPG', 'jfif', 'webp', 'jpeg'))]
    anw_2 = input("New Names of files: ")
    while len(images) != 0:
        x = images.pop(0)
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
        elif x.endswith('.JPEG'): 
            os.rename(x, anw_2+" ("+str(cont)+").JPEG")
        elif x.endswith('.jfif'): 
            os.rename(x, anw_2+" ("+str(cont)+").jfif")
        cont = cont + 1
    

    del images 
    videos = [file for file in os.listdir() if file.endswith(('mp4','mov','MOV','avi','mkv'))]
    if len(videos) > 0:
        while len(videos) != 0:
            x = videos.pop(0)
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
    else:
        del videos
    
    #files = os.listdir()
    gifs = [file for file in os.listdir() if file.endswith(('gif','GIF'))]
    if len(gifs) > 0:
        while len(gifs) != 0:
            x = gifs.pop(0)
            if x.endswith('.gif'): 
                os.rename(x, anw_2+" ("+str(cont)+").gif")
            elif x.endswith('.GIF'): 
                os.rename(x, anw_2+" ("+str(cont)+").GIF")
        cont = cont + 1
    else:
        del gifs
    
    del cont, anw_2

def main():
    size_1 = 0
    size_2 = 0
    byteImgIO = io.BytesIO()
    qlt = int(input("Quality 0 to 9 ( 1 gives best speed, 9 gives best compression, 0 gives no compression at all. Default is 6.)?: ")) 
    images = [file for file in os.listdir() if file.endswith(('jpg', 'JPG', 'jfif', 'jpeg', 'JPEG', 'PNG', 'png'))]
    print(f"These are all of the files in our current working directory: {images}")

    while len(images) != 0:
        image = images.pop(0) #Sacar de la cola el primer elementos

        if image.endswith('jpg') or image.endswith('JPG') or image.endswith('jfif') or image.endswith('jpeg') or image.endswith('JPEG'):
            #Crea una imagen en el buffer de Python para modificarla
            byteImg = Image.open(image)
            byteImg.save(byteImgIO, "JPEG")
            byteImgIO.seek(0)
            byteImg = byteImgIO.read()

            dataBytesIO = io.BytesIO(byteImg)
            
            im = Image.open(dataBytesIO)
            im = im.convert('RGB')
            image_name = image.split('.')[0]
            print(f"This is the image name: {image_name}")
            im.save(f"{image_name}.png", 'png', compress_level = qlt)

            im.close()
            #####################
            dataBytesIO.flush()
            dataBytesIO.seek(0)
            byteImgIO.flush()
            byteImgIO.seek(0)

        elif image.endswith('webp'):
            #Crea una imagen en el buffer de Python para modificarla
            byteImg = Image.open(image)
            byteImg.save(byteImgIO, "WEBP")
            byteImgIO.seek(0)
            byteImg = byteImgIO.read()

            dataBytesIO = io.BytesIO(byteImg)
            
            
            
            im = Image.open(dataBytesIO)
            im = im.convert('RGB')
            image_name = image.split('.')[0]
            print(f"This is the image name: {image_name}")
            im.save(f"{image_name}.png", 'png', compress_level = qlt)
            
            im.close()
            #####################
            dataBytesIO.flush()
            dataBytesIO.seek(0)
            byteImgIO.flush()
            byteImgIO.seek(0)

        elif image.endswith('png') or image.endswith('PNG'):
            #Crea una imagen en el buffer de Python para modificarla
            byteImg = Image.open(image)
            byteImg.save(byteImgIO, "PNG")
            byteImgIO.seek(0)
            byteImg = byteImgIO.read()

            dataBytesIO = io.BytesIO(byteImg)
            im = Image.open(dataBytesIO)
            im = im.convert('RGB')
            image_name = image.split('.')[0]
            print(f"This is the image name: {image_name}")
            im.save(f"{image_name}-New.png", 'png', optimize = True, quality = qlt , progressive = True)
                
            im.close()
            #####################
            dataBytesIO.flush()
            dataBytesIO.seek(0)
            byteImgIO.flush()
            byteImgIO.seek(0)
        else: 
            raise Error
    #Delete old files JPG/PNG
    files = os.listdir()
    images = [file for file in files if file.endswith(('jpg', 'JPG', 'jfif', 'jpeg', 'heif', 'heic', 'avif'))]
    image_png = [file for file in files if file.endswith(('PNG', 'png'))]

    for x in images:
            size_1 = size_1 + os.stat(x).st_size
    for y in image_png:
            size_2 = size_2 + os.stat(y).st_size

    print("Total Size of JPG-WEBP-HEIF: "+convert_size(size_1))
    print("Total Size of PNG: "+convert_size(size_2))

    anw = input("Do you want to delete \n 1.-JPG-HEIF-WEBP files \n 2.-PNG \n1 or 2?: ")

    if anw == '1':
        for x in images:
            os.remove(x)
    elif anw == '2':
        for y in image_png:
            os.remove(y)
    else:
        pass
    
    anw = input("Do you want change names of files in the folder? (Y/N): ")
    if anw == 'Y' or anw == 'y' or anw == 'yes':
        rename()
    else:
        pass

    
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return "%s %s" % (s, size_name[i])




if __name__ == "__main__":
    main()

