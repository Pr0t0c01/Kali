#! /usr/bin/python3
import argparse

# create argument parser
parser = argparse.ArgumentParser(description='Read multiple text files and output unique lines')

# add input file arguments
parser.add_argument('input_files', nargs='+', help='Input files to read')
args = parser.parse_args()

# define input file names
output_file = input("Enter Output File Name : ")

# initialize list to hold data from input files
data = []

# read data from input files and append to list
for file_name in args.input_files:
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip())

# remove duplicates from data list
data = list(set(data))
data.sort()

# write data to output file
with open(output_file, 'w') as file:
    for line in data:
        file.write(line + '\n')
