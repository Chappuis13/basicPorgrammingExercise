# Simple Calculator: Develop a simple calculator program that takes two numbers and an operator
# (+, -, *, /) as input and performs the corresponding operation.

num1 = int(input("\nInput the first number: "))
num2 = int(input("Input the second number: "))
opr = input("Choose the operations (+, -, *, /): ")

if opr == '+':
    res = int(num1 + num2)
    print(f"\n{num1} {opr} {num2} = {res}")
elif opr == '-':
    res = int(num1 - num2)
    print(f"\n{num1} {opr} {num2} = {res}")
elif opr == '*':
    res = int(num1 * num2)
    print(f"\n{num1} {opr} {num2} = {res}")
elif opr == '/':
    res = int(num1 / num2)
    print(f"\n{num1} {opr} {num2} = {res}")
else:
    print("\nError.")