#Take two strings as input and concatenate them. Print the resulting string.

#let user input the first name and also make it as string
firstName = str(input("Input your first name: "))

#let user input the last name and also make it as string
lastName = str(input("Input your last name: "))

#concatenate them
fullName = str(firstName + " " + lastName)

#print the result
print(fullName)