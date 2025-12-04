# Мои любимые блюда
my_foods = ['pizza', 'falafel', 'carrot cake']

# Блюда друга (копия)
friend_foods = my_foods[:]

# Добавляю свои блюда
my_foods.append('cannoli')
my_foods.append('ice cream')

# Друг добавляет свои
friend_foods.append('sushi')
friend_foods.append('pasta')

# Печатаем с помощью циклов for
print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)