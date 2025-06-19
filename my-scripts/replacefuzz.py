import urllib.parse

def replace_url_parameters_with_fuzz(url):
    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)
    
    # Extract query parameters
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    # Replace all parameter values with 'FUZZ'
    fuzzed_params = {param: ['FUZZ'] for param in query_params}
    
    # Rebuild the query string with fuzzed values
    fuzzed_query = urllib.parse.urlencode(fuzzed_params, doseq=True)
    
    # Reconstruct the URL with fuzzed parameters
    fuzzed_url = parsed_url._replace(query=fuzzed_query).geturl()
    
    return fuzzed_url

def process_urls(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for url in infile:
            url = url.strip()  # Remove any leading/trailing whitespace
            if url:  # Process only non-empty lines
                fuzzed_url = replace_url_parameters_with_fuzz(url)
                outfile.write(fuzzed_url + '\n')

# Example usage
input_file = 'openredirect.txt'  # Input file containing URLs
output_file = 'fuzzed_urls.txt'  # Output file to write fuzzed URLs

process_urls(input_file, output_file)
print(f"Fuzzed URLs have been written to {output_file}")
