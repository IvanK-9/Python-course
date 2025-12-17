class Restaurant:
    """A class to represent a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes for restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print information about the restaurant."""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"The restaurant '{self.restaurant_name}' is open!")

# Create three different restaurant instances
restaurant1 = Restaurant("Italian Pizza", "Italian cuisine")
restaurant2 = Restaurant("Sakura Sushi Bar", "Japanese cuisine")
restaurant3 = Restaurant("Burger King", "American cuisine")

# Call describe_restaurant() for each restaurant
print("Restaurant 1:")
restaurant1.describe_restaurant()
print()

print("Restaurant 2:")
restaurant2.describe_restaurant()
print()

print("Restaurant 3:")
restaurant3.describe_restaurant()