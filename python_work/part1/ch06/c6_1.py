alice = {'first_name': 'alice', 'last_name': 'maple', 
          'city': 'springfield', 'age': 25, 'hair': 'brown',}

for num in alice:
    print(alice[num])

#6_2
print("\nNEXT 6_2 and 6-10")
numbers = {'todd': [3, 4, 6, 8,], 
           'sammy': [5, 7, 3, 8,], 
           'joe': [6,], 
           'kyle': [7, 3,], 
           'janice': [3, 9, 1],
           }

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


print("\nNEXT 6-7")

alice = {'first_name': 'alice', 'last_name': 'maple', 
          'city': 'springfield', 'age': 25, 'hair': 'brown',
          'eye': 'brown'}
bob = {'first_name': 'bob', 'last_name': 'aspen', 
          'city': 'shelbyville', 'age': 24, 'hair': 'blonde',
          'eye': 'green'}

people = [alice, bob]

for person in people:
    first_last = (f"Full name: {person['first_name'].title()}"
                  f"{person['last_name'].title()}.")
    print(first_last)
    print(f"Location: {person['city'].title()}.")
    description = (f"Age: {person['age']}, " 
                   f"Hair: {person['hair'].title()}, "
                   f"Eyes: {person['eye'].title()}.\n")
    print(description)

print("\nNEXT 6-7")

trevor = {
      'name': 'trevor',
      'owner': 'adam',
      'toy': 'stick',
      }

dally = {
      'name': 'dally',
      'owner': 'bob',
      'toy': 'catnip',
      }

hero = {
      'name': 'hero',
      'owner': 'charlie',
      'toy': 'ball',
      }

pets = [trevor, dally, hero]

for pet in pets:
    print(f"PET NAME: {pet['name'].title()}\n\tPET OWNER: "
          f"{pet['owner'].title()}\n\t FAVORITE TOY: "
          f"{pet['toy'].title()})")
print("\nNEXT 6-8")

favorite_places = {
               'alice': ['austin', 'houston', 'greece'],
               'bob': ['seattle', 'author'],
               'charlie': ['channington'],
               }
for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are: ", end=' ')
    for place in places:
        print(f"{place.title()}", end=', ')
    print('\n')

print('\nNEXT 6-11')

cities = {
          'paris': 
           {'country': 'france',
            'language': 'french',
            'word': 'food',
            },
          'perth': 
           {'country': 'australia',
            'language': 'english',
            'word': 'sun',
            },
          'moscow':
           {'country': 'russia',
            'language': 'russian',
            'word': 'cold',
            },
          }

for city, facts in cities.items():
    print(city.title())
    for item, fact in facts.items():
        print(f'\t{item.title()}: {fact.title()}')