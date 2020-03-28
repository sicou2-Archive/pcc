dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Does not work
#dimensions[0] = 250
#print(dimensions[0])

my_tuple = (3,)
my_tup = 15,
print(my_tuple, my_tup)

print('\nLoop through tuple')
for dimension in dimensions:
	print(dimension)

print('Writing over tuple')
print('Original dimensions:')
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
for dimension in dimensions:
	print(dimension)

	