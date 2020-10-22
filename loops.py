"""
list1 = ['harry','marry','carry','larry']

for i in list1:
    print(i)


list = [['harry',1],['marry',2],['carry',3],['larry',4]]

for i in list:
    print(i)

for i,j in list:
    print(i,j)

for i,j in list:
    print(i,"and lollypop is",j)



dict1= dict(list)       #typecast list to dictionary

print(dict1)

#for i,j in dict                            this is the wrong way
#    print(i, "and loly is ",j)


for i,j in dict1.items():     #items means both key and value {"key":"value"}
    print(i,"and lolly in",j)

#for only key

for i in dict1:
    print(i)
"""

# printing only numbers from a list of many datatypes and it should be greater then 6

list2=[1,2,6,7,8,9,21,42,32,77,"hello","bye"]

for num in list2:
    if str(num).isnumeric() and num>=6:
            print(num)
