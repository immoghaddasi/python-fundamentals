"""

Use map to transform a list of strings ["1","2","3","-4"] into integers. Filter
out any values that cannot be converted (hint: use a helper function that returns
None on failure and then remove None later).
"""

# Helper function to safely convert string to int
def to_int(string):
    # Remove leading '-' and check if the rest are digits
    if string.lstrip("-").isdigit():
        return int(string)
    else:
        return None
    
strings = ["1","2","3","-4"]

# Apply the helper function using map
mapped = map(to_int, strings)

# Remove None values to keep only valid integers
new_list = [num for num in mapped if num is not None]

print(new_list)