class Employee:
    """A class representing an employee with first name, last name, and annual salary."""
    
    
    def __init__(self, first_name, last_name, annual_salary):
        """
        Initializes an employee instance.
        
        Args:
            first_name (str): Employee's first name
            last_name (str): Employee's last name
            annual_salary (float): Annual salary in dollars
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    
    def give_raise(self, amount=5000):
        """
        Increases the employee's annual salary by a specified amount.
        Default raise is $5,000.
        
        Args:
            amount (float): The raise amount in dollars (default: 5000)
        """
        self.annual_salary += amount
