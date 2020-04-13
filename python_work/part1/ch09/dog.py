class Dog:
    '''A simple attempt to model a dog.'''

    def __init__(self, name, age):
        '''Initialize name and attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command.'''
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        '''Simulate a dog rolling over in reaponse to a command.'''
        print(f"{self.name.title()} rolled over!")
        