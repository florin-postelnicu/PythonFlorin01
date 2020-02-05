

print("In this program we will check if a number is divisibleby 3, 5, and 15")
print("Enter your nymber ")
number = int(input("Number is :"))
if number% 15 == 0:
    print("The number you entered is divisible by 3, 5, and 15")
    print(number , " divided by 3  is ", number//3)
    print(number, " divided by 5  is ", number // 5)
    print(number, " divided by 30  is ", number // 15)
elif number % 5 == 0:
    print("The number you entered is divisible ONLY by 5")
    print(number, "  divided y 5 is ", number//5)
    print("Dividing  ", number , " by 3 , would give you a remainder ", number%3)
    print("Dividing  ", number, " by 15 , would give you a remainder ", number % 15)
elif number %3==0 :
    print("The number you entered is divisible ONLY by 3")
    print(number, "  divided by  3  is ", number // 3)
    print("Dividing  ", number, " by 5 , would give you a remainder ", number % 5)
    print("Dividing  ", number, " by 15 , would give you a remainder ", number % 15)

else:
    print("Your number :", number, " is not divisible by any of the numbers 3, 5, or 15")
    print("Dividing  ", number, " by 3 , would give you a remainder ", number % 3)
    print("Dividing  ", number, " by 5 , would give you a remainder ", number % 5)
    print("Dividing  ", number, " by 5 , would give you a remainder ", number % 15)
