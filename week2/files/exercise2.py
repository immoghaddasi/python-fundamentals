"""

Given a text file of numbers (one per line), read the file and compute the average.
Handle empty files and invalid lines gracefully.
"""

def average_from_file(filename):
    numbers = []
    
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()  # remove extra spaces/newlines
            if not line:         # skip empty lines
                continue
            try:
                numbers.append(float(line))  # try convert to float
            except ValueError:
                # Skip invalid (non-numeric) lines
                continue
    
    # Handle case: no valid numbers
    if not numbers:
        return None
    
    return sum(numbers) / len(numbers)


filename = "nums.txt"
avg = average_from_file(filename)

if avg is None:
    print("No valid numbers found in the file.")
else:
    print(f"Average = {avg}")