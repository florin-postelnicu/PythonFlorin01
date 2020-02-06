

print(" For this program you will need to decide how long the while loop will work")

# Create a boolean variable
yesno = True

while(yesno):
    print("Enter a number greater than 10")
    number = int(input("The number is :"))
    if(number < 10):
        print("You entered a number less than 10  ", number)
        print("The program will be terminated")
        yesno = False

    else:
        print(" Perfect! You entered anumber greater than 10 ", number , "  keep playing!")

print("Thank you for playing the game!")
exit()