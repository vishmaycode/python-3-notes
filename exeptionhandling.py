"""n = int(input("Enter number 1\n"))
m = int(input("Enter number 2\n"))

print("The sum of the two numbers is",n+m)"""

n = input("Enter number 1\n")
m = input("Enter number 2\n")

try:                                                            #this try method lets u try the code inside without exiting it if it throws error
    print("The sum of the two numbers is",int(n)+int(m))        #this is the line which is going to give error

except Exception as e:                                          #this is except Exeption as e means catch the error and and store the error in e ans then print e
    print("the error is ",e)                                                    

print("this line is very imp")