"""
var1 = 6
var2 = 56

var3 = int(input())

if var3>var2:           #if else
    print("greater")
if var3==var2:
    print("equal")
else:
    print("lesser")

if var3>var2:              #if else ladder
    print("greater")
elif var3==var2:
    print("equal")
else:
    print("lesser")


list = [5,6,7,8]

if 5 in list:
    print("yes 5 is in the list")

if 5 not in list:
    print("no 5 is not in the list")

print(3 in list)
print(3 not in list)
"""
age = int(input())
if age<100:
    if age>18:
        print("yes u can drive")
    elif age==18:
        print("we cannot be sure if u can drive")
    else:
        print("you cannot drive")
else:
    print("inavlid age")