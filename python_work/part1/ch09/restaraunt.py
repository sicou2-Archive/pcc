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