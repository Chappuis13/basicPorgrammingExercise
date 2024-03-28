#Write a Python script that calculates the sum of digits in a given integer.

#Define a function
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

#Loop
while True:
    try:
        #let user to input the integer
        num = int(input("Input the integer: "))
        print(f"The sum of digits in {num} is {sum_of_digits(num)}")
        
        #stop looping
        break
    
    #if the input is not an integer, show wrong input message and loop back to the input
    except ValueError:
        print("The input is wrong, please input some integer.")