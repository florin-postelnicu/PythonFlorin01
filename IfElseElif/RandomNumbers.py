
# To use a random generator  you need to import random module
import random;
# This program will generate a random integer between 1 and 10 , inclusive
yesno = True
while(yesno):
    number = random.randint(1, 10)
    print("The random number is : ", number)
    print("Do you want to get more random numbers y/n")
    more = str(input("Enter  y or n"))
    if(more =='y'):
        continue
    else:
        print("Thanks !")
        yesno = False
exit()
