import random
import math
def Number_Guessing(a,b):
   x = random.randint(a,b+1)
   print(f"Guess the number between {a} and {b}! You have 3 attempts.")

   while True:
       count = 3
       guess = int(input("Enter your guess: "))

       if guess == x:
           print(f"Congratulations! You guessed the correct number, {x}")
           break
       elif guess > x:
           print("Your guess is too high. Try again.")
       else:
           print("Your guess is too low. Try again.")

       count -= 1

       if count == 0:
           print(f"You've run out of attempts. The correct number was {x}.")
           break
a = int(input("Enter the lower limit of the range: "))
b = int(input("Enter the upper limit of the range: "))
Number_Guessing(a,b)
