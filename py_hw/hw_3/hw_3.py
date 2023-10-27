# Задача 1
def manipulate_string(s):
    if len(s) < 2:
        return "Empty String"
    return s[:2] + s[-2:]

print(manipulate_string('helloworld'))
print(manipulate_string('my'))
print(manipulate_string('x'))

# Задача 2
def check_phone_number(phone):
    if len(phone) == 10 and phone.isdigit():
        return "Это действительный номер телефона!"
    return "Недействительный номер телефона!"

phone_number = input("Введите номер телефона: ")
print(check_phone_number(phone_number))

# Задача 3
def math_quiz():
    answer = int(input("Сколько будет 5 + 3? "))
    if answer == 8:
        return "Правильно!"
    return "Неправильно!"

print(math_quiz())

# Задача 4
stored_name = "anton"

def check_name():
    user_name = input("Введите ваше имя: ")
    if user_name.lower() == stored_name:
        return True
    return False

print(check_name())