#!/usr/bin/python3

import urllib.parse
import sys

def decode_url(url):
    return urllib.parse.unquote(url)

def decode_urls_in_file(file_name):
    with open(file_name, 'r') as file:
        urls = file.read().splitlines()

    decoded_urls = [decode_url(url) for url in urls]

    with open(file_name, 'w') as file:
        file.write('\n'.join(decoded_urls))

    print("URLs have been decoded and overwritten in:", file_name,"\n")

if __name__ == '__main__':
    file_name = sys.argv[1]
    decode_urls_in_file(file_name)
