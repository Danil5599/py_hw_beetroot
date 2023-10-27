class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @property
    def name(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self, firstname, lastname, age, grade):
        super().__init__(firstname, lastname, age)
        self.grade = grade

class Teacher(Person):
    def __init__(self, firstname, lastname, age, salary):
        super().__init__(firstname, lastname, age)
        self.salary = salary

john = Student("John", "Doe", 20, "A")
jane = Teacher("Jane", "Smith", 35, 50000)

print(f"{john.name}, Age: {john.age}, Grade: {john.grade}")
print(f"{jane.name}, Age: {jane.age}, Salary: ${jane.salary}")
