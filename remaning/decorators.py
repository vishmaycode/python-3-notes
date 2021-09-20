"""we create a new function and assign it old function so it is displayed"""
# def fuc1():
#     print("subscribe now")
#
# fuc2 = fuc1
#
# del fuc1
#
# fuc2()

"""returning function using a function"""
# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
# a = funcret(0)
# print(a)

"""printing from execution of function"""
# def executer(func):
#     func("this")
#
# executer(print)


"""decorators"""

def dec1(any_func):
    def nowexec():
        print("Executing now")
        any_func()
        print("Executed")
    return nowexec

@dec1
def arg_func():
    print("who is vishmay")

# arg_func = dec1(whoisn)

@dec1
def arg_func2():
    print("this is not vishmay")


arg_func()
arg_func2()