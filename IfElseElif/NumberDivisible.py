

print(" Enter a positive integer")

number = int(input(" Enter your number now  number   "))

# Decide if your number is divisible by a positive divisor

print(" Enter your divisor  ")
divisor = int(input("Enter a positive integer as a divisor "))

if number % divisor == 0:
    print(" number " , number ,"  is divisible by divisor ", divisor)
    print("\nsince ", number , " = ", divisor , " * ", number//divisor)
else:
    print(" number ", number, "  is NOT divisible by divisor ", divisor)
    print("\nsince the remainder when dividing ", number, " by ", divisor, " is  ", number % divisor)

