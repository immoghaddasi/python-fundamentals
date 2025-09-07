"""

Given a list of names like ["ali", "Sara", "omid"], use map to return a new
list with each name capitalized (first letter uppercase, rest lowercase)
"""

# Function to capitalize the first letter of a string
def capital_first_letter(string):
    return string.capitalize()
    
names = ["ali", "Sara", "omid"]

# Apply the function to each element of the list using map and convert to list
print(list(map(capital_first_letter, names)))