'''A set of classes that can be used to represent electric cars.'''

from car import Car 

class Battery:
    '''A simple attempt to model a battery for an electric car.'''

    def __init__(self, battery_size=75):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This car has a {self.battery_size}-kWH battery.")

    def get_range(self):
        '''Print a statement about the range this battry provides'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge.')

    def battery_upgrade(self):
        '''This upgrades the battery of the Electric Car.'''
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"Your EV now has a {self.battery_size}-kWH battery.")
        else:
            print("Your EV already has an upgraded battery.")


class ElectricCar(Car):
    '''Represents aspects of a car, specific to electric models.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_fuel_tank(self):
        '''Electric cars do not have fuel tanks.'''
        print("This car does not have a fuel tank!")