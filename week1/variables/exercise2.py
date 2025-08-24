"""

Swap the values of two variables without using a third variable.
"""

# Assign initial values
num1 = 5
num2 = 10

# Print original values
print(f"Before swap: Number1 = {num1}, Number2 = {num2}")

# Swap values without a third variable
num1, num2 = num2, num1

# Print swapped values
print(f"After swap: Number1 = {num1}, Number2 = {num2}")