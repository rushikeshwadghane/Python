
# Incapsulation -->>:
#   Incapsulation means binding data (variable) and method (function ) together into single unit (class)
#   and restricting direct access to some data to protect it.

class BankAccount():
    def __init__(self,bal):
        self.__bal  = bal #private variable

    def deposite(self,amount):
        self.__bal += amount

    def get_bal(self):
        return self.__bal

b_ojb =  BankAccount(1000)
b_ojb.deposite(1000)
k = b_ojb.get_bal()
print(k)


# Abstraction  -->

# abstraction means hiding internal implementation detail and showing only essentials features to the user.

from abc import ABC , abstractmethod

class  Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Size(Shape):
    def __init__(self,l,h):
        self.l = l
        self.h = h

    def area(self):
        return self.l * self.h
    
a_obj = Size(5,4)
print('----------------')
print(a_obj.area())


# Inheritance -->
    # Inheritance allow a class to aquire properties and method of another class,
    # enabling code reuse


class Parent:
    def __init__(self,use):
        self.use = use
    def  Car(self):
        print(f"Car is driving by",self.use)

    
class Child(Parent):
    def __init__(self, use):
        self.use = use

    def bike(self):
        print("bike use by ")



p = Parent('Parent')
c = Child('child')
c.Car()

    
# Polimorphism -->
    # polimorphism means same function same name but different behaviour depending on the project

    

