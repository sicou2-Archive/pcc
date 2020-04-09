def get_formatted_name(first_name, middle_name='', last_name=''):
    '''Return a full name, neatly formatted.'''
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    elif last_name:
        full_name = f'{first_name} {last_name}'
    else:
        full_name = f'{first_name}'

    return full_name.title()



musician = get_formatted_name('jimi', 'hendrix')
print(musician)

magician = get_formatted_name('teller')
print(magician)

blues = get_formatted_name('john', 'lee', 'hooker')
print(blues)