# Set item [name, price, stock]
item1 = ["Lipstick"      , 100000, 10]
item2 = ["Face Primer"     , 150000, 5]
item3 = ["Foundation"   , 200000, 2]
item4 = ["Eyeliner"     , 150000, 7]
item5 = ["Blush On"        , 50000 , 4]

# Set transaction
trans = 0
profit = 0

# Define a function transaction
def transaction(item):
    global profit
    global trans
    if item[2] == 0:
        print(f"{item[0]} is out of stock.\n")
    else:
        much = int(input("How Much?: "))
        if much > item[2]:
            print(f"Insufficient Stock. {item[2]} {item[0]}s available.\n")
        else:
            item[2] -= much
            total = int(much * (item[1] + (item[1] * 0.10)))
            profit += int(much * (item[1] * 0.10))
            trans += 1

            print(f"\n Selling {much} {item[0]}")
            print(f" Total \t\t\t: RP. {total:,}")
            display()
            print(f" Today transaction \t: {trans}")
            print(f" Today Profit \t\t: RP. {profit:,}")
            print("----------------------------------------------------------------")

# Display the name of the item price and available stock.
def display():
    print("\n COSMETIC LISTS & PRICES : \n----------------------------------------------------------------")
    print("No.| Name\t\t| Supplier Price\t| Price to Sell\t| Stock\n----------------------------------------------------------------")
    print(f"1.   {item1[0]}\t\t  Rp. {item1[1]:,}\t\t  Rp. {int(item1[1] + (item1[1] * 0.10)):,}\t  {item1[2]}")
    print(f"2.   {item2[0]}\t\t  Rp. {item2[1]:,}\t\t  Rp. {int(item2[1] + (item2[1] * 0.10)):,}\t  {item2[2]}")
    print(f"3.   {item3[0]}\t\t  Rp. {item3[1]:,}\t\t  Rp. {int(item3[1] + (item3[1] * 0.10)):,}\t  {item3[2]}")
    print(f"4.   {item4[0]}\t\t  Rp. {item4[1]:,}\t\t  Rp. {int(item4[1] + (item4[1] * 0.10)):,}\t  {item4[2]}")
    print(f"5.   {item5[0]}\t\t  Rp. {item5[1]:,}\t\t  Rp. {int(item5[1] + (item5[1] * 0.10)):,}\t  {item5[2]}")
    print("----------------------------------------------------------------")
display()

# Sell
while True:
    menu = input("Enter the item (number) you want to sell: ")
    if menu == '1':
        transaction(item1)
    elif menu == '2':
        transaction(item2)
    elif menu == '3':
        transaction(item3)
    elif menu == '4':
        transaction(item4)
    elif menu == '5':
        transaction(item5)
    else:
        print("\nBye bye.\n")
        break