# 1: making dictionaries for three people
person_1 = {
    'first_name': 'Marie',
    'last_name': 'Curie',
    'age': 66,
    'location': 'Paris'
}

person_2 = {
    'first_name': 'Albert',
    'last_name': 'Einstein',
    'age': 76,
    'location': 'Princeton'
}

person_3 = {
    'first_name': 'Nikola',
    'last_name': 'Tesla',
    'age': 86,
    'location': 'New York'
}

# Step 2: creating a list of these dictionaries
people = [person_1, person_2, person_3]

# Step 3: looping through the list and printing information
for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"Location: {person['location']}")
