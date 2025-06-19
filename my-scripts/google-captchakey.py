import requests
import argparse

# create argument parser
parser = argparse.ArgumentParser(description='Google Captcha Key POC ')

# add input file arguments
parser.add_argument('input_file', nargs='+', help='Google Captcha Key File')
args = parser.parse_args()

url = "https://www.google.com/recaptcha/api/siteverify"
input_file = args.input_file[0]

with open(input_file, 'r') as file:
    for key in file:
        key = key.strip()  # Remove newline character
        params = { "secret": key, "response": "Shiroe" }

        response = requests.post(url, data=params)
        json_response = response.json()

        if json_response["success"]:
            print(key + " is valid")
        else:
            print(key + " is invalid")
