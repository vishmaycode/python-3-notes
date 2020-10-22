def printhar(string):
    return f"ye string harry ko dede thakut {string}"

def add(num1,num2):
    return num1+num2+5

print("and the name is ",__name__)      #prints name of the the file from where it will be imported
                                        #normally not used just for learning

if __name__ == '__main__':          #it will run if used in this program and not anywhere else
    print(printhar("harry1"))
    o = add(4,5)
    print(o)