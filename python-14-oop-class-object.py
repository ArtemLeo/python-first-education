# OOP: Classes and objects
# class creating
class Person:
    pass


# object creating
person1 = Person()
person1.name = "John"
person1.surname = "Smith"
person1.place_of_birth = "Spain"
print(f"Name: {person1.name} -> Surname: {person1.surname} -> Place of birth: {person1.place_of_birth}")

person2 = Person()
person2.name = 'Sam'
person2.surname = 'Jonson'
person2.place_of_birth = 'Ireland'
print(f"Name: {person2.name} -> Surname: {person2.surname} -> Place of birth: {person2.place_of_birth}")
