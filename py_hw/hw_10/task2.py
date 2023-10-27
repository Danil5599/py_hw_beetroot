import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл JSON не найден!")
        return {}

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def add_entry(data, filename):  # добавляем filename как параметр
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    city = input("Введите город: ")
    data[name] = {"phone": phone, "city": city}
    save_data(filename, data)  # сохраняем изменения сразу после добавления записи

def search(data, key, value):
    results = [name for name, details in data.items() if details[key] == value]
    for result in results:
        print(f"Найдено {result} с телефоном: {data[result]['phone']}, город: {data[result]['city']}")

def main():
    filename = "phonebook.json"
    data = load_data(filename)

    while True:
        choice = input(
            "Выберите:\n"
            "1. Добавить новую запись\n"
            "2. Поиск по имени\n"
            "3. Поиск по номеру телефона\n"
            "4. Выход\n"
        )
        if choice == "1":
            add_entry(data, filename)  # передаем filename как аргумент
        elif choice == "2":
            name = input("Введите имя для поиска: ")
            search(data, "phone", name)
        elif choice == "3":
            phone = input("Введите номер телефона для поиска: ")
            search(data, "city", phone)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()