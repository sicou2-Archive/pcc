import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Unit tests for the Employee Class."""
    
    def setUp(self):
        """
        Initializes a single employee, named 'Scott Carpenter' that makes 
        '100_000' per year, for testing."""
        self.emp_1 = Employee('Scott', 'Carpenter', 100_000)

    def test_give_default_raise(self):
        """Tests 'Scott Carpenter's salary' with a default raise."""
        self.emp_1.give_raise()
        self.assertEqual(105_000, self.emp_1.salary)

    def test_give_custom_raise(self):
        """Tests 'Scott Carpenter's salary' with a 50_000 raise."""
        self.emp_1.give_raise(50_000)
        self.assertEqual(150_000, self.emp_1.salary)

if __name__ == '__main__':
    unittest.main()
