import random

while True:
    another_roll=input("Want to roll the dice again? (y/n):")
    if another_roll.strip().lower()=="y":
        print(random.randint(1,6))
        continue
    elif another_roll.lower()=="n": 
         print("Thank you for playing")
         break
    else:
         print("Enter valid input")
         continue
    
