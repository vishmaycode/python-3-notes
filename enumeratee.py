# enunumerate fumctions

listof=["bhindi","aloo","chopstick","chowmein"]
#
# i = 1
#
# for item in listof:
#     if i%2 is not 0:
#         print(f"jarvis please buy {item}")
#     i += 1

#enumerate returns index and item as tuple in list
#
# loop = ["up","down","left","right"]
#
#enumerate(loop) on this will return
#
#[(1,"up"),(2,"down"),(3,"left"),(4,"right")]

for i,j in enumerate(listof):
    if i%2==0:
        print(i,j)

#used to track position of item in for loop

new_dict = dict(enumerate(listof))
print(new_dict)

#creates a dict from a list with index as keys