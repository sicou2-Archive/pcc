#rental = input("What make of car would you like to rent? ")

# print(f"Let me see if I can find a {rental} for you to drive.")

# print('\nNEXT 7_2')

# party_size = int(input("How many people will be dining with you this "
#                    "evening? "))
# if party_size >= 8:
#     print("Please wait a few moments while we get a table ready for "
#           "you.")
# else:
#     print("We have seating available for you right over here.")

# print('\nNEXT 7_3')

#number = int(input('Please enter any number. '))

# if (number % 10) == 0:
#     print(f"The number {number} is a multiple of 10.")
# else:
#     print(f"The number {number} is not a multiple of 10.")

# print('\nNEXT 7_4')

# prompt = "Whad'ya wan' on ya' pie?"
# prompt += "\nType 'quit' to complete order.\n> "

# flag = 1

# while flag:
#     request = input(prompt)
#     print("Aigh't, but it'll cost ya!")

#     if request == 'quit':
#         flag = False #see what I did there?

# print('\nNEXT 7_5')

# prompt = "Please enter age for ticket price. "
# prompt += "Type 'quit' to complete transaction. "

# while True:
#     age = input(prompt)
    
#     try:
#         age_int = int(age)
#     except ValueError:
#         if age == 'quit':
#             break
#         else:
#             print("Please enter a valid age, or 'quit'.")
#             continue
    
#     if age_int < 3:
#         print("Under 3 is free, enjoy!")
#     elif age_int < 13:
#         print("Ages 3 to 12 are $10, enjoy!")
#     else:
#         print("Ages 13 and up are $15, enjoy!")
        
# print('\nNEXT 7_6\n DONE')

# print('\nNEXT 7_7')

# x = 1
# z = 1
# while True:
#     print(x)

#     x += 1

#     print(x)
#     #tried to Fibinachi and just... no. 

print('\nNEXT 7_8 and 7_9')
sandwich_orders = ['bacon', 'pastrami','baked bean', 'pastrami',
                   'barbecue', 'pastrami', 'blt', 'pastrami', 
                   'british rail',]
finished_sandwiches = []

print('Sorry folks, we are all out of pastrami, you are going to need'
    ' to choose another sandwich.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f"Next up, {sandwich}!")
        making = sandwich_orders.pop(0)
        finished_sandwiches.append(making)

print("All of the sandwich orders have been made!")
print(finished_sandwiches)

print('\nNEXT 7_10')

dream_vacation = {}

stop_flag = True

while stop_flag:

    print('Where is a dream vacation for you? ')
    vacation = input('> ')

    print('What would you like to do there? ')
    event = input('> ')

    dream_vacation[vacation] = event

    print('Is there anywhere else you want to go? (y/ n) ')
    proceed = input('> ')
    if proceed == 'n':
        stop_flag = 0

for vacation, event in dream_vacation.items():
    print(f'You want to go to {vacation} and {event.lower()}.')

print('That sounds fun!')

