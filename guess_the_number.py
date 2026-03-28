import time
import random
number = random.randint(1,100)
print(number)

print("welcome to the Number guessing game")
time.sleep(1)
print("You have 10 turns to enter the right number \n The Number Would be between  1 t0 100")

while True:
    
    guessed =int(input("Enter the Number: "))
    
    if guessed == number:
        print("You Guessed the right number : !!!")

    elif guessed > number:
        print("Enter the smallest number:  ")

    else:
        print("Enter the larger number:   ")

