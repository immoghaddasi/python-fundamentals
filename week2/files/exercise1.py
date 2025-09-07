"""

Ask the user for a filename, then append a new line containing the current date and
time to that file. If the file doesn’t exist, create it.
"""

from datetime import datetime

# Ask user for a filename
filename = input("Enter filename: ")

now = datetime.now().strftime("%m/%d/%Y ; %H:%M")

# Open the file in append mode ("a"), create it if it doesn't exist
with open(filename, "a") as f:
    f.write(now + "\n")

print(f"Date and time appended to {filename}.")