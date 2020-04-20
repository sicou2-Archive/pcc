'''A set of classes used to represent ICE and Electric cars.'''

class Car:
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes to desctibe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print(f'This car has {self.odometer_reading} miles on it.')

    def fill_fuel_tank(self):
        '''This simulates filling the fuel tank to full.'''
        print("The fuel tank has been filled to 'FULL'.")