"""

Given a list of integers, use filter to keep only the positive numbers.
"""

nums = [-5, -1, 0, 2, 7, -3, 10]

# Use filter with a lambda function to keep only positive numbers
positives = filter(lambda num: num > 0, nums)

print(list(positives))