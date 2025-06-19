#! /usr/bin/python3
import argparse
import re

# create argument parser
parser = argparse.ArgumentParser(description='Read multiple text files and output unique lines')

# add input file arguments
parser.add_argument('input_files', nargs='+', help='Input files to read')
args = parser.parse_args()

output_file = "allsubdomain.txt"

# initialize list to hold data from input files
data = []

# Regex pattern to match http URLs with port 443
pattern = re.compile(r"^http://([^/:]+):443(/.*)?$")

# read data from input files and append to list
for file_name in args.input_files:
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            match = pattern.match(line)
            if match:
                hostname, path = match.groups()
                path = path if path else ""
                updated_url = f"https://{hostname}{path}"
                data.append(updated_url)
            else:
                data.append(line)

# remove duplicates from data list
data = list(set(data))
data.sort()

# write data to output file
with open(output_file, 'w') as file:
    for line in data:
        file.write(line + '\n')
