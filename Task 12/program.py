import calculator as modcalc

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
            if operation not in modcalc.opr:
                print('Invalid operation.')
            else:
                print(f'\n{num1} {operation} {num2} = {modcalc.calc(num1, num2, operation)}')
        elif choice == 2:
            break
            exit()
        else:
            print('Wrong input.')
    except ValueError:
        print('Wrong input.')