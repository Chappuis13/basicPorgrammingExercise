#Develop a program that checks if a user's age is between 18 and 65 (inclusive) and prints whether they are eligible to vote.

#loop
while True:
    try:
        #let user to input age
        age = int(input("Enter your age here: "))
        
        if (age >= 18 and age <= 65):
        #if age is between 18 and 65
            print(f"Your age {age} is eligible to vote")
        else:
            print(f"Your age {age} is not eligible to vote")
        
        #stop looping
        break
    
    except ValueError:
        #if the input is not number, show wrong input message and loop back to the input
        print("Wrong input. Please input number.")