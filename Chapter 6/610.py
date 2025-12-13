# multiple numbers per person
favorite_numbers = {
    'Alice': [7, 42, 13],
    'Bob': [3, 21],
    'Charlie': [99, 100, 777, 5],
    'Diana': [8],
    'Ethan': [23, 69, 88]
}

print("\n=== Exercise 6-10: Favorite Numbers ===")
for person, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{person}'s favorite number is: {numbers[0]}")
    else:
        numbers_str = ', '.join(str(num) for num in numbers)
        print(f"{person}'s favorite numbers are: {numbers_str}")