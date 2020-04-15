print("NEXT 9_1 and 9_2")

class Restaraunt:
    '''This is a basic representation of a restaraunt'''

    def __init__(self, restaraunt_name, cuisine_type):
        '''Initialize basic facts about the restaraunt'''
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaraunt(self):
        '''This are the basic facts about the restaraunt'''
        print(f"The name of the restaraunt is: {self.restaraunt_name.title()}."
            f"\nThe cuisine type is : {self.cuisine_type}. That sounds great!")

    def open_restaraunt(self):
        '''This indicates if the restaraunt is open'''
        print(f"{self.restaraunt_name.title()} is currently open! Lets go!")

    def increment_number_served(self, served_today):
        '''This increases the total number served by todays served total.'''
        self.number_served += served_today


tonys = Restaraunt('tony\'s', 'pizza')
garden = Restaraunt('the garden', 'french')
pit = Restaraunt('the pit', 'BBQ')

tonys.describe_restaraunt()
tonys.open_restaraunt()

garden.describe_restaraunt()
garden.open_restaraunt()

pit.describe_restaraunt()
pit.open_restaraunt()

print('\nNEXT 9_3')

class User:
    '''This creates a citizens user profile'''
    def __init__(self, first_name, last_name, pet=0, sig_other=0):
        '''Initialize the citizen's information'''
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.sig_other = sig_other
        self.fullname = first_name.title() + ' ' + last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        '''This is the ZONE citizen's profile'''
        print(f"\nUSER DATA for: {self.fullname}")

        if self.sig_other == 1 or self.pet == 1:
            if self.sig_other == 1:
                print("Has a significant other.")
            if self.pet == 1:
                print("Has at least one pet.")
        else:
            print("We have no further valid data.")

    def greet_user(self):
        '''
        This distrubues a friendly greeting to the citizen with 
        gentle encouragement for LOYALTY
        '''

        print(f"\n{self.fullname}! The ZONE hopes you are happy!")

        if self.sig_other == 1 or self.pet == 1:
            if self.sig_other == 1:
                print("We trust your life partner is remaining LOYAL!")
            if self.pet == 1:
                print("We trust you will remain LOYAL for your pets sake.")
        else:
            print("LOYALTY is the key to life!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Number of login attempts: {self.login_attempts}.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts reset.")




user_1 = User('alice', 'alington', 0, 0)
user_2 = User('bob', 'bobbart', 0, 1)
user_3 = User('charlie', 'chazville', 1, 0)
user_4 = User('dan', 'daniael', 1, 1)

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()
user_4.describe_user()

user_1.greet_user()
user_2.greet_user()
user_3.greet_user() 
user_4.greet_user()

print('\nNEXT 9_4')

tonys.number_served = 199
print(tonys.number_served)
tonys.increment_number_served(34)
print(tonys.number_served)

print('\nNEXT 9_5')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
user_1.increment_login_attempts()

