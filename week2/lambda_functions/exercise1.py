"""

Sort a list of tuples [(name, age)] by age using sorted with a lambda key.
"""

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("David", 20)]

# Sort the list by the second element of each tuple (age)
sorted_people = sorted(people, key = lambda person: person[1])

print(sorted_people)