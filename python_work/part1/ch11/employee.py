class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first = first_name
        self.last = last_name
        self.salary = annual_salary

    def give_raise(self, give_raise=5_000):
        self.salary += give_raise
#       print(self.salary)

#emp_1 = Employee('scott', 'carpenter', 75_000)

#emp_1.give_raise()
#emp_1.give_raise(10_000)