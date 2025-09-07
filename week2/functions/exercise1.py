"""

Write a function is_prime(n) that returns True if n is prime and False otherwise.
Use it to print all primes from 2 to 100.
"""

# Function to check if a number is prime
def is_prime(n):
    tot = 0
    for i in range(1, n+1):
        if n % i == 0:
            tot += 1

    return True if tot == 2 else False

    
# Loop through numbers from 2 to 100
for i in range(2, 101):
    if is_prime(i):
        print(i)
    