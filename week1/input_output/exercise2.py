"""

Ask the user for two numbers and print their sum, difference, product, and division.
"""

# Ask the user for two numbers
num1 = int(input("Please Enter The First Number: "))
num2 = int(input("Please Enter The Second Number: "))

# Calculate sum, difference, product, and division
_sum = num1 + num2
_difference = num1 - num2
_product = num1 * num2
_division = num1 / num2 if num2 != 0 else "Undefined"

# Print the results
print(f"Sum: {_sum}")
print(f"Difference: {_difference}")
print(f"Product: {_product}")
print(f"Division: {_division}")