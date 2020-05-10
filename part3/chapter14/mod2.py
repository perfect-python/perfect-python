from mod1 import func1

def func2():
    value = func1()
    if value % 2 == 0:
        return "even"
    else:
        return "odd"
