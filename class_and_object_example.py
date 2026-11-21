"""Practice example defining or demonstrating `Person`, `Employee`."""



class Person:

    species = 'Homo sapiens'    # class variable (shared by all instances)

    def __init__(self,name,age): # constructor
        self.name = name      # instance variable
        self.age = age

    def greet(self):
        return f"hi, I am {self.name} , {self.age} years old "



    @classmethod
    def from_string(cls,string):   # class method (alternate constructor)
        name , age = string.split(',')
        return cls(name,int(age))


    @staticmethod
    def is_adult(age):  # static method (utility)
        return age >= 18


p = Person('Rushikesh',27)
q = Person.from_string("Rushikesh,28")  #class method no need to create object

print(p.greet())
print(q.greet())
print(Person.is_adult(q.age))  # True



class Employee:
    company = "Google"   # Class Variable
    def __init__(self, name, salary):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__bonus = 5000      # Private

    def show(self):              # Instance Method
        print(self.name)

    def _calculate(self):        # Protected Method
        return self._salary * 0.1

    def __private_method(self):  # Private Method
        print("Private")

    @classmethod
    def change_company(cls, name):   # Class Method
        cls.company = name

    @staticmethod
    def is_valid(salary):   # Static Method
        return salary > 0
