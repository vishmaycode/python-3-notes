# l=10                            #global can be used throughout the program only changes in any function if defined
#
# def func1(n):
#     l=5                         #local specific to this function
#     print(l)
#     print(n,"i have printed")
#
# func1("this is me")
#print(l)


def harry():
    x=20                                        #local variable not global
    def rohan():
        global x                                #gives permisson to edit global variable
        x=88                                    #changes global variable to 88 which does not exist so it creates a global variable
    print("before calling rohan()",x)           #x is 20
    rohan()
    print("after calling rohan()",x)            #x is still 20 as it changes global variable and not local variable


harry()
print("global x is ",x)                #prints global variable and this time there was no global varaible but it created one and initalsied and
                        #printed that without affecting the local harry variable