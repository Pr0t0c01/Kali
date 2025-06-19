import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
domain_extract_file = sys.argv[3]

domain_scope = []
filter_subdomain = []

with open(domain_extract_file, 'r') as f_domain:
    for extract_domain in f_domain:
        domain_scope.append(extract_domain.strip())

with open(input_file, 'r') as f_input:
    for domain in f_input:
        for specific_domain in domain_scope:
            if specific_domain in domain:
                filter_subdomain.append(domain.strip())

with open(output_file, 'w') as f_output:
    for eachdomain in filter_subdomain:
        f_output.write(eachdomain + '\n')
