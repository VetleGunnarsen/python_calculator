number1: int = int(input("enter first number: "))
action = input("enter the action: ")
number2 = int(input("enter second number: "))

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

e = input("press to close")
