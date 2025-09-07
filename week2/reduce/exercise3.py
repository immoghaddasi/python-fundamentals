"""

Using reduce, concatenate a list of words into a sentence separated by spaces (avoid
a leading/trailing space).
"""

from functools import reduce

words = ["I", "am", "in", "the", "IAAA", "bootcamp"]

# Use reduce to join words with a space
sentence = reduce(lambda acc, word: acc + " " + word, words)

print(sentence)