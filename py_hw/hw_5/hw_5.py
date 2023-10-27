# Задача 1: Поиск наибольшего числа в списке.
import random

numbers = []
i = 0

while i < 10:
    num = random.randint(1, 100)
    numbers.append(num)
    i += 1

max_num = numbers[0]
i = 0

while i < 10:
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1

print(f"Список чисел: {numbers}")
print(f"Наибольшее число: {max_num}")


# Задача 2: Эксклюзивные общие числа.
list1 = []
list2 = []
i = 0

while i < 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    i += 1

common_numbers = []
i = 0

while i < 10:
    if list1[i] in list2 and list1[i] not in common_numbers:
        common_numbers.append(list1[i])
    i += 1

print(f"Первый список: {list1}")
print(f"Второй список: {list2}")
print(f"Общие числа: {common_numbers}")


#Задача 3: Извлечение чисел.
numbers = []
i = 1

while i <= 100:
    numbers.append(i)
    i += 1

result = []
i = 0

while i < 100:
    if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
        result.append(numbers[i])
    i += 1

print(f"Числа, которые делятся на 7, но не являются кратными 5: {result}")