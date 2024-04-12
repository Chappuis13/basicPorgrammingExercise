# Reverse a String by input your name

name = str(input("\nInput Your Name: "))
rev_name = ""

for char in name:
    rev_name = char + rev_name

print(f"Reversed Name: {rev_name}")