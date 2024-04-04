# Grade Calculator: Create a program that takes a student's score as input and then
# outputs their corresponding letter grade based on the following criteria:
# A: 90-100     D: 60-69
# B: 80-89      E: 0-59
# C: 70-79

score = int(input("Input your exam score: "))

if(score >= 90) and (score <= 100):
    print("\nYour Grade is A")
elif(score >= 80) and (score <= 89):
    print("\nYour Grade is B")
elif(score >= 70) and (score <= 79):
    print("\nYour Grade is C")
elif(score >= 60) and (score <= 69):
    print("\nYour Grade is D")
elif(score >= 0) and (score <= 59):
    print("\nYour Grade is E")
else:
    print("\nYou input invalid score. There's no grade for you lmao.")