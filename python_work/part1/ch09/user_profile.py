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
                print("\tHas a significant other.")
            if self.pet == 1:
                print("\tHas at least one pet.")
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

