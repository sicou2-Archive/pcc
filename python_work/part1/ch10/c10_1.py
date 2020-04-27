filename = 'c:/users/sicou/Learning/pcc/python_work/pcc_review.txt'
#filename = 'text_files/pi_digits.txt'


with open(filename) as file_object:
    lines = file_object.read()
print(lines)

with open(filename) as file_object:
    for line in file_object.readlines():
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())


print('\nNEXT 10-2')

for line in lines:
    if 'Python' in line:
    #Prints only changes
        replaced = line.replace('Python', 'C')
        print(replaced.strip())

print('\nNEXT 10-3 COMMENTED OUT')

# filename = 'text_files/guest.txt'

# guest = input("Welcome to Maison Lorraine, what is your name?\n> ")

# with open(filename, 'w') as file_object:
#     file_object.write(guest)

print('\nNEXT 10-4 COMMENTED OUT')

# filename = 'text_files/guest_book.txt'

# quit_flag = 1

# while quit_flag:
#     with open(filename, 'a') as file_object:
#         welcome_message = "Welcome to Maison Leigh, what is your name?\n> "
#         welcome_message += "When you have typed all names type 'quit' > "
#         guest_sign = input(welcome_message)

#         if guest_sign == 'quit':
#             quit_flag = 0
#         else:
#             file_object.write(f'{guest_sign.title()}\n')

print('\nNEXT 10-5 COMMENTED OUT')

filename = 'text_files/programming_reasons.txt'


while True:

    with open(filename, 'a') as file_object:
        name_message = "What is your name?\n"
        name_message += "Type 'quit' to stop entry.\n> "
        name = input(name_message)

        if name == 'quit':
            break

        reason_message = "What is one reason you love programming?\n> "
        reason_message += "Type 'quit' to stop entry.\n> "
        reason = input(reason_message)
        
        if reason == 'quit':
            break

        file_object.write(f"{name.title()}: {reason}\n")

print('\nNEXT 10-6 and 10-7')

while True:
    print("Choose two numbers to add together.\nType 'q' at any time to "
    "quit.")

    first_response = input("What is your first number?\n> ")
        if first_response == 'q'
            break
    try:
        first_number = int(first_response)
    except ValueError:
        print("That is not a valid number. Please enter a numberic digit.")
        continue
    else:

    try:
        second_number = int(input("What is your first number?\n> "))
    except ValueError:
        print("That is not a valid number. Please enter a numberic digit.")
        continue
    else:
        sum = first_number + second_number
        print(sum)