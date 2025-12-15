def build_profile(first, last, **user_info):
    """Build a dictionary containing user profile info."""
    profile = {
        'first_name': first,
        'last_name': last
    }
    # Add any additional key-value pairs
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build my profile
my_profile = build_profile(
    'Alice',
    'Smith',
    age=30,
    city='Seattle',
    occupation='Software Engineer'
)

print(my_profile)
