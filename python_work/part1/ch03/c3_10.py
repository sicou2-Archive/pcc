pets = ['dog', 'cat', 'rat']
print(pets[0])
print(pets[0].title())

print(pets[-1])

message = f'My 1st pet was a {pets[0].title()}'
print(message)

pets.append('goose')
pets[3] = 'mouse'

print(pets)

pets.append('snake')
pets.insert(2, 'hawk')
pets.insert(3, 'kangaroo')

print(pets)

del pets[3]
print(pets)

pop_pet = pets.pop()
print(pop_pet)
print(pets)

pop_spot = pets.pop(2)
print(pop_spot)
print(pets)

annoy_pet = 'mouse'
pets.remove('mouse')
print(annoy_pet, pets)

pets.reverse()
print(pets, 'reversed')
pets.reverse()
print(pets, 're-reversed')

print(sorted(pets), 'sorted')

pets.sort()
print(pets, 'sort')

pets.sort(reverse = True)
print(pets, 'sort,rev')

pet_len = len(pets)
print(pet_len)

print(pets[-1])



