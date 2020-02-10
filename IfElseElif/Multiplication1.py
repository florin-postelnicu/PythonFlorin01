
import random
print(" This program helps you to learn the multiplication table!")
a = random.randint(1, 10)
b = random.randint(1, 10)

print("Find the product of the numbers  :", a , " * ", b)
product = a*b
print("Please Enter your answer")
guess = int(input("Answer   "))

if(product == guess):
    print ("Your answer is correct, Congrats!")

else:
    print("Sorry, you should try again, the real answe is : " , product)
exit()