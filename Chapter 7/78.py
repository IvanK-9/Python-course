sandwich_orders = ['tuna', 'cheese', 'ham', 'vegetarian']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
