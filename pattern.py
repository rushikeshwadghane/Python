"""Practice example defining or demonstrating `pattern`."""

def pattern(n):
    for i in n:
        print("|",end='')
        print("* " * int(i))
