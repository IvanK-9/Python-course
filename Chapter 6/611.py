# Nested dictionaries
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 37_400_000,
        'fact': 'Tokyo is the world\'s most populous metropolitan area'
    },
    'Paris': {
        'country': 'France',
        'population': 2_161_000,
        'fact': 'Paris is known as the "City of Light"'
    },
    'New York': {
        'country': 'United States',
        'population': 8_804_000,
        'fact': 'New York City has over 800 languages spoken'
    }
}

print("\n=== Exercise 6-11: Cities ===")
for city, info in cities.items():
    print(f"\n{city}:")
    print(f"  Country: {info['country']}")
    # Format population with commas
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact']}")