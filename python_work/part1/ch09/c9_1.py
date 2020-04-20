import restaraunt, user_profile, admin_profile, random

print("NEXT 9_1 and 9_2")

#Restaraunt class moved to restaraunt.py

tonys = restaraunt.Restaraunt('tony\'s', 'pizza')
garden = restaraunt.Restaraunt('the garden', 'french')
pit = restaraunt.Restaraunt('the pit', 'BBQ')

tonys.describe_restaraunt(); tonys.open_restaraunt()
garden.describe_restaraunt(); garden.open_restaraunt()
pit.describe_restaraunt(); pit.open_restaraunt()

print('\nNEXT 9_3')

#User class moved to user_profile.py

user_1 = user_profile.User('alice', 'alington', 0, 0)
user_2 = user_profile.User('bob', 'bobbart', 0, 1)
user_3 = user_profile.User('charlie', 'chazville', 1, 0)
user_4 = user_profile.User('dan', 'daniael', 1, 1)

user_1.describe_user(); user_2.describe_user(); user_3.describe_user();
user_4.describe_user(); user_1.greet_user(); user_2.greet_user()
user_3.greet_user(); user_4.greet_user()

print('\nNEXT 9_4')

tonys.number_served = 199; print(tonys.number_served)
tonys.increment_number_served(34); print(tonys.number_served)

print('\nNEXT 9_5')

user_1.increment_login_attempts(); user_1.increment_login_attempts()
user_1.increment_login_attempts(); user_1.increment_login_attempts()
user_1.reset_login_attempts(); user_1.increment_login_attempts()

print('\nNEXT 9_6')

class IceCreamStand(restaraunt.Restaraunt):
    """This represents a restaraunt, specifically an Ice Cream Stand"""
    def __init__(self, restaraunt_name, cuisine_type):
        """
        This inherits the parent arguments and defines the available flavors.
        """
        super().__init__(restaraunt_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'coffee']

    def display_flavors(self):
        """ This shows the available flavors. """
        print("That flavors available today are: ")
        for flavor in self.flavors:
            print(f"\t-> {flavor.title()}")

shivers = IceCreamStand('shivers ice cream', 'desert')
shivers.display_flavors

print('\nNEXT 9-7 and 9_8')

#Privledges class moved to admin_profile.py
#Admin class moved to admin_profile.py

user_5 = admin_profile.Admin('ellen', 'shields', 1, 1)
user_5.describe_user()
user_5.privledges.show_privledges()

print('\nNEXT 9-13')

class Die:
    """This simulates a single, user selected sided die"""

    def __init__(self, sides=6):
        """This initializes the class with a die side default of 6."""
        self.sides = sides

    def roll_die(self):
        """This simulates the rolling of a die."""
        rolls = int(input("How many time would you like to roll the die? "))

        for roll in range(rolls):
            print(f'The die rolls a "{random.randint(1, self.sides)}"!')

blue = Die(10)

#blue.roll_die()

red = Die(20)

#red.roll_die()

print('\nNEXT 9-14')

lottery_numbers = (
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',    
    )
winning_numbers = []
my_ticket = []

for i in range(6):
        my_number = random.choice(lottery_numbers)
        my_ticket.append(my_number)

print(my_ticket)

attempts = 0

while sorted(my_ticket) != sorted(winning_numbers) and attempts <= 200000:
    
    winning_numbers = []

    for i in range(6):
        winning_number = random.choice(lottery_numbers)
        winning_numbers.append(winning_number)

    attempts += 1
    print(attempts)

print(f"Tonight's winning lotter numbers are {sorted(winning_numbers)}!")
print(f"It took you {attempts} to win the lottery one time.")
print(sorted(winning_numbers), (sorted(my_ticket)))