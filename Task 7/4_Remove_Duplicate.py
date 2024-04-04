# Remove Duplicates from a List: [1, 2, 3, 4, 2, 3, 5, 6, 1]

org_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
new_list = list(set(org_list))

print(f"\n{org_list}")
print(f"Removed duplicates: ")
print(new_list)