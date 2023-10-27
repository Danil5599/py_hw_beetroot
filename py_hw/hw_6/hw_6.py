# Задача 1
def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = input("Введите предложение: ")
print(count_words(sentence))


# Задача 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_total_price(stock, prices):
    return {item: stock[item] * prices[item] for item in stock}

print(compute_total_price(stock, prices))


# Задача 3
result = [(i, j) for i in range(1, 11) for j in [i**2]]
print(result)


#Задача 4
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_dict = {i+1: day for i, day in enumerate(days_of_week)}

reverse_day_dict = {day: i for i, day in day_dict.items()}

print(day_dict)
print(reverse_day_dict)