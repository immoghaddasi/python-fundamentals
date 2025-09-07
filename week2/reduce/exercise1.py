"""

Using functools.reduce, compute the product of all numbers in a list (e.g.,
[2,3,4] -> 24).
"""

from functools import reduce

nums = [2, 3, 4]

# Use reduce with a lambda function to compute the product
product = reduce(lambda x, y: x * y, nums)

print(product)