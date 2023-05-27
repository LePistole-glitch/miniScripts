from PIL import Image
from pillow_heif import register_heif_opener
import pillow_heif, os, gc, io, math

register_heif_opener()

class Error(Exception):
    pass

gc.enable()
gc.set_threshold(900, 15, 15)

def main():
    size_1 = 0
    size_2 = 0
    byteImgIO = io.BytesIO()
    
    qlt = int(input("Quality 0 to 100?: "))
    images = [file for file in os.listdir() if file.endswith(('PNG', 'webp', 'png', 'heif', 'heic'))]
    print(f"These are all of the files in our current working directory: {images}")

    while len(images) != 0:
        image = images.pop(0) #Sacar de la cola el primer elementos
        if image.endswith('png') or image.endswith('PNG'):
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
            im.save(f"{image_name}.jpeg", 'jpeg', optimize = True, quality = qlt , progressive = True)
            
            im.close()
            #####################
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
            im.save(f"{image_name}.jpeg", 'jpeg', optimize = True, quality = qlt , progressive = True)
                
            im.close()
            byteImgIO.flush()
            byteImgIO.seek(0)

        elif image.endswith('heif') or image.endswith('heic'):
            #Crea una imagen en el buffer de Python para modificarla
            byteImg = Image.open(image)
            byteImg.save(byteImgIO, "HEIF")
            byteImgIO.seek(0)
            byteImg = byteImgIO.read()

            dataBytesIO = io.BytesIO(byteImg)
            im = Image.open(dataBytesIO)
            im = im.convert('RGB')
            image_name = image.split('.')[0]
            print(f"This is the image name: {image_name}")
            im.save(f"{image_name}.jpeg", 'jpeg', optimize = True, quality = qlt , progressive = True,  enc_params={"x265:pools": "3"})
                
            im.close()
            byteImgIO.flush()
            byteImgIO.seek(0)
        else:
            raise Error
        
    #Delete old files JPG/PNG
    files = os.listdir()
    images = [file for file in files if file.endswith(('png', 'webp', 'PNG', 'heif', 'heic'))]
    image_webp = [file for file in files if file.endswith(('JPG', 'jpeg', 'jpg'))]

    for x in images:
        size_1 = size_1 + os.stat(x).st_size
    for y in image_webp:
        size_2 = size_2 + os.stat(y).st_size
                
    print("Total Size of WEBP/PNG/HEIF: "+convert_size(size_1))
    print("Total Size of JPEG: "+convert_size(size_2))
        
    anw = input("Do you want to delete \n 1.-Source Images files \n 2.-New JPG \n1 or 2?: ")

    if anw == '1':
        for x in images:
            os.remove(x)
    elif anw == '2':
        for y in image_webp:
            os.remove(y)
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