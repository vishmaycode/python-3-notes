#creates a list on which a given funtion returns true when applied

list1 = [1,2,3,4,5,6,7,8,9]

def fuction1(num):
    return num>5                #this type of return statment will return true or false

num = list(filter(fuction1, list1))         #same as map fuction it aplies function1 on list1's all elements
print(num)                                  #and if its true then only its value is stored in list else no
                                            #so after it done executing we get a list whic will return true
                                            #for all its  values as defined by function
                                            # in the sense it applies filter to list (filter is that function)