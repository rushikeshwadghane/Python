from abc import ABC,abstractmethod


class Vehicle(ABC): #abstract class
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print('car starts with key')
    
class Bike(Vehicle):
    def start(self):
        print('bike start with kick')


# Using the classes
vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()