def build_profile(first, last, **user_info):
    """
    Build a user profile dictionary with first/last names and additional info.

    Args:
        first (str): First name of the user.
        last (str): Last name of the user.
        **user_info: Arbitrary keyword arguments for additional profile data.

    Returns:
        dict: Dictionary containing all user information.
    """
    profile = {
        'first_name': first,
        'last_name': last
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile
