import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test cases for the Employee class using setUp fixture."""
    
    def setUp(self):
        """Creates a common employee instance for all test methods."""
        self.employee = Employee('Alice', 'Johnson', 70000)
    
    def test_give_default_raise(self):
        """Verifies that default $5,000 raise works as expected."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 75000)
    
    def test_give_custom_raise(self):
        """Verifies that custom raise amount is correctly applied."""
        self.employee.give_raise(15000)
        self.assertEqual(self.employee.annual_salary, 85000)

if __name__ == '__main__':
    unittest.main()
