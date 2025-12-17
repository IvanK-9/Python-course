# Exercise 9-6: Ice Cream Stand
# Inheriting from Restaurant class (using version from exercise 9-4)

class Restaurant:
    """A simple model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Number of customers served
    
    def describe_restaurant(self):
        """Display information about the restaurant"""
        print(f"Restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        print(f"Restaurant '{self.restaurant_name}' is now open!")


class IceCreamStand(Restaurant):
    """Represents an ice cream stand - a specialized type of restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """
        Initialize attributes of the parent class
        and add ice cream stand specific attributes
        """
        super().__init__(restaurant_name, cuisine_type)
        # Initialize with a list of ice cream flavors
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint chip', 'cookie dough']
    
    def display_flavors(self):
        """Display the available ice cream flavors"""
        print(f"\nAvailable ice cream flavors at '{self.restaurant_name}':")
        for index, flavor in enumerate(self.flavors, 1):
            print(f"{index}. {flavor.title()}")
    
    def add_flavor(self, new_flavor):
        """Add a new ice cream flavor to the list"""
        if new_flavor.lower() not in [f.lower() for f in self.flavors]:
            self.flavors.append(new_flavor)
            print(f"Added new flavor: {new_flavor}")
        else:
            print(f"Flavor '{new_flavor}' is already available")
    
    def remove_flavor(self, flavor_to_remove):
        """Remove an ice cream flavor from the list"""
        if flavor_to_remove in self.flavors:
            self.flavors.remove(flavor_to_remove)
            print(f"Removed flavor: {flavor_to_remove}")
        else:
            print(f"Flavor '{flavor_to_remove}' not found in the list")


# Create an instance of IceCreamStand
my_ice_cream_stand = IceCreamStand("Frosty Delights")

# Use methods from the parent class
print("=== Restaurant Information ===")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()

# Use the child class method to display flavors
print("\n=== Ice Cream Flavors ===")
my_ice_cream_stand.display_flavors()

# Demonstrate adding a new flavor
print("\n=== Adding New Flavors ===")
my_ice_cream_stand.add_flavor("Rocky Road")
my_ice_cream_stand.add_flavor("Chocolate")  # This should show it's already available

# Display updated flavors
print("\n=== Updated Flavor List ===")
my_ice_cream_stand.display_flavors()

# Demonstrate removing a flavor
print("\n=== Removing a Flavor ===")
my_ice_cream_stand.remove_flavor("mint chip")

# Final display
print("\n=== Final Flavor List ===")
my_ice_cream_stand.display_flavors()

# Create another ice cream stand with custom flavors
print("\n" + "="*50)
print("Creating another ice cream stand...")

sweet_treats = IceCreamStand("Sweet Treats", "desserts")
sweet_treats.flavors = ['salted caramel', 'pistachio', 'butter pecan', 'coffee']

print(f"\nWelcome to {sweet_treats.restaurant_name}!")
sweet_treats.describe_restaurant()
sweet_treats.display_flavors()