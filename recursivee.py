#recursion  - function inside function

#FACTORIAL

# n! = n * n-1 * n-2 * n-3 ........... 1
# n! = n * (n-1)
#
# def factorial_itterative(n):                                       #iterative function
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
# def factorial_recursive(n):                                         #recursive function
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
#
#
num=int(input("Enter the number:-"))                                #input number to find factorial
# print("using itterative method",factorial_itterative(num))
# print("using recursive method",factorial_recursive(num))

#FIBBONACI

#fibbonace series
# 0 1 1 2 3 5 8 13 21 34 55 .....and so on

def fibbo_itterative(n):
    f1=0
    f2=1
    #print(f1)
    #print(f2)
    for i in range(n-2):
        f3=f1+f2
        f1=f2
        f2=f3
        #print(f3)                      # can also return f3 only if asked which is the last element
        return f3


def fibbo_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbo_recursive(n-1) + fibbo_recursive(n-2)


print("fibbonacy itterative")
fibbo_itterative(num)
print("\n")
print(fibbo_recursive(num))