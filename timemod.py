#using time module

import time

initial = time.time()
#print(initial)

k=0
while(k<45):
#    time.sleep(2)
    print("this is awsome!")
    k+=1

print("\nwhile loop ran in:- ",time.time()-initial," seconds")
initial2=time.time()

for i in range(45):
    print("this is awsome!")

print("\nfor loop ran in:- ",time.time()-initial2," seconds")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)