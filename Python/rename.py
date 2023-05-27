import os
cont = 1
files = os.listdir() # We list all of the files and folders using os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'jfif'))]

for x in images:
    os.rename(x, "Mikomi Honika - Sonico_("+str(cont)+").png")
    cont = cont + 1