# #making a calculator
# Project: Simple Calculator
# Features
# The calculator will prompt the user to choose an operation.
# It will take two numbers as inputs.
# Perform the selected operation.
# Display the result.
# Allow the user to perform multiple calculations until they choose to exit.

def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    if b == 0:
        return "Error ! Div by 0"
    else :
        return a/b
    
def display_menu():
    print("\nSimple Calculator")
    print("Select Operation")
    print(" 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for exit ")

def calculator():
    while True:

        display_menu()
        choice = int(input("\nEnter your choice : "))

        if choice == 5:
            print("Exitting the Calculator")
            break
        
        if choice in {1,2,3,4}:
            try:
                num1 = float(input("Enter a number : "))
                num2 = float(input("Enter other number : "))
            except ValueError:
                print("Invalid !!! Enter a valid number.")

            if choice == 1:
                print(f"The resuilt is {add(num1,num2)}")
            elif choice == 2:
                print(f"The resuilt is {subtract(num1,num2)}")
            elif choice == 3:
                print(f"The resuilt is {multiply(num1,num2)}")
            elif choice == 4:
                print(f"The resuilt is {divide(num1,num2)}")
        else:
            print("Invalid choice !!! Enter a valid choice") 

#main code

calculator()