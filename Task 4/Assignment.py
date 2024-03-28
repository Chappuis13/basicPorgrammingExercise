while True:
    try:
        print('<<<<<<<<<<<<<--->>>>>>>>>>>>>')
        print('Check Profit 10% & Price Sell')
        print('<<<----------------------->>>')

        input_price = float(input("Enter the price: \t\t: Rp. "))
        selling_price = input_price * 1.1
        profit = selling_price - input_price
        
        
        print(f"The price is \t\t: Rp. {input_price}")
        print(f"The price to sell is \t: Rp. {selling_price}")
        print(f"The profit is \t\t: Rp. {profit}")
        print()
        break
    
    except ValueError:
        print('The input is wrong! Please input a number.')
