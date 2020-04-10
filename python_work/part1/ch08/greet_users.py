def greet_users(names):
    '''Print a simple greeting to each user in the list'''
    for name in names:
            msg = f"Howdy, {name.title()}!"
            print(msg)

usernames = ['dog', 'gypsy', 'hans', 'blaze']
greet_users(usernames)

