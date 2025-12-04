# Мой список пицц
my_pizzas = ['pepperoni', 'margherita', 'hawaiian']

# Копия списка для друга
friend_pizzas = my_pizzas[:]

# Добавляю новую пиццу в мой список
my_pizzas.append('four cheese')

# Добавляю другую пиццу в список друга
friend_pizzas.append('vegetarian')

# Доказательство что списки разные
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)