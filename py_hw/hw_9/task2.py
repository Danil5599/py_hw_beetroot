def compute_value():
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        return (a**2) / b
    except ValueError:
        return "Ошибка! Введите действительное число."
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль."

print(compute_value())