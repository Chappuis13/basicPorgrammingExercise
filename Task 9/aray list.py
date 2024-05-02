# Drinkking Shop
product = []


while (True):
  print("Select Item")
  print("1. Add products")
  print("2. Delete products by index")
  print("3. Delete products by name")
  print("4. List the products")
  print("5. Exit")
  selected_menu = input("select menu(1/2/3/4/5): ")

# input product
  if(selected_menu == "1"):
    new_products = input('Add your product : ')
    product.append(new_products)

# delete product by index
  if(selected_menu == "2"):
    product.pop(int(input("input your deleted index :")))
    
# delete product by name
  if(selected_menu == '3'):
    product.remove(input("input your deleted array:"))

# print product
  if(selected_menu == '4'):
    print("your item is :")
    print(product)

# exit
  if(selected_menu == '5'):
    break
  
  



