"""Practice example defining or demonstrating `decorator`, `demo`, `wrapper`, and related helpers."""


def decorator(fun):
    def wrapp():
        fun()

    return wrapp


@decorator
def demo():
    print('check decoraor')



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
