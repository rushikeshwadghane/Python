
def my_decorator(fun):
    def wrapper_fun():
        print('Inside Decorator')
        fun()
        print("After function call")
    return wrapper_fun
    

    
@my_decorator
def say_hello():
    print('Hello WOrld')
    print('Hello WOrld')


say_hello()