file_name = 'text_files/pi_digits.txt'


with open(file_name) as file_object:
    contents = file_object.read()
print(contents) 
#NO CLUE WHAT HE MEANS HERE WITH rstrip() THERE IS NOT \n UNACCOUNTED FOR

print("\nNEXT")

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\nNEXT")

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print("\nNEXT")

next_file_name = 'text_files/pi_million_digits.txt'

with open(next_file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:50]}")
print(len(pi_string))

print("\nNEXT")


next_file_name = 'text_files/pi_million_digits.txt'

with open(next_file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:50]}")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")