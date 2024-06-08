import modulebank as system

def main_menu():
    print('\nBanking System by Chappuis CS. Select Menu:')
    print('1. Create Account')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Check Balance')
    print('5. Exit')

while True:
    main_menu()
    try:
        choice = int(input('\nSelect menu: '))
        if choice == 1:
            system.create_account()
        elif choice == 2:
            system.deposit_money()
        elif choice == 3:
            system.withdraw_money()
        elif choice == 4:
            system.check_balance()
        elif choice == 5:
            system.exit()
            break
        else:
            print('Please enter a valid menu number.')
    except ValueError:
        print('Please enter a valid menu number.')
