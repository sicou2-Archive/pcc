usernames = ['admin', 'todd', 'betty', 'adam', 'scott', 'sally']

def looping(names):
    if names:
        for name in usernames:
            if name == 'admin':
                print("Welcome, keeper of the keys. The motor is still "
            "running!")
            else:
                print(f"Welcome user {name.title()}!")
    else:
        print("We need to find some users.")

looping(usernames)

print("\n5_9")

empty_names = []
looping(empty_names)

print("\n5_10")

current_names = ['admin', 'toDd', 'betty', 'adam', 'scott', 'sally']
new_names = ['ToDd', 'Jake', 'sammy', 'sally']
current_names_lower = []
new_names_lower = []
def taken_check(current, current_lower, new, new_lower):
    for name in current:
        current_lower.append(name.lower())

    for name in new:
        new_lower.append(name.lower())

    for name in new_lower:
        if name in current_lower:
            print(f"Username: {name} is already taken, please select"
                   " another.")
        else:
            current.append(name)

# I feel that the original name, not the lower name should be put in 
#to current_names, however TLDC

taken_check(current_names, current_names_lower,
            new_names, new_names_lower)
print(current_names, current_names_lower, new_names, new_names_lower)

print("\n5_11")

for num in range(1, 10):
    if num == 1:
        print(f"{str(num)}st")
    elif num == 2:
        print(f"{str(num)}nd")
    elif num == 3:
        print(f"{str(num)}rd")
    else:
        print(f"{str(num)}th")