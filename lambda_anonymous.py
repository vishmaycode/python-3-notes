#lambda functions or anonymous functions
#
# def addition1(a,b):
#     return a+b
#
# addition2 = lambda x,y: x+y
#
# print(addition1(2,3))
# print(addition2(2,3))

#sorting using lambda

# def a_first(a):
#     return a[1]

a=[[1,8],[23,6],[4,5]]

#a.sort(key=a_first)

a.sort(key=lambda x:x[1])

print(a)