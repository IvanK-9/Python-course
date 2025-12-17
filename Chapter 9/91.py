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


# Create a restaurant instance
restaurant = Restaurant("Golden Dragon", "Chinese cuisine")

# Print attributes individually
print(f"Name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")
print()

# Call methods
restaurant.describe_restaurant()
print()
restaurant.open_restaurant()