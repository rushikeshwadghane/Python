class base:
    def __init__(self):
        print("inside base")
      
    def inBase(self,y):
        print(y)
               
class Derived:
    def inBase(self,x):
        print(x ,"inside base")
    
class demo(Derived ,base):
    pass


obj = demo()

obj.inBase(20)    

        