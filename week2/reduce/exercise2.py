"""

Using reduce, find the longest string in a list of strings.
"""

from functools import reduce

words = ["apple", "banana", "kiwi", "strawberry", "pear"]

# Use reduce to find the longest string
longest_str = reduce(lambda acc, word: word if len(word) > len(acc) else acc, words)

print(longest_str)