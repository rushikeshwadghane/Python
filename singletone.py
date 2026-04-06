"""
Singleton class is a design pattern used in programming to ensure that only one instance of
a class is created during the entire program of execution and provide a single access point to that instance

"""

"""
A singleton class is a class that restricts the instantiation of the class to only one object and follo 
that single object to be accessed globally throughout the application 

"""

class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
    

a = Singleton()
b = Singleton()

print(a is b)
