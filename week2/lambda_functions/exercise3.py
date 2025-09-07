"""

Given a list of strings, sort them by their last character using a lambda with sorted.
"""

words = ["apple", "banana", "kiwi", "pear", "orange"]

# Sort the list by the last character of each string
sorted_words = sorted(words, key = lambda word: word[-1])

print(sorted_words)