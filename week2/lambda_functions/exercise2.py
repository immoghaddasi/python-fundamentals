"""

Given prices = [120, 55, 300, 90], use a lambda with map to apply a 10% discount to
all prices and return the new list.
"""

prices = [120, 55, 300, 90]

# Apply a 10% discount to each price using map and a lambda function
discounted_prices = map(lambda price: price * 0.9, prices)

print(list(discounted_prices))