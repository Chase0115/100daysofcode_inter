def add(*args):
    print(args[0:2])
    sum = 0
    for argument in args:
        sum += argument

    return sum

print(add(1,2,3,4,5,4,5,4,3,8))

def calculate(n, **kwargs):
    for key, value in kwargs.items():
    #     print(key)
    #     print(value)
        n += kwargs["add"]
        n *= kwargs["multiply"]
    # print(kwargs["add"])
    # print(kwargs["multiply"])
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"] # if use [], "make" is essential argument
        self.model = kw.get("model") #if use "get", "model" is not essential argument


mycar = Car(make= "Subaru", model= "Impreza")
print(mycar.make)

