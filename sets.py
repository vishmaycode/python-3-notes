#dict={'one':1,'two':2,'three':3,'four':4}
#n=input()
#print(dict[n])


s = set()
#print(type(s))

#sxxxx = set([1,2,3,4]) # or store list (var=[1,2,3,4])in a var and put var in set(var) like this
#print(sxxxx)
#print(type(sxxxx))

s.add(1)
s.add(1)

s.add(2)
print(s)
s.remove(2)

s1=s.union({1,2,3})
s2=s.intersection({1,2,3})
print(s,s1,s2)
print(max(s))

print(s.isdisjoint(s1))