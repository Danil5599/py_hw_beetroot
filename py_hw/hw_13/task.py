# Задача 1: Класс Person

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old."

person = Person("Carl", "John", 26)
print(person.talk())

print()                 # новая строка для разделения


# Задача 2: Doggy age

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


dog = Dog(3)
print(dog.human_age())

print()                 # новая строка для разделения


# Задача 3: TV controller

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_number = 0

    def first_channel(self):
        self.current_channel_number = 0
        return self.channels[self.current_channel_number]

    def last_channel(self):
        self.current_channel_number = -1
        return self.channels[self.current_channel_number]

    def turn_channel(self, n):
        self.current_channel_number = n - 1
        return self.channels[self.current_channel_number]

    def next_channel(self):
        self.current_channel_number = (self.current_channel_number + 1) % len(self.channels)
        return self.channels[self.current_channel_number]

    def previous_channel(self):
        self.current_channel_number = (self.current_channel_number - 1) % len(self.channels)
        return self.channels[self.current_channel_number]

    def current_channel(self):
        return self.channels[self.current_channel_number]

    def exists(self, value):
        if isinstance(value, int):
            return "Yes" if 0 < value <= len(self.channels) else "No"
        elif isinstance(value, str):
            return "Yes" if value in self.channels else "No"

controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))