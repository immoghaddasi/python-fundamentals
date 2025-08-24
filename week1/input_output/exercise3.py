"""

Ask the user for their birth year and print their age (assume the current year is 2025).
"""

# Ask the user for their birth year
birth_year = int(input("Please Enter Your Birth Year: "))

# Assume the current year is 2025
current_year = 2025

# Calculate age
age = current_year - birth_year

# Print the result
print(f"You Are {age} Years Old!")