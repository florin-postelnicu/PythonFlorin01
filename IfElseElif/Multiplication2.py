
import random
print(" This program helps you to learn the multiplication table!")
a = random.randint(1, 10)
b = random.randint(1, 10)

print("Find the product of the numbers  :", a , " * ", b)
product = a*b
print("Please Enter your answer")
guess = int(input("Answer   "))

count = 0
while( count <=2):
    if(product == guess):
        print ("Your answer is correct, Congrats!")
        break;

    else:

        print("Sorry, you should try again, the real answer is not that \nYou have some more trails " )
        print("You have 3 trails. So far you tryied :", count +1, "   time(s)")
        print("Please Enter your answer")
        guess = int(input("Answer   "))
        count = count +1

exit()