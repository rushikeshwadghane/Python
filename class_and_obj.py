

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
