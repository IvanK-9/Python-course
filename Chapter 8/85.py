def describe_city(city, country='Iceland'):
    print(f"{city} is in {country}.")

# 1. Город в стране по умолчанию
describe_city('Reykajavik')

# 2. Ещё один город в Исландии
describe_city('Akujeri')

# 3. Город в другой стране
describe_city('Tokio', 'Japan')
describe_city(city='Paris', country='France')
