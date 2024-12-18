#python program to make a rock paper scissors game
import random

def game(comp,user):
    #declaration of tie
    if comp == user :
        return None
    #check possibilities if comp chooses rock
    elif comp == "r":
        if user == "p":
            return True
        elif user == "s":
            return False
    #check possibilities if comp chooses paper
    elif comp == "p":
        if user == "s":
            return True
        elif user == "r":
            return False
    #check possibilities if comp chooses scissors
    elif comp == "s":
        if user == "r":
            return True
        elif user == "p":
            return False
        
print("\n Welcome to our game Rock Paper Scissors")
choice = random.randint(1,3)
if choice == 1:
    comp = "r"
elif choice == 2:
    comp = "p"
else:
    comp = "s"

user = input("\n Your Turn Rock(r) Paper(p) Scissors(s) : ")
print("Computer chose : ", comp)
print("Your choice : ", user)

fun = game(comp,user)
 
if fun == None:
    print("The Game is a tie")
elif fun == True:
    print("You Win !!!")
elif fun == False:
    print("You Lose !!!")
