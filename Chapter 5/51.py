# 5-1. Conditional Tests

# Test 1: Car brand check
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')    # False

# Test 2: Age check
age = 25
print("\nIs age > 18? I predict True.")
print(age > 18)         # True

print("\nIs age < 20? I predict False.")
print(age < 20)         # False

# Test 3: Username check
username = 'Alex'
print("\nIs username.lower() == 'alex'? I predict True.")
print(username.lower() == 'alex')  # True

print("\nIs username == 'alex'? I predict False.")
print(username == 'alex')          # False (case matters)

# Test 4: Number check
number = 42
print("\nIs number == 42? I predict True.")
print(number == 42)     # True

print("\nIs number != 42? I predict False.")
print(number != 42)     # False

# Test 5: List check
fruits = ['apple', 'banana', 'orange']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)  # True

print("\nIs 'grape' in fruits? I predict False.")
print('grape' in fruits)   # False

# Test 6: Using 'and' operator
temperature = 22
print("\nIs temperature between 20 and 25? I predict True.")
print(temperature >= 20 and temperature <= 25)  # True

print("\nIs temperature between 25 and 30? I predict False.")
print(temperature >= 25 and temperature <= 30)  # False