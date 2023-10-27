# Задача 1: Создание простой функции favorite_movie
def favorite_movie(movie_name):
    print(f"My favorite movie is named {movie_name}")

favorite_movie("Star Wars")


# Задача 2: Создание словаря с помощью функции make_country.
def make_country(name, capital):
    country = {
        'name': name,
        'capital': capital
    }
    print(country)

make_country("Ukraine", "Kyiv")


# Задача 3: Создание простого калькулятора с функцией make_operation.
def make_operation(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        return args[0] - sum(args[1:])
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result

print(make_operation('+', 7, 7, 2))  # Должно вернуть 16
print(make_operation('-', 5, 5, -10, -20))  # Должно вернуть 30
print(make_operation('*', 7, 6))  # Должно вернуть 42