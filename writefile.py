# f = open("vishmay.txt","a")
#
# a=f.write("vishmay bhai bohot acche hai")
#
# print(a)
#
# f.close()

#handle read and writw both

f = open("vishmay.txt","r+")

print(f.read())

f.write("thank you")

f.close()