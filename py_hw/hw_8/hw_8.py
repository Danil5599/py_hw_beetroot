import sys
import mymod

# Задача 2:
print(sys.path)  # Показать текущий sys.path

# Добавим новый путь
sys.path.append('/path/to/directory')

print(sys.path)  # Показать измененный sys.path



# Задача 3:
mymod.test('mymod.py')