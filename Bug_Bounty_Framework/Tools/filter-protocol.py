import sys

# This script is to sure that urls are end with / and remove duplication of http and https.
# Eg - http://google.com, https://google.com   --->   https://google.com/
# Usage - python3 filter-protocol.py <input.txt> <output.txt>

urls = []
filter_urls = []
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,'r') as file:
    for line in file:
        line = line.strip()
        if not line.endswith("/"):
            urls.append(line + "/")
        else:
            urls.append(line)
file.close()

urls = list(set(urls))
for url in urls:
    # Check if the URL starts with "http://"
    if url.startswith("http://"):
        # Check if there is a corresponding "https://" version of the same domain
        https_url = "https://" + url[len("http://"):]
        if https_url in urls:
            # If both HTTP and HTTPS versions exist for the same domain, discard the HTTP version
            continue
    filter_urls.append(url)

filter_urls = list(set(filter_urls))
filter_urls.sort()
with open(output_file, 'w') as file:
    for newurl in filter_urls:
         file.write(newurl + '\n')
