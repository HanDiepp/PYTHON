# import os
# os.listdir("D:\\DAT\\PYTHON")
# print(os.listdir("D:\\DAT\\PYTHON"))


import glob

src = "./Folder1"
obj_list = glob.glob(src +"/**", recursive=True)
print(obj_list)
import os
os.listdir("D:\\DAT\\PYTHON\\Folder1")
print(os.listdir("D:\\DAT\\PYTHON\\Folder1"))
