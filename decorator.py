# def demo(x):
#     print("Inside demo")
#     return x
    
# demo1 = demo
# y = demo1(6)
# print(y)    



def demo(x):
    return x*x

def demo1(demo):
    y = demo(10)
    print(y)        
    
demo1(demo)   