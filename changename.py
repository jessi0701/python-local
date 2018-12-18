import os
import glob

os.chdir(r'C:\Users\student\nokgu\SSAFY지원자')

for filename in os.listdir("."):
    new_filename = filename.replace("SAMSUNG_","SSAFY_")
    os.rename(filename, new_filename)