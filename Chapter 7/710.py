responses = {}
polling_active = True

print("Dream Vacation Poll!")
print("(Enter 'quit' to stop the poll.)")

while polling_active:
    name = input("\nWhat is your name? ")
    if name.lower() == 'quit':
        break

    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")
