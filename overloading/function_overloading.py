from overloading import overload


@overload
def same_fun():
    print('same fun, no arg')


@overload
def same_fun(a, b):
    return a + b


same_fun(1, 2)
