"""
===========================================================
            COMPLETE PYTHON OOP GUIDE
          (Theory + Code + Design Patterns)
===========================================================


CONTENTS:
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
5. Method Overriding
6. Operator Overloading
7. Class vs Instance Variables
8. Static Methods
9. Class Methods
10. Magic / Dunder Methods
11. Property Decorators
12. Composition vs Inheritance
13. Multiple Inheritance & MRO
14. Duck Typing
15. Object Lifecycle
16. Design Patterns:
    - Singleton
    - Factory
    - Strategy
    - Observer
===========================================================
"""

print("\n================ 1. ENCAPSULATION =================\n")

# Theory:
# Encapsulation is the mechanism of **binding data and methods** together
# and **restricting direct access** to some of the object's components.
# It helps to protect the internal state of an object.

class BankAccount:
    """Encapsulated Bank Account Example"""

    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print("Encapsulation - Balance:", acc.get_balance())


print("\n================ 2. ABSTRACTION =================\n")

# Theory:
# Abstraction means **hiding internal implementation details**
# and showing only the necessary features to the user.
# In Python, abstract classes from `abc` module are used for this.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        """Every shape must implement area method"""
        pass

class Rectangle(Shape):

    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

rect = Rectangle(5, 4)
print("Abstraction - Rectangle Area:", rect.area())


print("\n================ 3. INHERITANCE =================\n")

# Theory:
# Inheritance allows a class to **acquire properties and methods**
# from another class. Helps in code reuse.

class Parent:
    def __init__(self, name):
        self.name = name

    def car(self):
        print(f"{self.name} is driving a car")

class Child(Parent):
    def bike(self):
        print(f"{self.name} is riding a bike")

c = Child("Rahul")
c.car()
c.bike()


print("\n================ 4. POLYMORPHISM =================\n")

# Theory:
# Polymorphism means **same interface, different implementations**.
# Example: multiple classes having the same method name.

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

for animal in [Dog(), Cat()]:
    animal.speak()


print("\n================ 5. METHOD OVERRIDING =================\n")

# Theory:
# Child class can **override methods** of parent class for different behavior.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Cow(Animal):
    def sound(self):
        print("Cow says Moo")

c = Cow()
c.sound()


print("\n================ 6. OPERATOR OVERLOADING =================\n")

# Theory:
# Operator overloading allows **custom behavior of operators** for objects.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print("Operator Overloading - Sum:", n1 + n2)


print("\n================ 7. CLASS VS INSTANCE VARIABLES =================\n")

# Theory:
# Class variables are shared across all instances,
# while instance variables are unique to each object.

class Employee:
    company = "Google"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

e1 = Employee("Aman")
e2 = Employee("Rahul")
print(e1.company, e1.name)
print(e2.company, e2.name)


print("\n================ 8. STATIC METHODS =================\n")

# Theory:
# Static methods are **bound to the class**, not the object.
# They do not access instance variables.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print("Static Method:", MathUtils.add(5, 6))


print("\n================ 9. CLASS METHODS =================\n")

# Theory:
# Class methods access **class variables** and can modify class state.

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")
print("Class Method - School:", Student.school)


print("\n================ 10. MAGIC / DUNDER METHODS =================\n")

# Theory:
# Special methods like __str__, __repr__, __add__, etc.
# allow us to define **object behavior with operators & built-ins**.

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"

b = Book("Python Mastery")
print(b)


print("\n================ 11. PROPERTY DECORATORS =================\n")

# Theory:
# Property decorators allow **controlled access** to private variables.

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

p = Person("Ravi")
print(p.name)
p.name = "Karan"
print(p.name)


print("\n================ 12. COMPOSITION VS INHERITANCE =================\n")

# Theory:
# Composition = object **has a** reference to another object.
# Inheritance = object **is a** type of parent class.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        self.engine.start()

car = Car()
car.start()


print("\n================ 13. MULTIPLE INHERITANCE & MRO =================\n")

class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show()
print("MRO:", C.mro())


print("\n================ 14. DUCK TYPING =================\n")

# Theory:
# If it walks like a duck and quacks like a duck, it's a duck.
# Python uses **dynamic typing**, so objects are accepted if they have the required methods.

class Bird:
    def fly(self):
        print("Bird flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

def start_flying(obj):
    obj.fly()

start_flying(Bird())
start_flying(Airplane())


print("\n================ 15. OBJECT LIFECYCLE =================\n")

# Theory:
# Object lifecycle involves __new__, __init__, and __del__.

class Test:
    def __new__(cls):
        print("Object Creating")
        return super().__new__(cls)

    def __init__(self):
        print("Object Initialized")

    def __del__(self):
        print("Object Destroyed")

t = Test()


print("\n================ 16. DESIGN PATTERNS =================\n")

print("\n-- Singleton Pattern --")

class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print("Singleton - Same Instance:", s1 is s2)


print("\n-- Factory Pattern --")

class Car:
    def drive(self):
        print("Driving Car")

class Bike:
    def drive(self):
        print("Riding Bike")

class VehicleFactory:
    @staticmethod
    def get_vehicle(vtype):
        if vtype == "car":
            return Car()
        elif vtype == "bike":
            return Bike()
        else:
            return None

v = VehicleFactory.get_vehicle("car")
v.drive()


print("\n-- Strategy Pattern --")

class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class PaypalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using PayPal")

class ShoppingCart:
    def __init__(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        self.strategy.pay(amount)

cart = ShoppingCart(CreditCardPayment())
cart.checkout(500)


print("\n-- Observer Pattern --")

class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

class Observer:
    def update(self, message):
        print("Received:", message)

sub = Subject()
obs1 = Observer()
obs2 = Observer()
sub.subscribe(obs1)
sub.subscribe(obs2)
sub.notify("New Notification")

print("\n================ END OF COMPLETE OOP GUIDE =================\n")