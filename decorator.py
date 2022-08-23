# def demo(x):
#     print("Inside demo")
#     return x
    
# demo1 = demo
# y = demo1(6)
# print(y)    

# def demo(x):
#     return x*x

# def demo1(demo):
#     y = demo(10)
#     print(y)        
    
# demo1(demo)   


# def hello_Decorator(fun):
#     print("Inside hello")
#     def inner1():
#         print("Inside Inner ")
#         fun()
#     return inner1

# @hello_Decorator
# def main_Function():
#     print("Inside main")
    

# main_Function()


def get_upper(fun):
    def inner(para):
        return fun(para.upper())
        
    return inner        

@get_upper
def is_palindrom(name):
    if(name == name[::-1]):
        return True
    return False
        

print(is_palindrom("pytho"))                        
 
