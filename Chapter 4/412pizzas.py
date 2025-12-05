# My favorite foods
my_foods = ['pizza', 'falafel', 'carrot cake']

# Friend's foods (copy)
friend_foods = my_foods[:]

# I add my foods
my_foods.append('cannoli')
my_foods.append('ice cream')

# Friend adds their foods
friend_foods.append('sushi')
friend_foods.append('pasta')

# Print using for loops
print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)