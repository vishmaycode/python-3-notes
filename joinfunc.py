lis = ["jhon","cena","randy","orton","khali","jindar mahal","sheamus"]

# for item in lis:                                  #basic way anyone will think of doing
#     print(item,"and ",end="")
#
# print("other wwe superstars")


a = " and ".join(lis)                           #using join function
print(a,"and other wwe superstars")