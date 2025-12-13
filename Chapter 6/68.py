# Create all pet dictionaries directly in the list
pets = [
    {
        'animal': 'dog',
        'owner': 'sarah'
    },
    {
        'animal': 'cat',
        'owner': 'michael'
    },
    {
        'animal': 'rabbit',
        'owner': 'emma'
    },
    {
        'animal': 'hamster',
        'owner': 'lucas'
    }
]

# Loop through the list and print info about each pet
for pet in pets:
    print(f"\nHere's what I know about this pet:")
    print(f"  Animal type: {pet['animal']}")
    print(f"  Owner's name: {pet['owner']}")