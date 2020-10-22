i = 0

#while(i<10):
#    print(i)
#    i = i + 1

#break and  continue
"""
while(1):           #or while(true) loop goes on and on
    i = i+1
    if(i<10):
        continue        #continue statement makes the loop stop there and go to the next iteration  without executing the code beloq
    print(i)
    if(i==30):
        break   #breaks the loop
"""

"""
x=0
while(x<100):
    x=int(input())
print("congratulations on typing a number bigger then hundred")
"""



z=0

while(True):
    print("enter ur no")
    z=int(input())
    if z<100:
        print("try again\n")
        continue
    else:
        print("congo u made it")
        break

