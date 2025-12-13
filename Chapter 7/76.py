print("=== Exercise 7-6: Three Exits ===")

print("\n--- Version 1: Conditional test in while statement ---")
topping = ""
while topping.lower() != 'quit':
    topping = input("Enter topping (or 'quit' to stop): ")
    if topping.lower() != 'quit':
        print(f"Adding {topping} to your pizza.")

print("\n--- Version 2: Active variable to control loop ---")
active = True
toppings_list = []
while active:
    topping = input("Enter topping (or 'quit' to stop): ").strip()
    
    if topping.lower() == 'quit':
        active = False
    elif topping.lower() == 'done':
        active = False
    elif topping == "":
        print("Please enter a topping or 'quit'.")
    else:
        toppings_list.append(topping)
        print(f"Added {topping}. Current toppings: {', '.join(toppings_list)}")

print(f"\nFinal pizza toppings: {', '.join(toppings_list)}")

print("\n--- Version 3: Break statement ---")
print("Enter pizza toppings. Type 'finished' when done.")

while True:  # This loop runs forever until break
    topping = input("Topping: ").strip()
    
    if topping.lower() in ['finished', 'done', 'quit', 'stop']:
        print("Order complete!")
        break
    elif not topping:  # Empty input
        continue
    else:
        print(f"Adding {topping}...")