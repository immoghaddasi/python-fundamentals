"""

Mini-Project: Shopping List Manager:
1.Ask the user how many items they want to add.
2.Input each item's name and price.
3.Store them in a list of tuples (item_name, price).
4.Functions: display all items, calculate total cost, find the most expensive item
"""

# Function to display all items
def display_all_items(items):
    for item in items:
        print(f"Item: {item[0]}, Price: {item[1]}")
        
# Function to calculate the total cost of all items
def calculate_total_cost(items):
    total_cost = 0
    for item in items:
        total_cost += item[1]
        
    return total_cost

# Function to find the most expensive item in the list
def find_most_expensive_item(items):
    most_exp_item = items[0]
    for item in items:
        if item[1] > most_exp_item[1]:
            most_exp_item = item
            
    return most_exp_item

# Ask the user how many items they want to add
num_of_items = int(input("How many items do you want to add? ")) 

shopping_list = []
# Loop to take user input for each item
for i in range(num_of_items):
    name = input(f"Please enter the name of item {i + 1}: ")
    price = float(input(f"Please enter the price of {name}: "))
    shopping_list.append((name, price))

display_all_items(shopping_list)
print(f"The total cost is: {calculate_total_cost(shopping_list)}$")

exp_item = find_most_expensive_item(shopping_list)
print(f"Most Expensive Item: {exp_item[0]} with price {exp_item[1]}")