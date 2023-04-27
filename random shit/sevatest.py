class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        self.__age = value
    
    @age.deleter
    def age(self):
        del self.__age

person = Person("John", 30)
print(person.age) # 30
person.age = 40
print(person.age) # 40
del person.age
