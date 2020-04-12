from overloading import overload
from collections import Iterable


@overload
def same_fun():
    print('same fun, no arg')


@overload
def same_fun(a, b):
    return a + b


same_fun(1, 2)

"""
def add(in_type,*args):
    if in_type == 'int':
        res = 0
    if in_type == 'str':
        res = ''
    for i in args:
        res = i +res
    return res


add('int',1,2)
"""