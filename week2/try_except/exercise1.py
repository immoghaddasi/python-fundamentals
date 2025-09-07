"""

Write a function safe_divide_list(nums, d) that divides each number in
nums by d. Use a loop and try/except to handle division by zero and non-numeric
values; return a new list where invalid divisions are replaced with None.
"""

def safe_divide_list(nums, d):
    results = []
    
    for num in nums:
        try:
            # Try dividing the number by d
            results.append(num / d)
        except (ZeroDivisionError, TypeError):
            # If division by zero OR non-numeric value -> add None instead
            results.append(None)
    
    return results


nums = [10, 20, "hello", 30]
print(safe_divide_list(nums, 5))
print(safe_divide_list(nums, 0))