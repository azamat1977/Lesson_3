
x = 3
def mult(*args):
    for i in args:
        global x
        result = i * x
        x = 2
        print(result)
    return result
mult(1,2,3)