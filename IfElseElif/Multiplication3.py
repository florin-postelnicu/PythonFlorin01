

import random
yesno = True
correct = 0
incorrect = 0
score = 0
games = 0
while(yesno):
    games += 1

    print(" This program helps you to learn the multiplication table!")
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("Find the product of the numbers  :", a , " * ", b)
    product = a*b
    print("Please Enter your answer ")
    guess = int(input("Answer   "))
    count = 0
    while ( count <=2):
        count = count + 1
        if(product == guess):
            print ("Your answer is correct, Congrats!")
            correct +=3
            break;
        else:
            incorrect += 1
            print("Sorry, you should try again, the real answer is not that \nYou have some more trails " )
            print("You have 3 trails. So far you tryied :", count  , "   time(s)")
            print("Find the product of the numbers  :", a, " * ", b)
            print("Please Enter your answer")
            guess = int(input("Answer   "))

    score = correct - incorrect
    print("Score is   ", score)
    print("Do you want to play again? y/n   ")
    yn = str(input("Enter y or n  "))
    if(yn != 'y'):
        yesno = False

print("Thank you for playing thegame. Your score is ", score)
print("You have played  ", games, "  games!")
print("Your accuracy si : ", round(score/(3*games)*100 , 3), "%  ")
exit()
