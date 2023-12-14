# OOP: Functions, 'self'
class Person:

    def show_info(self, quantity_of_shows):
        for i in range(quantity_of_shows):
            print(f"Name: {self.name} -> Surname: {self.surname} -> Place of birth: {self.place_of_birth}")

    def get_age(self, current_year):
        return current_year - self.year_of_birth


person1 = Person()
person1.name = "John"
person1.surname = "Smith"
person1.place_of_birth = "Spain"
person1.year_of_birth = 2000
person1.show_info(2)  # or by class name -> Person.show_info(person1)
print(f"Age of person1 = {person1.get_age(2023)}")
print('------------------------------')

person2 = Person()
person2.name = 'Sam'
person2.surname = 'Jonson'
person2.place_of_birth = 'Ireland'
person2.year_of_birth = 1998
person2.show_info(3)  # or by class name -> Person.show_info(person2)
print(f"Age of person2 = {person2.get_age(2023)}")
print('------------------------------')
