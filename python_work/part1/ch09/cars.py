class Car:
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes to desctibe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desctiptive_name(self):
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

class ElectricCar(Car):
    '''Represents aspects of a car, specific to electric models.'''

    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class.'''
        super().__init__(make, model, year)

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_desctiptive_name())

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_desctiptive_name())

my_new_car.odometer_reading = 42
my_new_car.read_odometer()

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()


my_used_car.update_odometer(12)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_desctiptive_name())