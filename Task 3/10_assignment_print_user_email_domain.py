#Take a user's email address as input and extract the domain name. Print the domain name.

#loop
while True:
    try:
        #let user input the email
        email = input("Input your email here: ")
        
        #takes the domain after '@' character
        domain_start = email.index('@') + 1
        domain = email[domain_start:]
        
        #print the result
        print("The domain name is", domain)

        #stop looping
        break
    
    except ValueError:
        # if the input there is no domain (no '@' character),
        # show wrong input message and loop back to the input
        print("Wrong input. Please input an email.")