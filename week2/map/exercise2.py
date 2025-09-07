"""

Given a list of Celsius temperatures, use map to convert them to Fahrenheit using the
formula F = C * 9/5 + 32 .
"""

# Function to convert Celsius to Fahrenheit
def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures = [0, 12, 25, 30, 37, 40, -5, -10]

# Apply the function to each temperature using map and convert to list
print(list(map(to_fahrenheit, temperatures)))
    