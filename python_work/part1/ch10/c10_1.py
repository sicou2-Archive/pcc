import json

#filename = 'c:/users/sicou/Learning/pcc/python_work/pcc_review.txt'
#filename = 'text_files/pi_digits.txt'


# with open(filename) as file_object:
#     lines = file_object.read()
# print(lines)

# with open(filename) as file_object:
#     for line in file_object.readlines():
#         print(line.strip())

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.strip())


print('\nNEXT 10-2 COMMENTED OUT')

# for line in lines:
#     if 'Python' in line:
#     #Prints only changes
#         replaced = line.replace('Python', 'C')
#         print(replaced.strip())

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

# filename = 'text_files/programming_reasons.txt'


# while True:

#     with open(filename, 'a') as file_object:
#         name_message = "What is your name?\n"
#         name_message += "Type 'quit' to stop entry.\n> "
#         name = input(name_message)

#         if name == 'quit':
#             break

#         reason_message = "What is one reason you love programming?\n> "
#         reason_message += "Type 'quit' to stop entry.\n> "
#         reason = input(reason_message)
        
#         if reason == 'quit':
#             break

#         file_object.write(f"{name.title()}: {reason}\n")

print('\nNEXT 10-6 and 10-7 COMMENTED OUT')

# while True:
#     print("Choose two whole numbers to add together.\nType 'q' at any time to "
#     "quit.")

#     first_response = input("What is your first number?\n> ")
#     if first_response == 'q':
#         break
#     try:
#         first_number = int(float(first_response))
#     except ValueError:
#         print("That is not a valid number. Please enter a numberic digit.")
#         continue

#     second_response = input("What is your second_number?\n> ")

#     if second_response == 'q':
#         break

#     try:
#         second_number = int(float(second_response))
#     except ValueError:
#         print("That is not a valid number. Please enter a numberic digit.")
#         continue
#     else:
#         sum = first_number + second_number
#         print(sum)

print('\nNEXT 10-8 and 10-9')

filename = ['text_files/cats.txt', 'text_files/dogs.txt', 'fammit.txt']



for file in filename:
    try:
        with open(file) as f:
            print(f'\n{file}')
            text = f.readlines()
    except:
#        print(f"\n{file} was not found.")
        pass            
    else:
        for name in text:
            print(name.strip())

print('\nNEXT 10-10 COMMENTED OUT')

# filename = [
#         'text_files/alice.txt', 'text_files/cats.txt', 'text_files/dogs.txt',
#         'text_files/guest.txt', 'text_files/guest_book.txt', 
#         'text_files/little_women.txt', 'text_files/moby_dick.txt',
#         'text_files/pi_digits.txt', 'text_files/pi_million_digits.txt',
#         'text_files/programming.txt', 'text_files/programming_reasons.txt',
#         ]

# for file in filename:
#     with open(file, encoding='utf-8') as f:
#         text = f.read()
#         times = text.lower().count(' happy ')
#         print(file, times)

print('\nNEXT 10-11 and 10-12')

try:
    filename = 'text_files/favorite_number.json'
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        number = input("What is your favorite number? ")
        json.dump(number, f)


if number:
    print(f"Your favorite number is {number}!")
