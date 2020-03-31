alien_color = "green"
if alien_color == 'green':
    print("You have earned five points!")

print("Next part")

if alien_color == 'red':
    print("That was a friendly! Lose five points!")

print("No output")

print("\n5_4")

if alien_color == 'green':
    print("You have earned five points!")
else:
    print("You have earned ten points!")

print("Run the else block")
alien_color = 'red'

if alien_color == 'green':
    print("You have earned five points!")
else:
    print("You have earned ten points!")

print("\n5_5")

def color_check(check):
    if check == 'green':
        print("You have earned five points!")
    elif check == "yellow":
        print("You have earned ten points!")
    elif check == 'red':
        print("You have earned 15 points!")
    else: 
        print("MISTAKE")    
alien_color = ['green', 'yellow', 'red']

for color in alien_color:
    color_check(color)

print("\n5_6")

age = [1, 3, 5, 13, 50, 69, 100]
def age_check(age):
    if age < 2:
        print("BABY")
    elif age < 4:
        print("TODDLER")
    elif age < 13:
        print("KID")
    elif age < 20:
        print("TEEN")
    elif age < 65:
        print("ADULT")
    elif age >= 65:
        print("ELDER")
    else:
        print("INPUT ERROR")
for year in age:
    age_check(year)

print('\n5-7')

fruit = ['apple', 'orange', 'pear']

if 'apple' in fruit:
    print("You really like apples")
if 'grape' in fruit:
    print("You really like grapes")
if 'banana' in fruit:
    print("You really like bananas")
if 'pear' in fruit:
    print("You really like pears")
if 'pineapple' in fruit:
    print("You really like pineapples")