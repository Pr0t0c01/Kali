#! /usr/bin/python3
file1 = input("Enter File-1 : ")
file2 = input("Enter File-2 : ")
#output_file = input("Enter Output File: ")
print("")

# Read the contents of the two files
with open(file1, 'r') as file1, open(file2, 'r') as file2:
    lines1 = set(file1.read().splitlines())
    lines2 = set(file2.read().splitlines())

# Find the different strings
different_strings = lines1.symmetric_difference(lines2)

# Convert the result back to a list for easier manipulation
different_strings_list = list(different_strings)
print(different_strings)
# Print or save the different strings
#with open(output_file, 'w') as file:
    #for line in different_strings_list:
        #file.write(line + '\n')
