# Creating all people dictionaries directly in the list
people = [
    {
        'first_name': 'Marie',
        'last_name': 'Curie',
        'age': 66,
        'location': 'Paris'
    },
    {
        'first_name': 'Albert',
        'last_name': 'Einstein',
        'age': 76,
        'location': 'Princeton'
    },
    {
        'first_name': 'Nikola',
        'last_name': 'Tesla',
        'age': 86,
        'location': 'New York'
    }
]

# Looping through the list and printing information
for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"Location: {person['location']}")
    print()  # Blank line between people