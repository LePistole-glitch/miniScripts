import os
from PIL import Image

files = os.listdir()
images = [file for file in files if file.endswith(('PNG', 'webp', 'png', 'JPG', 'jpg', 'JPEG', 'jpeg'))]
cont = 1
for i in images:
    data = list(i.getdata())
    image_without_exif = Image.new(i.mode, i.size)
    image_without_exif.putdata(data)

    image_without_exif.save('image_file_without_exif'+cont+".jpg")
    cont = cont + 1