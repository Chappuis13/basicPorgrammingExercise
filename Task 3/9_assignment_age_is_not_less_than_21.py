#Implement a program that checks if a user's age is not less than 21.

#loop
while True:
    try:
        #let user to input age
        age = int(input("Enter your age here: "))
        
        if (age >= 21):
        #if age is 21 and more
            print("You're passed")
        else:
            print(f"Sorry, you didn't pass. Your age {age} is less than 21. ")
        
        #stop looping
        break
    
    except ValueError:
        #if the input is not number, show wrong input message and loop back to the input
        print("Wrong input. Please input number.")