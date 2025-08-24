"""

Ask the user to enter 5 numbers and store them in a list. Print the maximum and minimum.
"""

# Initialize an empty list
nums = []

# Ask the user to enter 5 numbers
for i in range(5):
    num = int(input(f"Please Enter Number{i+1}: "))
    nums.append(num)
    
# Initialize max and min with the first number
max_num = nums[0]
min_num = nums[0]
    
# Loop through the list to find max and min
for num in nums:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
        
# Print the results
print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")