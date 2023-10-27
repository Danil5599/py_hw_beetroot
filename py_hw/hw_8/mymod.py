def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_chars(name):
    with open(name, 'r') as file:
        content = file.read()
        return len(content)

def test(name):
    print(f"Количество строк в {name}: {count_lines(name)}")
    print(f"Количество символов в {name}: {count_chars(name)}")