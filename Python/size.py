import os
import math
size = 0
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


files = os.listdir() # We list all of the files and folders using os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'jfif'))]
for x in images:
        size = size + os.stat(x).st_size
        
print(convert_size(size))