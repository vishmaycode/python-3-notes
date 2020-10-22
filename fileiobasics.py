# file io basics
"""
"r" - open file for reading                                 default mode
"w"- open file for writing
"x" - creates file if not exist & fails if already exist
"a" - add more content to file from append mode
"t" - its a txt file open as text                           default mode
"b" - binary file
"+" - read and write
"""

f = open("vishmay.txt","rt")         #f is the file pointer 2nd argument is the mode r-read t-text

#print(f.readline())                 #reads only 1 line

#print(f.readlines())                #reads lines in a list

#content = f.read()                  #read is a functions which reads from file pointed by f pointer
                                    #it takes in arguments as 3 which means it will read till 3 characters
                                    #content = f.read(3) prints only once if opened
                                    #after reading whole file it reads none for 2nd time

# s = f.read(4)
# print(s)                #does not print as its already read file
#
# print(content)

# for line in content:
#     print(line)

#for line in f:
#    print(line, end="")


f.close()



