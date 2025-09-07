"""

From a list of words, use filter to keep only those with length ≥ 5.
"""

words = ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "strawberry", "pear"]

# Use filter with a lambda function to keep words with length >= 5
long_words = filter(lambda word: len(word) >= 5, words)

print(list(long_words))