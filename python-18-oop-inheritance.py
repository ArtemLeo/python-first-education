# Inheritance, super()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Person created!')

    def say_hello(self):
        print(f"{self.name} says hello!")


person1 = Person('John', '25')
person1.say_hello()


class Student(Person):
    pass
