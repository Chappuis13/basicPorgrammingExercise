# Find the Largest and Smallest Number in a List [10, 20, 5, 40, 30, 72, 34]
number = [10, 20, 5, 40, 30, 72, 34]
max_num = number[0]
min_num = number[0]

for num in number:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num

print(f"\n{number}")
print(f"The largest number: {max_num}")
print(f"The smallest number: {min_num}")