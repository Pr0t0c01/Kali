#! /usr/bin/python3

import re
import sys
from urllib.parse import urlparse

data = []
filter_urls = []

def extract_urls(input_file):
    with open(input_file, 'r') as infile:
        text = infile.read()
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for url in urls:
            parsed_url = urlparse(url.strip())
            fulldomain = f"{parsed_url.scheme}://{parsed_url.netloc}"
            data.append(fulldomain)

def remove_duplicate(data):
    data = list(set(data))

def filter_protocol(urls):
    global filter_urls
    for url in urls:
        if url.startswith("http://"):
            https_url = "https://" + url[len("http://"):]
            if https_url in urls:
                continue
        filter_urls.append(url)
    
    filter_urls = list(set(filter_urls))
    filter_urls.sort()
    with open(output_file, 'w') as file:
        for url in filter_urls:
            file.write(url + '\n')

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    extract_urls(input_file)
    remove_duplicate(data)
    filter_protocol(data)