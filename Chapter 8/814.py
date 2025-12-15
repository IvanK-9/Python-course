def make_car(manufacturer, model, **options):
    """Builds a car dictionary with required and optional features."""
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    # Add all additional options
    for key, value in options.items():
        car[key] = value
    return car

# Create a car with additional features
car = make_car(
    'subaru',
    'outback',
    color='blue',
    tow_package=True,
    sunroof=False,
    year=2023
)

# Print the resulting dictionary
print(car)
