
def getdate():
    import datetime
    return str(datetime.datetime.now())


f = open("hello.txt","a")

name=input("input here:-")
f.write(name)

f.write(" - ")

date=getdate()
print(date)
f.write(date)

f.write("\n")
f.close()
