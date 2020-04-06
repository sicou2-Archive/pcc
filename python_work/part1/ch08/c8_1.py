def display_message():
    '''Displays a summary of what was learned in Chapter 8'''
    print('We learned about creating and using Functions in the Python '
        'programming\n language!')

display_message()

print('\nNEXT 8_2')

def favorite_book(book):
    '''Displays the title of the users favorite book'''
    print(f'My favorite book is "{book.title()}".')

favorite_book('where is joe merchant')

print('\nNEXT 8_3 and 8_4')

def make_shirt(size, message='I love Python'):
    '''Informs the user of the size of shirt and message requested.'''
    print(f"The size of the shirt will be {size}. The message will have"
            f" a badass typeset,\nwith bold colors, and say, "
            f"'{message}'.")

make_shirt('S', 'Howdy dammit!')
print('Next shirt')
make_shirt('L')
print('Next shirt')
make_shirt('M')

print('\nNEXT 8_5')

def describe_city(city, country='Canada'):
    print(f"{city.title()} is in {country.title()}")

describe_city('montreal')
describe_city('toronto')
describe_city('london', 'england')
