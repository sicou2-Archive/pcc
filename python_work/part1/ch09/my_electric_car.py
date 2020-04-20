from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_fuel_tank()
my_tesla.battery.get_range()
my_tesla.battery.battery_upgrade()
my_tesla.battery.get_range()