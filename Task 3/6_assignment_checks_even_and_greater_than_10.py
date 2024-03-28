#Implement a program that checks if a number is even and greater than 10.

#Loop
while True:
    try:
        #let user to input the numbers
        num = int(input("Enter any number to test whether it is odd or even and greater than 10: "))

        if (num % 2) == 0:
        #if the number divided by 2 is equal to zero
            if num > 10:
            #if the number is greater than 10
                print (f"The number {num} is even and greater than 10.")
            else:
                print (f"The number {num} is even and not greater than 10.")
        else:
        #if the number divided by 2 is not equal to zero
            if num > 10:
                print (f"The number {num} is odd and greater than 10.")
            else:
                print (f"The number {num} is odd and not greater than 10.")
        #stop looping
        break
    
    #if the input is not number, show wrong input message and loop back to the input
    except ValueError:
        print("The input is wrong, please input a number.")