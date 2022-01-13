f = open('a1.txt', 'r')
data1 = f.readline()
data2 = f.readline()
data3 = f.readline()
print(f"+ {data1}")
print(f"+ {data2}")
print(f"+ {data3}")

f = open('a1.txt', 'r')
data = f.read()
l = data.splitlines()
for i in range(len(l)):
	print(f'+ {l[i]}')

