from unicodedata import name


class Demo:
    x=10
    def __init__(self,name) -> None:
        self.name = name
        
    def fun(self):
        print("Learn Language:",self.name)


obj = Demo('Python')

obj.fun()

        
            