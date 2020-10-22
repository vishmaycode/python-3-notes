# applies a function to all the items of list

num=["3","34","64"]

#
# for i in range(len(num)):
#     num[i] = int(num[i])

# print(map(int, num))                    #prints map object
#
# num = list(map(int, num))               #map returns a object thats why we use list to type cast it to list
#
# num[2] = num[2] + 1
#print(num[2])


#new part

number = [2,3,4,5,6,7,8,1]

# def sq(a):
#     return a*a
#
# square = list(map(sq, number))
# print(square)

#using lambda functions
# square = list(map(lambda x: x*x, number))
# print(square)

def squ(a):
    return a*a

def cube(a):
    return a*a*a

func = [squ,cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

