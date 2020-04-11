from multipledispatch import dispatch
import math

@dispatch(int)
def area(r):
    return math.pi * r ** 2

@dispatch(int, int)
def area(l, b):
    return l * b


print(area(3))
print(area(3,4))
