sandwich_orders = ['tuna', 'pastrami', 'cheese', 'pastrami', 'ham', 'pastrami']
finished_sandwiches = []

print("Sorry, we've run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches made (no pastrami):")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
