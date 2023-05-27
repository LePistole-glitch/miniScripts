from PIL import Image
from pillow_heif import register_heif_opener
import pillow_heif, os, math, io, gc

register_heif_opener()

gc.enable()
gc.set_threshold(900, 15, 15)


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return "%s %s" % (s, size_name[i])


byteImgIO = io.BytesIO()
size_1 = 0
size_2 = 0
images = [file for file in os.listdir() if file.endswith(('jpg', 'jpeg', 'JPG'))]
qlt = int(input("Quality 1 to 100 (-1 Lossless): "))
print(f"These are all of the files in our current working directory: {images}")

while len(images) != 0:
    image = images.pop(0) #Sacar de la cola el primer elementos
    byteImg = Image.open(image)
    byteImg.save(byteImgIO, "JPEG")
    byteImgIO.seek(0)
    byteImg = byteImgIO.read()

    dataBytesIO = io.BytesIO(byteImg)
            
    im = Image.open(dataBytesIO)
    image_name = image.split('.')[0]
    print(f"This is the image name: {image_name}")
    im.save(f"{image_name}.heif", quality = qlt, enc_params={"x265:pools": "3"})
            
    #####################
    im.close()
    dataBytesIO.flush()
    dataBytesIO.seek(0)
    byteImgIO.flush()
    byteImgIO.seek(0)
    
files = os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'jfif', 'jpeg', 'PNG'))]
image_heif = [file for file in files if file.endswith(('heif'))]
    
for x in images:
    size_1 = size_1 + os.stat(x).st_size
for y in image_heif:
    size_2 = size_2 + os.stat(y).st_size

print("Total Size of JPG/PNG: "+convert_size(size_1))
print("Total Size of HEIF: "+convert_size(size_2))


