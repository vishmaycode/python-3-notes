# it is a function which is used to reduce a list to a single value by processing the elements according to the
#function supplied

list_1 = [1,2,3,4]

# num = 0
# for i in list_1:
#     num = num + i
#
# print(num)

from functools import reduce

result = reduce(lambda x,y: x+y, list_1)

print(result)