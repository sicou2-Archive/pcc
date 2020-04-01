alice = {'first_name': 'alice', 'last_name': 'maple', 
          'city': 'springfield', 'age': 25, 'hair': 'brown',
          'eye': 'brown'}

for num in alice:
    print(alice[num])

#6_2
print("\nNEXT")
numbers = {'todd': 3, 'sammy': 5, 'joe': 6, 'kyle': 7, 'janice': 1}

for num in numbers:
    print(num.title(), numbers[num])

#6_3 and 6_4
print("\nNEXT")

glossary = {
            'get()': 'Return the value for key if key is in the '
            'dictionary.\n',            
            'def':'The keyword def introduces a function definition.\n',
            'pop()':'If key is in the dictionary, remove it and return '
            'its value.\n',
            'len()':'Return the number of elements in set.\n',
            'iterator':'An object that implements next, which is '
            'expected to return the "next" element of the iterable '
            'object that returned it\n',
            'keys()': 'Return a new view of the dictionary\'s keys\n',
            'values()': 'Return a new view of the dictionary\'s values'
            '\n',
            'items()': 'Return a new view of the dictionary\'s items '
            '((key, value) pairs)\n',
            'sorted()': 'Return a new sorted list from the items in '
            'iterable\n',
            'list()': 'Return a list of all the keys used in the '
            'dictionary\n',
            }

for word in glossary.keys():
    print(word, ': ', glossary[word])

#6_5
print("\nNEXT")

river = {'amazon': 'brazil', 'congo': 'congo', 'orinoco': 'venezuela'}

for water in river:
    print(f'The {water.title()} runs through {river[water].title()}')

print('\nOR DO THIS')

for water, country in river.items():
    print(f"The {water.title()} runs through {country.title()}.")


#####STOPPED ON 6-6