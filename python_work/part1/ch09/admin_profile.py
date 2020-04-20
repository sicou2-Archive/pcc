import user_profile

class Admin(user_profile.User):
    ''' This creates an Administrators profile. '''

    def __init__(self, first_name, last_name, pet=0, sig_other=0):
        '''
        This initializes User arguments and defines the Admin's privledges.
        '''
        super().__init__(first_name, last_name, pet, sig_other)
        self.privledges = Privledges()


class Privledges:
    ''' This is a basic unit for Privledges and how they are applied. '''

    def __init__(self):
        self.privledges = [
            'can add post',
            'can edit post',
            'can correct truth', 
            'can judge LOYALTY',
            ]

    def show_privledges(self):
        ''' This prints the list of the Administrator's privledges. '''

        print("This citizan may: ")
        for privledge in self.privledges:
            print(f"\t - {privledge}")