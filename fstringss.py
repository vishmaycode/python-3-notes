# f strings

me = "vishmay"
no = 3

# a = "this is %s" %me                          #string formating
# print(a)


# a = "this is %s %s" %(me,no)                    #string formating suing a tuple
# print(a)


# a = "this is {} {}"                       #using format method if we place as "this is {1} {0} then
# b = a.format(me,no)                       #it will change to "this is 3 vishmay" as 1 and 0 are the index places
# print(b)                                  #of the format method's parameter


#f strings

a = f"this is {me} {no}"                            #f string u can use anything inside even modules functions also
print(a)                                            #like {math.sqrt(65)} and {fact(2)}