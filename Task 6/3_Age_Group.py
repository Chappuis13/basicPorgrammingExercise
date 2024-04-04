# Age Group Classifier: Develop a program that takes a person's age as input and then outputs their age group:
# Child: 0-12 years
# Teenager: 13-19 years
# Adult: 20+ years

age = int(input("Input Your Age: "))

if age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20:
    print("Adult")