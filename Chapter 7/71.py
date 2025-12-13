print("=== Exercise 7-1: Rental Car (Enhanced) ===")

# List of available cars for validation
available_cars = ['toyota', 'honda', 'ford', 'subaru', 'bmw', 'tesla']

while True:
    car = input("What kind of rental car would you like? ").lower().strip()
    
    if car in available_cars:
        print(f"Great choice! Let me see if I can find you a {car.title()}.")
        break
    else:
        print(f"Sorry, we don't have {car.title()} in our fleet.")
        print(f"Available cars: {', '.join([c.title() for c in available_cars])}")
        try_again = input("Would you like to choose another car? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thank you for visiting!")
            breakv