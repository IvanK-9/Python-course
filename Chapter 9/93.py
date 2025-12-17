class User:
    """A class to represent a user."""
    
    def __init__(self, first_name, last_name, age, city, occupation):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.occupation = occupation
        self.login_attempts = 0  # Additional attribute for tracking login attempts
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print("User information:")
        print(f"  First name: {self.first_name}")
        print(f"  Last name: {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  City: {self.city}")
        print(f"  Occupation: {self.occupation}")
        print(f"  Login attempts: {self.login_attempts}")
    
    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name} {self.last_name}! Nice to see you again!")
    
    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


# Create several users
user1 = User("Anna", "Ivanova", 25, "Moscow", "Engineer")
user2 = User("Peter", "Sidorov", 30, "Saint Petersburg", "Designer")
user3 = User("Maria", "Petrova", 28, "Kazan", "Teacher")

# Call methods for each user
print("User 1:")
user1.describe_user()
user1.greet_user()
print()

# Simulate login attempts for user1
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"{user1.first_name} has attempted to log in {user1.login_attempts} times")
user1.reset_login_attempts()
print(f"After reset: {user1.login_attempts} attempts")
print()

print("User 2:")
user2.describe_user()
user2.greet_user()
print()

print("User 3:")
user3.describe_user()
user3.greet_user()