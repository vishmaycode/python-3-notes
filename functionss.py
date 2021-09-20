"""
b=3
c=9
a =sum((b,c))
"""


#user defined functions

def func1():
    print("ur in function 1")

func1()
print("\nx",func1())


def func2(a, b):
    print("ur in function 2",a+b)

func2(5,7)


def func3(a, b):
    avg=(a+b)/2
    print(avg)

func3(4,8)


def func4(a, b):
    avg=(a+b)/2
    return avg

x= func4(4,8)

print(x)

#docstring

def hellon():
    """this is the docdtring of this functions"""

#to print the doctring of any function

print(hellon.__doc__)

print(sum.__doc__)