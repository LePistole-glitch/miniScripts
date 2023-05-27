from PIL import Image, ImageFilter
from pillow_heif import register_avif_opener
import os, math, io

register_avif_opener()

class Error(Exception):
    pass

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

qlt = int(input("Quality 1 - 100: "))
images = [file for file in os.listdir() if file.endswith(('jpg', 'JPG', 'jfif', 'jpeg'))]
print(f"\n\nThese are all of the files in our current working directory: {images}")


while len(images) != 0:
    image = images.pop(0)
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
    del dataBytesIO
    im.close()

images = [file for file in os.listdir() if file.endswith(('jpg', 'JPG', 'jfif', 'jpeg'))]
image_webp = [file for file in os.listdir() if file.endswith(('webp'))]

for x in images:
    size_1 = size_1 + os.stat(x).st_size
for y in image_webp:
    size_2 = size_2 + os.stat(y).st_size

print("Total Size of JPG/PNG: "+convert_size(size_1))
print("Total Size of WEBP: "+convert_size(size_2))

del image_webp, images