from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 42
my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
# my_used_car.fill_fuel_tank()

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.update_odometer(12)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
