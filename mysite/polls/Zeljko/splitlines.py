input = open('MiddleFile', 'r')
seed = input.read()
lineas = seed.split('\n')
for i in lineas:
	print(i)
print(type(lineas))
print(lineas[1])