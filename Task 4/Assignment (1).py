# Task 4

while True:
    try:
        print('==============================')
        print('Price of 10 percent Calculator')
        print('==============================')

        realPrice = float(input("Enter the price: \t\t: Rp. "))
        price = realPrice + (realPrice * 0.10)

        print(f"The price to sell is \t\t: Rp. {int(price):,}")
        print()
        break

    except ValueError:
        print('The input is wrong! please input number.')