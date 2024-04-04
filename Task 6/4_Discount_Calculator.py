# Discount Calculator: Create a program that calculates the total cost after applying a discount 
# based on the following conditions:
# If the purchase amount is greater than $100, apply a 10% discount.
# If the purchase amount is greater than $50 but less than or equal to $100, apply a 5% discount.
# If the purchase amount is less than or equal to $50, apply no discount.

price =  int(input("\nEnter Price: "))

if (price > 100): 
    
    discount = int(price * 0.1)
    total_cost = price - discount
    print("\nCost greater than $100")
    print("You got discount 10%.")
    print(f"Total cost after discount: ${total_cost}\n")
elif(price > 50 and price <= 100):
    discount = int(price * 0.05)
    total_cost = price - discount
    print("\nCost greater than $50 but less than or equal to $100")
    print("You got discount 5%.")
    print(f"Total cost after discount: ${total_cost}\n")
else: 
    print("Cost less than or equal $50, you got no discount.\n")