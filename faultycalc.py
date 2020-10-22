#print wrong calc only for some sums and all rest will be as normal

#45*3=555, 56+9=77, 56/6=4
while(True):
    print("enter first number")
    var1=int(input())
    print("enter second number")
    var2=int(input())
    print("enter the operator")
    op=input()

    if var1==45:            # if var1==45 and var2==3 and op=='*':
        if var2==3:
            if op=='*':
                print("ans is 555")
    elif var1==56:
        if var2==9:         #var2==9 and op=='+'
            if op=='+':
                print("ans is 77")
        elif var2==6:       #var2==6 and op=='+'
            if op=='/':
                print("ans is 4")
    else:
        if op=='+':
            print('ans is ',var1+var2)
        elif op=='-':
            print('ans is ',var1-var2)
        elif op=='/':
            print('ans is ',var1/var2)
        elif op=='*':
            print('ans is ',var1*var2)
        else:
            print("invalid operator")