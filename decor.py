

# def decorator(fun):
#     def wrapper():
#         print('before function')
#         fun()
#         print('after fun')
#     return wrapper

# @decorator
# def say_hello():
#     print('hello world')


# say_hello()
    





def wrapper(fun):
    def inside_wrapp():
        print('inside wrapper')
        fun()
        print('after fun excution')
    return inside_wrapp
    
@wrapper
def demo():
    print('inside demo')


demo()