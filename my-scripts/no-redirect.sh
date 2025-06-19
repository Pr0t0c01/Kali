#!/bin/bash

# Take user input
echo "Enter URL :"
read url

# Perform the curl request and store the response headers in a temporary file
response_headers=$(mktemp)
curl -sS -D "$response_headers" -o response_body.txt $url

# Extract the status code from the response headers
status_code=$(grep -i '^HTTP/1\.[01] [23].. ' "$response_headers" | tail -n 1 | awk '{print $2}')

# Check if the status code is 302 (Found or Moved Temporarily)
if [ "$status_code" = "302" ]; then
    # Check if the response body is not empty
    if [ -s "response_body.txt" ]; then
        echo "$url is can be no-redirect-vulnerability"
    else
        echo "No Vulnerable"
    fi
else
    echo "Response is not 302"
fi

# Clean up temporary files
rm "$response_headers" response_body.txt >/dev/null 2>&1
