import math

def entwono():
    print("Enter first number")
    a=int(input())
    print("Enter second number")
    b=int(input())


print("1.addition")
print("2.substration")
print("3.multiplication")
print("4.division")
print("5.sqareroot")
print("6.a raised to b")
print("\nENTER UR CHOICE-")
z=int(input())
if(z==1):
    entwono()
    print(a+b)
elif(z==2):
    entwono()
    print(a-b)
elif(z==3):
    entwono()
    print(a*b)
elif(z==4):
    entwono()
    print(a/b)
elif(z==5):
    y=int(input())
    ans=sqrt(y)
    print(ans)
elif(z==6):
    entwono()
    print(math.sqrt(a,b))
else:
    print("\nEnter correct number")
    break