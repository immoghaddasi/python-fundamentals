"""

Write a function count_occurrences(items, target) that returns how
many times target appears in the list items
"""

# Function to count how many times 'target' appears in the list 'items'
def count_occurrences(items, target):
    res = 0
    for item in items:
        if item == target:
            res += 1
            
    return res

# Example list
my_list = [1, 2, 3, 2, 4, 2, 5]
result = count_occurrences(my_list, 2)

print("Number of times 2 appears:", result)
