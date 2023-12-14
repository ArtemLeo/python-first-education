# OOP: Class attributes, static
class Person:
    static_count = 100
    create_count = 0

    def __init__(self, name, surname, place_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        print('Person created!')
        Person.create_count += 1


person1 = Person('John', 'Smith', 'Spain')

# call static attributes
# by object (changes through the object are not possible -> creates an object variable)
print('Call static attributes: ' + str(person1.static_count))
person1.static_count = 200
print('Call static attributes: ' + str(person1.static_count))
print('------------------------------')

# by class (changes through the class are possible)
print(f"Call static attributes: {Person.static_count}")
Person.static_count = 200
print(f"Call static attributes: {Person.static_count}")
print('------------------------------')

person2 = Person('Tom', 'Smith', 'Italy')
person3 = Person('Ben', 'Smith', 'UK')
print('------------------------------')
print(f"Create_count = {Person.create_count}")
