# This script is to use together with "split command"
# "split -l <line-no> text.txt
# And then change output-file names into what you like names and it will append like file1.txt,file2.txt,etc...
# You must edit file_prefix, start=, and output_prefix. (extension is your opinion)

#!/usr/bin/env python3
import os

file_prefix = 'xa'  # Replace with the original file prefix

output_prefix = input("Enter Filename Prefix : ")  # Replace with the desired output file prefix
output_extension = '.txt'  # Replace with the desired output file extension

# Get the list of files matching the pattern
files = sorted([f for f in os.listdir('.') if f.startswith(file_prefix)])

# Rename the files
for i, file_name in enumerate(files, start=1):
    new_file_name = f'{output_prefix}{i}{output_extension}'
    os.rename(file_name, new_file_name)
