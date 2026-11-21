"""Practice example defining or demonstrating `my_gen`."""



def my_gen():
    for i in range(1,11):
        yield i

obj = my_gen()
print(list(obj))
