"""

Given a tuple of numbers, count how many times a number (entered by the user) appears.
"""

# Define a tuple of numbers
nums = (1, 2, 3, 2, 2, 1, 4, 5, 5, 5, 5, 3, 2, 4, 1, 3, 3)

# Ask the user for a number
user_num = int(input("Enter a number: "))


count = 0
# Loop through the tuple
for num in nums:
    if num == user_num:
        count += 1

# Print the result
print(f"The number {user_num} appears {count} times.")
