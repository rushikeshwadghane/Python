
def decorator(func):

    def wrapper_fun(a,b):
        print(a,b)
        print('in dec')

        val = func(a,b)
        return val
    return wrapper_fun
    
@decorator
def sum_of_val(a,b):
    print(a,b)
    return a + b


print('Sum ------>>', sum_of_val(5,7))