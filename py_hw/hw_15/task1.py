class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return 'woof woof'

class Cat(Animal):
    def talk(self):
        return 'meow'

def animal_talk(animal):
    return animal.talk()

dog = Dog()
cat = Cat()
print(animal_talk(dog))
print(animal_talk(cat))