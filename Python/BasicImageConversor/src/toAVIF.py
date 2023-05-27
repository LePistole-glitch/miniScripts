from PIL import Image
from pillow_heif import register_avif_opener
import pillow_heif, os, math, io

register_avif_opener()


class Error(Exception):
    pass
  
def main():
    size_1 = 0
    size_2 = 0
    byteImgIO = io.BytesIO()
    images = [file for file in os.listdir() if file.endswith(('JPG', 'jpg', 'jpeg', 'PNG', 'png'))]
    qlt = int(input("Quality 1 to 100 (-1 is lossless): "))

    while len(images) != 0:
        image = images.pop(0)
         
        if image.endswith('jpg') or image.endswith('jpeg'):
            byteImg = Image.open(image)
            byteImg.save(byteImgIO, "JPEG")
            byteImgIO.seek(0)
            byteImg = byteImgIO.read()
            
            dataBytesIO = io.BytesIO(byteImg)
            
            im = Image.open(dataBytesIO)
            im = im.convert('RGB')
            image_name = image.split('.')[0]
            print(f"This is the image name: {image_name}")
            im.save(f"{image_name}.avif", 'avif', quality = qlt)
            
            im.close()
            dataBytesIO.flush()
            dataBytesIO.seek(0)
            byteImgIO.flush()
            byteImgIO.seek(0)
            
        if image.endswith('PNG') or image.endswith('png'):
            byteImg = Image.open(image)
            byteImg.save(byteImgIO, "PNG")
            byteImgIO.seek(0)
            byteImg = byteImgIO.read()
            
            dataBytesIO = io.BytesIO(byteImg)
            
            im = Image.open(dataBytesIO)
            im = im.convert('RGB')
            image_name = image.split('.')[0]
            print(f"This is the image name: {image_name}")
            im.save(f"{image_name}.avif", 'avif', quality = qlt)
            
            im.close()
            dataBytesIO.flush()
            dataBytesIO.seek(0)
            byteImgIO.flush()
            byteImgIO.seek(0)    
        else:
            raise Error  
                
    #Delete old files JPG/PNG/WEBP
    images = [file for file in os.listdir() if file.endswith(('png', 'JPG', 'jpg', 'webp', 'jpeg'))]
    image_avif = [file for file in os.listdir() if file.endswith(('avif'))]

    for x in images:
            size_1 = size_1 + os.stat(x).st_size
    for y in image_avif:
            size_2 = size_2 + os.stat(y).st_size
            
    print("Total Size of JPG/PNG/WEBP: "+convert_size(size_1))
    print("Total Size of AVIF: "+convert_size(size_2))

    anw = input("Do you want to delete \n 1.-JPG and/or PNG files \n 2.-AVIF \n1 or 2?: ")

    if anw == '1':
        for x in images:
            os.remove(x)
    elif anw == '2':
        for y in image_avif:
            os.remove(y)
    
    del images, image_avif

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return "%s %s" % (s, size_name[i])
