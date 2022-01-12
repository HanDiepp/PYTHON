f = open('a1.txt', 'r')
data = f.read()
for i in range(len(data)):
	print(data.splitlines())

