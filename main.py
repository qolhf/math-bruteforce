import sys

def divison():
    def divide(x,y):
        return x / y

    first = int(input("First Number: "))
    second = str(input("Divided by var: "))
    equals = int(input("equals: "))


    for x in range(1,1000):
        expression = divide(first, x)
        print("Trying {}/{}={}".format(first, x, expression))
        if expression == equals:
            print("{}={}".format(second, x))
            sys.exit()

def multiplication():
    def multiply(x,y):
        return x * y

    first = int(input("First Number: "))
    second = str(input("times by var: "))
    equals = int(input("equals: "))


    for x in range(1,1000):
        expression = multiply(first, x)
        print("Trying {}x{}={}".format(first, x, expression))
        if expression == equals:
            print("{}={}".format(second, x))
            sys.exit()

def addition():
    def add(x,y):
        return x + y

    first = int(input("First Number: "))
    second = str(input("plus var: "))
    equals = int(input("equals: "))


    for x in range(1,1000):
        expression = add(first, x)
        print("Trying {}+{}={}".format(first, x, expression))
        if expression == equals:
            print("{}={}".format(second, x))
            sys.exit()

def subtraction():
    def subtract(x,y):
        return x + y

    first = int(input("First Number: "))
    second = str(input("subtracted by var: "))
    equals = int(input("equals: "))


    for x in range(1,1000):
        expression = subtract(first, x)
        print("Trying {}-{}={}".format(first, x, expression))
        if expression == equals:
            print("{}={}".format(second, x))
            sys.exit()

a = input("Multiply, Divison, Addition or Subtraction?: ")

if "multi" in a:
    multiplication()
elif "divi" in a:
    divison()
elif "addi" in a:
    addition()
elif "subtra" in a:
    subtraction()
else:
    sys.exit()
