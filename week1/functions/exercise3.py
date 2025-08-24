"""

Write a function that takes a string and returns the number of vowels in it.
"""

# Define a function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    # Loop through each character in the string
    for ch in text:
        if ch in vowels:
            count += 1
    
    return count

# Test the function
print(count_vowels("Hello IAAA"))

