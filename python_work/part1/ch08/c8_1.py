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

print('\nNEXT 8_6')

def city_country(city, country):
    c_and_c = f'{city}, {country}'
    return c_and_c.title()

print(city_country('austin', 'texas'))
print(city_country('petoria', 'south africa'))
print(city_country('tillinton', 'england'))
    
print('\nNEXT 8_7 and 8_8')

def make_album(artist, album, songs=None):
        
    if songs:
        music_album = {
            'Artist': artist.title(),
            'Album': album.title(),
            'Number of songs': songs
            }
    else:
        music_album = {
            'Artist': artist.title(),
            'Album': album.title(),
            }
    return music_album

while True: #No I am not going to do another q to quit thing. No. Not now. 
    artist_text = 'Please enter the name of the artist/band. \n>>>'
    album_text = 'Please enter the name of the album. \n>>>'
    songs_text = 'If known please enter the number of songs on the album. \n'
    'Otherwise please leave blank or enter 0 (zero) \n>>>'
    artist = input(artist_text)
    album = input(album_text)
    songs = input(songs_text)
    print(make_album(artist, album, songs))


#print(make_album('boston','dont look back', 5))
#print(make_album('metalica','fuel', 8))
#print(make_album('pink floyd','the wall'))

