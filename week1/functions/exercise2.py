"""

Write a function that takes a list of numbers and returns the largest number.
"""

# Define a function to find the largest number in a list
def largest_num(nums):
    # Assume the first number is the largest
    max_num = nums[0]
    # Loop through the list and update max_num if a bigger number is found
    for num in nums:
        if num > max_num:
            max_num = num
    
    return max_num

# Test the function
print(largest_num([3, 7, 2, 9, 5]))