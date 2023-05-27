import cv2 
import os
cont = 2
files = os.listdir() # We list all of the files and folders using os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'jfif', 'jpeg','webp'))]
print(f"These are all of the files in our current working directory: {images}")
filename = 'savedImage.jpeg'

for x in images:
    img=cv2.imread(x)
    #img_75 = cv2.resize(img, (3840, 2160), interpolation = cv2.INTER_LANCZOS4)
    img_75 = cv2.resize(img, None, fx = 0.50, fy = 0.50, interpolation  = cv2.INTER_LANCZOS4)
    cv2.imwrite(filename, img_75)
    filename = 'savedImage ('+str(cont)+').jpeg'
    cont = cont + 1