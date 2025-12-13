# Basic solution
print("=== Exercise 7-4: Pizza Toppings ===")
print("Enter the toppings you want on your pizza.")
print("Enter 'quit' when you're done.\n")

while True:
    topping = input("Enter a pizza topping: ").strip().lower()
    
    if topping == 'quit':
        print("\nYour pizza is being prepared!")
        break
    else:
        print(f"  I'll add {topping} to your pizza.")