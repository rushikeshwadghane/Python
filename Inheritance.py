class Person:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"My name is {self.name}")

class Student(Person):   # Student inherits Person
    def study(self):
        print(f"{self.name} is studying")

# Using classes
s = Student("Rushikesh")
s.speak()   # inherited from Person
s.study()   # own method
