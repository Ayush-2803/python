#game to guess the number 

import random
randNo = random.randint(1,100) 
guess_counter = 0
user_guess = None

while (user_guess != randNo):
    user_guess = int(input("Enter your Guess : "))
    guess_counter += 1
    if (user_guess == randNo):
        print("You guessed it right! ")
    else :
        if (user_guess > randNo):
            print("You guessed it wrong !! Guess a smaller number")
        else:
            print("You guessed it wrong !! Guess a larger number")

print(f"You guessed it in {guess_counter} number of guesses !!!")
with open ("hiscore.txt", "r") as f:
    hiscore = int(f.read())
if(guess_counter<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guess_counter)) 