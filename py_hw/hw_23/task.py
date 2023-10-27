# Бинарный поиск с использованием рекурсии
def binary_search_recursive(arr, x, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search_recursive(arr, x, mid + 1, high)
        else:
            return binary_search_recursive(arr, x, low, mid - 1)
    else:
        return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 9
print(f"Элемент {x} найден на позиции:", binary_search_recursive(arr, x))


# Fibonacci search
def fibonacci_search(arr, x):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(arr):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while fibM > 1:
        i = min(index + fibM_minus_2, len(arr)-1)
        if arr[i] < x:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif arr[i] > x:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if fibM_minus_1 and index < len(arr)-1 and arr[index+1] == x:
        return index+1
    return -1

x = 17
print(f"Элемент {x} найден на позиции:", fibonacci_search(arr, x))

# HashTable с in (__contains__) и len (__len__) методами
class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return
        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[key_hash].append(key_value)

    def __getitem__(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def __contains__(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return True
        return False

    def __len__(self):
        count = 0
        for i in self.table:
            if i is not None:
                count += len(i)
        return count


hash_table = HashTable()
hash_table["name"] = "John"
hash_table["age"] = 30
hash_table["country"] = "USA"
print("'name' содержится в хеш-таблице:", "name" in hash_table)
print("'gender' содержится в хеш-таблице:", "gender" in hash_table)
print("Размер хеш-таблицы:", len(hash_table))
