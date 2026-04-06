
def my_denerator(n):
    for i in range(n):
        yield i

g = my_denerator(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))




def read_large_file(file_path):
    with open(file_path,'r') as f:
        for line in f:
            yield line