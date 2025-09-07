"""

Write a program that copies the contents of input.txt to output.txt, but only lines that
are not empty and don’t start with #.
"""

# Copy only non-empty lines that don't start with '#'
def copy_filtered_lines(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            # Remove spaces/newline from start and end
            stripped = line.strip()
            
            # Skip empty lines and lines starting with '#'
            if stripped == "" or stripped.startswith("#"):
                continue
            
            # Otherwise write the line
            outfile.write(line)


copy_filtered_lines("input.txt", "output.txt")