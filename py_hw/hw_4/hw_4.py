import random

# Задача 1: Игра Угадай число.
def guessing_game():
    # Генерируем случайное число между 1 и 10
    number = random.randint(1, 10)
    # Запрашиваем у пользователя число
    guess = int(input("Угадайте число от 1 до 10: "))

    # Сравниваем число пользователя с сгенерированным числом
    if guess == number:
        print("Поздравляем! Вы угадали!")
    else:
        print(f"Вы не угадали. Загаданное число было: {number}")

guessing_game()

# Задача 2: Программа приветствия по дню рождения.
def birthday_greeting():
    # Получаем имя и возраст от пользователя
    name = input("Введите ваше имя: ")
    age = int(input("Введите ваш возраст: "))

    # Выводим сообщение
    print(f"Привет, {name}, на ваш следующий день рождения вам будет {age + 1} лет!")

birthday_greeting()

# Задача 3: Комбинация слов.
def word_combinations():
    # Получаем строку от пользователя
    word = input("Введите слово: ")

    # Генерируем и выводим 5 случайных комбинаций
    for _ in range(5):
        shuffled_word = ''.join(random.sample(word, len(word)))
        print(shuffled_word)

word_combinations()