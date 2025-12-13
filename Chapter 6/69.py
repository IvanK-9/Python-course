# Dictionary with lists as values
favorite_places = {
    'Sarah': ['Paris', 'Tokyo', 'New York'],
    'Michael': ['Hawaii', 'Swiss Alps'],
    'Emma': ['Sydney', 'Rome', 'Bali', 'Cape Town']
}

# Alternative: Asking friends (simulated with input)
# In real scenario, you could ask friends and add their responses
friends_places = {}
friends = ['Alex', 'Jamie', 'Taylor']

# Simulating friend responses (in practice, use input())
for friend in friends:
    if friend == 'Alex':
        friends_places[friend] = ['Grand Canyon', 'Yellowstone']
    elif friend == 'Jamie':
        friends_places[friend] = ['London', 'Edinburgh', 'Dublin']
    else:
        friends_places[friend] = ['Barcelona']

# Combining both dictionaries
all_places = {**favorite_places, **friends_places}

print("\n=== Exercise 6-9: Favorite Places ===")
for person, places in all_places.items():
    print(f"\n{person}'s favorite places:")
    for place in places:
        print(f"  • {place}")