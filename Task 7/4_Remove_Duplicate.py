# Remove Duplicates from a List: [1, 2, 3, 4, 2, 3, 5, 6, 1]

org_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
new_list = []

for num in org_list:
    if num not in new_list:
        new_list.append(num)
        
print(f"\nOriginal List:\n{org_list}")
print(f"\nRemoved duplicates: \n{new_list}")