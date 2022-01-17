import os
a = os.listdir("D:\\DAT\\PYTHON")
for i in a:
	if os.path.isfile(i) == True:
		print(f"File {i}")
	else:
		print(f"Dir {i}")
