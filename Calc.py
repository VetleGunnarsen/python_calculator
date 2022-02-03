from tkinter import E


number1: int = int(input("enter first number: "))
action = input("enter the action: ")
number2 = int(input("enter second number: "))

def my_calc():
        if action == "+":
            print(number1 + number2)
            
        elif action == "-":
            print(number1 - number2)
           
        elif action == "*":
            print(number1 * number2)
            
        elif action == "/":
            print(number1 / number2)
            
        else:
            print("do better!")
            my_calc()

while True:
    mode = input("press q to close or press n to do a new calculation")
    if mode == "q":
        break
    elif mode == "n":
        my_calc()