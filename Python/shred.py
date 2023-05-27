import os
images = [file for file in os.listdir() if file.endswith(('png'))]
file_name = images.pop(0)
f = open(file_name,'wb')
f.write("00110111110001010100010001001");
f.close()
os.rename(file_name,'abf09i')
#os.unlink('abf09i')
print(file_name + " shredded successfully")