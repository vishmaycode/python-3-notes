f= open("vishmay.txt")
print(f.readline())
print(f.tell())

f.seek(97)

print(f.readline())
#print(f.tell())
#print(f.readline())
#print(f.tell())


f.close()