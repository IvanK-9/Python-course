print("\n=== Exercise 7-7: Infinity Loop ===")
print("WARNING: This will create an infinite loop!")
print("Press CTRL-C to stop it.\n")

# Uncomment to run (commented out for safety)
"""
# Version 1: Simple infinite loop
count = 0
while True:
    count += 1
    print(f"This is loop iteration #{count}")
    # In real scenario, you'd want a small delay
    # import time
    # time.sleep(1)  # 1 second delay
"""

# Safe demonstration version with auto-stop
print("Running safe version (stops after 10 iterations):")

count = 0
while True:
    count += 1
    print(f"Loop iteration #{count}")
    
    # For demonstration, we'll add a break condition
    # Remove this for a true infinite loop
    if count >= 10:
        print("Stopping after 10 iterations (remove break for infinite loop)")
        break


# Version 2: Infinite loop with user input
print("Type 'stop' to end this infinite loop...")
while 1:  # 1 is always True
    user_input = input("Say something: ")
    print(f"You said: {user_input}")
    if user_input.lower() == 'stop':
        print("Breaking the infinite loop!")
        break

# Version 3: Infinite for loop (less common)
from itertools import count
for i in count():
    print(f"Infinite for loop iteration {i}")
    # Add break condition or it will run forever
    if i >= 5:  # Remove this for infinite
        break
