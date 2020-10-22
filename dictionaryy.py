#dictionary is nothing but a key value pairs

#dictionary{"key","value"}

d1={"harry":"burger","rohan":"fish","fatso":"roti","satyam":{"b":"maggie","l":"roti","d":"chicken"}}
"""
print(d1)
print(d1["rohan"])          #case sensitive
print(d1["satyam"]["d"])    #dictionary in dictionary


d1["ankit"]="junk food"         #adding elemrnts to dctionarty
del d1["rohan"]                 #deleting in a dictionary
"""

d2 = d1                  #it will assign d1 to d2( that menes d2 and d1 are same) but if u delete anything from
                         # d2 it will aslo get deleted from d1
d3 = d1.copy()           #thats why use sopy function

print(d1.get("harry"))      #print harry's valure

d1.update({"lina":"toffee"})    #insert lina at end

print(d1)

print(d1.keys())            #prints all keys
print(d1.items())           #prints keys and its values as tuples in a list
print(d1.values())          #print values of each key