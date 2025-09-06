# Method Overriding

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()   # Child’s method overrides Parent


# Method Overloading

class MathOps:
    def add(self, a, b=0, c=0):   # default values
        return a + b + c

m = MathOps()
print(m.add(5, 10))        # 15
print(m.add(5, 10, 15))    # 30
