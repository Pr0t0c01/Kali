#!/usr/bin/python3

import requests
import argparse
from bs4 import BeautifulSoup

description = "Web Directory Extractor via <a href=?>. I purposed it to be useful in some ctf."

parser = argparse.ArgumentParser(description=description)
parser.add_argument("-u", "--url", help = "add target url")

args = parser.parse_args()
target = args.url

def scrape_dir(base_url):
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = base_url + href
            print(f"[{response.status_code}] {full_url}")
            scrape_dir(full_url)

    except requests.RequestException as e:
        print(f"[x] Exception: {e}")

scrape_dir(target)
