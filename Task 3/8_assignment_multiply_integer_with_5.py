#Write a Python script that multiplies a given integer by 5.

while True:
    try:
        #let user to input the integer value
        num = int(input("Input an integer value to multiply it by 5: "))
        print("The result is: ", int(num * 5))
        
        #stop looping
        break
        
    #if the input is not number, show wrong input message and loop back to the input
    except ValueError:
        print("The input is wrong, please input an integer value.")