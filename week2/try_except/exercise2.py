"""

Write a function read_int_until_valid(prompt) that loops asking the user
for an integer and uses try/except to keep asking until a valid integer is entered.
Return the integer.
"""

def read_int_until_valid(prompt):
    while True:
        try:
            # Try converting the user input into an integer
            return int(input(prompt))
        except ValueError:
            # If conversion fails, show an error and repeat
            print("Invalid input. Please enter a valid integer.")


number = read_int_until_valid("Enter an integer: ")
print(f"You entered: {number}")