#Make a simple calculator application using functions.
opr = ['+', '-', '*', '/']
def calc(num1, num2, opr):
    if opr == '+':
        result = num1 + num2
    
    if opr == '-':
        result = num1 - num2
    
    if opr == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
        
    if opr == '*':
        result = num1 * num2
        
    return result

while True:
    print('\nSimple Calculator')
    print('1. Start calculator')
    print('2. Exit')
    choice = int(input('\nSelect menu: '))
    try:
        if choice == 1:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input('Choose the operation (+ - / *): ')
            if operation not in opr:
                print('Invalid operation.')
            else:
                print(f'\n{num1} {operation} {num2} = {calc(num1, num2, operation)}')
        elif choice == 2:
            break
            exit()
        else:
            print('Wrong input.')
    except ValueError:
        print('Wrong input.')