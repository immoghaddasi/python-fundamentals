"""

Implement sum_valid_numbers(text_values) that loops over a list like
["10", "abc", "3.5", "7"] and sums only the valid numeric entries (ints or
floats). Use try/except.
"""

def sum_valid_numbers(text_values):
    total = 0  # accumulator
    
    for val in text_values:
        try:
            # Try converting to float
            total += float(val)
        except ValueError:
            # Skip invalid values
            continue
    
    return total


values = ["10", "abc", "3.5", "7"]
print(sum_valid_numbers(values))