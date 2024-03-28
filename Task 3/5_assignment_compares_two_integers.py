#Write a program that compares two integers and prints whether they are equal, greater, or smaller.

#loop
while True:
    try:
        #let user input number
        x = int(input("Input the first number: "))
        y = int(input("Input the second number: "))
        
        if (x == y):
        #if the first number and second number are equal
            print(f"The first number: {x} and second number: {y} are equal.")
        elif (x > y):
        #if the first number is greater than second number
            print(f"The first number: {x} is greater than second number: {y}.")
        elif (x < y):
        #if the second number is greater than first number
            print(f"The second number: {y} is greater than first number: {x}.")
        
        #stop looping
        break
    
    #if the input is not integer, show wrong input message and loop back to the input
    except ValueError:
        print("The input is wrong, please input an integer value.")