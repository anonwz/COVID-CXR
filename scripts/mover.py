import shutil
import os.path
import os
from shutil import copyfile

src = 'G:/BrixData/BRIXALLDICOM' #source folder
dst = 'G:/BrixData/brixparsev3/18' #destination folder

count = 0
with open('G:/BrixData/18.txt', 'r') as openfile:
    Lines = openfile.readlines()
    for line in Lines:
         check_file = os.path.exists(src + '/' +  Lines[count].strip())
         if check_file == True:
             tmp = src + '/' + str(Lines[count].strip())
             shutil.move(tmp, dst)
         count+=1
