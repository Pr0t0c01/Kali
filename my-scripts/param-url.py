import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

urls = []
fuzz_urls = []
nested_parameters = []
parameter_urls = []

pattern_1 = r"=(\w+)"
pattern_2 = r"[?&](.*?)="

with open(input_file,'r') as file:
    for line in file:
        line = line.strip()
        urls.append(line)
file.close()

for url_1 in urls:
    fuzz_url = re.sub(pattern_1, rf"=FUZZ", url_1)
    fuzz_urls.append(fuzz_url)
    fuzz_urls = list(set(fuzz_urls))

for url_2 in fuzz_urls:
    parameter_names = re.findall(pattern_2, url_2)
    nested_parameters.append(parameter_names)

parameters = [item for sublist in nested_parameters for item in sublist]   
parameters = list(set(parameters))

for parameter in parameters:
    for specific_url in fuzz_urls:
        if parameter in specific_url:
            parameter_urls.append(specific_url)

parameter_urls = list(set(parameter_urls))
parameter_urls.sort()
with open(output_file, 'w') as file:
    for newurl in parameter_urls:
         file.write(newurl + '\n')