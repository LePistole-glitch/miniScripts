from PIL import Image
import PIL
import pillow_avif
import os, math


class Error(Exception):
    pass
  
def main():
    size_1 = 0
    size_2 = 0
    files = os.listdir()
    images = [file for file in files if file.endswith(('png', 'JPG', 'jpg', 'webp', 'jpeg'))]
    qlt = int(input("Quality 1 to 100: "))

    for image in images:
            if image.endswith('png') or image.endswith('PNG') or image.endswith('jpg') or image.endswith('webp') or image.endswith('jpeg'):
                im = Image.open(image)
                im = im.convert('RGB')
                image_name = image.split('.')[0]
                print(f"This is the image name: {image_name}")
                im.save(f"{image_name}.avif", 'avif', quality = qlt)
            else:
                raise Error
                
    #Delete old files JPG/PNG/WEBP
    files = os.listdir()
    images = [file for file in files if file.endswith(('png', 'JPG', 'jpg', 'webp', 'jpeg'))]
    image_avif = [file for file in files if file.endswith(('avif'))]

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

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return "%s %s" % (s, size_name[i])