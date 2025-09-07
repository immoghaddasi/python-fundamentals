"""

Print the multiplication table for a number n (from 1 to 10), where n is input by the
user.
"""

# Ask the user to enter a number
n = int(input("Please enter your number: "))

# Loop from 1 to 10 to create the multiplication table
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")