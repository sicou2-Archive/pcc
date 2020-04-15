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

my_dog = Dog('Willie', 6)
your_dog = Dog('Gypsy', 11)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()


print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
my_dog.roll_over()