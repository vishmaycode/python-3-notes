
gro=["harpic","lollipop","deo","vim","bhindi"]
print(gro)
print(gro[1])

num=[2,4,1,5,17]
print(num)
print(num[3])

print(num[0:5])
print(num[::2])

print("\n\n")

num.sort()
print(num)
num.reverse()
print(num)


num2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

print("x",num2[::-4])

num2.append(20)
num2.insert(1,4)
print(num2)



#tuple

#mutable-can change         -list
#immutable-cannot change     -tuple


tp=(1,2,3)
print(tp)

#swapping

a=1
b=8
a,b=b,a
print(a,b)