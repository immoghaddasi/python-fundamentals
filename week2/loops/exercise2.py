"""

Using a while loop, ask the user to enter numbers until they type 0. Print the sum of
all entered numbers (excluding 0).
"""

res = 0

# Infinite loop that will stop when user enters 0
while True:
    num = int(input("Please enter your number: "))
    # If the user enters 0, exit the loop
    if num == 0:
        break
    
    # Add the entered number to the total sum
    res += num

print("The sum of entered numbers is:", res)
