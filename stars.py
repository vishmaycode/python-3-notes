"""patern printing

input a int no
inut a boolean variable true or false

true

*
**
***
****


false

****
***
**
**

"""

n=int(input("Enter the number of rows\n"))
z=int(input("Enter True -1 or false -2\n"))
if z==1:
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print("*",end="")
            j=j+1
        print("\n")
        i=i+1
elif z==2:
        q=n
        i=1
        while(q>0):
            j=i
            while(j<=n):
                print("*",end="")
                j=j+1
            print("\n")
            i=i+1
            q=q-1
else:
    print("You entered wrong input")