#! /usr/bin/python3

import re
import sys

def extract_urls(input_file, output_file):
    with open(input_file, 'r') as infile:
        text = infile.read()
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        with open(output_file, 'w') as outfile:
            for url in urls:
                outfile.write(url + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    extract_urls(input_file, output_file)
