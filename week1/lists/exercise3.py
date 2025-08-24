"""

Write a program that removes duplicates from a list.
"""

# Original list with duplicates
original_list = [1, 2, 3, 2, 4, 1, 5]

# Initialize an empty list to store unique elements
unique_list = []

# Loop through the original list
for i in range(len(original_list)):
    # Check if the current item already exists in unique_list
    is_duplicate = False
    for j in range(len(unique_list)):
        if original_list[i] == unique_list[j]:
            is_duplicate = True
            break
    # If not duplicate, add to unique_list
    if not is_duplicate:
        unique_list.append(original_list[i])

# Print the list without duplicates
print("Original list:", original_list)
print("List after removing duplicates:", unique_list)