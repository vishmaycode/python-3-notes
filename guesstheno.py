n=29        #fixed number
z=0        #number of guesses

while(z<10):
    print("Enter ur number(anything between 1 to 100)")
    c=int(input())
    z=z+1
    if z == 0:
        print("Game over!! \nThe number was ", n)
        break
    if c>100 or c<1:
        print("Choice should be between the range\nYou have ",10-z," attempts left")
        continue
    else:
        if c==n:
            print("Congratilations u got the right number in ",z," attempts\nThe entered number was ",n)
            break
        elif c>n:
            print("The entered number is bigger\nYou have ",10-z," attempts left")
            continue
        elif c<n:
            print("The entered number is smaller\nYou have ",10-z," attempts left")
            continue